from random import random
from typing import TextIO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit,QScrollArea,QLabel,QWidget,QVBoxLayout,qApp,QApplication
from PySide6 import QtWidgets,QtCore, QtGui
from PySide6.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit,QScrollArea,QLabel,QWidget,QVBoxLayout
from PySide6.QtGui import QFont, QImage, QPixmap
from PyQt5.QtGui import QFont, QImage, QPixmap
from main import Ui_HIS
import interface_actions as ac
import sqlite3
import win32com.client as client
from random import randint
from threading import Thread
import pythoncom 
import time 
import credentials
msgs=[]
l=[]
                        




class Master(QtCore.QObject):

    command = QtCore.Signal()

    def __init__(self):
        super().__init__()

class Mail(QtCore.QObject):

    def __init__(self):
        super().__init__()

    def run(self):
        pythoncom.CoInitialize()
        Auth().get_inbox(l,msgs)



class ScrollMessageBox(QMessageBox):
   def __init__(self, l, *args, **kwargs):
      QMessageBox.__init__(self, *args, **kwargs)
      scroll = QScrollArea(self)
      self.dragPos = QtCore.QPoint()
      scroll.setWidgetResizable(True)
      self.content = QWidget()
      scroll.setWidget(self.content)
      lay = QVBoxLayout(self.content)
      lay.addWidget(QLabel(l, self))
      self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
      self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
      self.setStyleSheet("QScrollArea{min-width:500 px; min-height: 400px; } QMessageBox{background-color:black;}"
      "QPushButton{background-color:white; border-radius:10px; font-size:10pt; font-weight:bold; min-width:40px; min-height:30px;}"
      "QLabel{font-size:9pt; font-weight:bold; background-color:white; color:blue;}"
      "QPushButton::pressed{\n"
      "background-color: rgb(0, 188, 138);\n"
      "color:white;\n"
"    border-style:inset;\n"
"\n"
"}"
      )

   def mousePressEvent(self, event):
       self.dragPos = event.globalPos()
        
   def mouseMoveEvent(self, event):
       if event.buttons() == QtCore.Qt.LeftButton:
           self.move(self.pos() + event.globalPos() - self.dragPos)
           self.dragPos = event.globalPos()
           event.accept()  

class Ui_SendDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("SendDialog")
        self.resize(400, 298)
        font = QtGui.QFont()
        font.setKerning(True)
        self.setFont(font)
        self.setWindowTitle("  ")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(6, 0, 4, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.d_frame = QtWidgets.QFrame(self)
        self.d_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.d_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d_frame.setObjectName("d_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.d_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dia_to = QtWidgets.QHBoxLayout()
        self.dia_to.setObjectName("dia_to")
        self.to_lbl = QtWidgets.QLabel(self.d_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.to_lbl.setText("To: ")
        self.to_lbl.setFont(font)
        self.to_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.to_lbl.setObjectName("to_lbl")
        self.dia_to.addWidget(self.to_lbl)
        self.to_input = QtWidgets.QLineEdit(self.d_frame)
        self.to_input.setStyleSheet("background-color: rgb(255, 255, 255); font-size:10pt; font-weight:bold;")
        self.to_input.setObjectName("to_input")
        self.dia_to.addWidget(self.to_input)
        self.verticalLayout_2.addLayout(self.dia_to)
        self.dia_sub = QtWidgets.QHBoxLayout()
        self.dia_sub.setObjectName("dia_sub")
        self.sub_lbl = QtWidgets.QLabel(self.d_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.sub_lbl.setText("Subject: ")
        self.sub_lbl.setFont(font)
        self.sub_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.sub_lbl.setObjectName("sub_lbl")
        self.dia_sub.addWidget(self.sub_lbl)
        self.sub_input = QtWidgets.QLineEdit(self.d_frame)
        self.sub_input.setStyleSheet("background-color: rgb(255, 255, 255);font-size:10pt; font-weight:bold;")
        self.sub_input.setObjectName("sub_input")
        self.dia_sub.addWidget(self.sub_input)
        self.verticalLayout_2.addLayout(self.dia_sub)
        self.send_txt = QtWidgets.QTextEdit(self.d_frame)
        self.send_txt.setStyleSheet("background-color: rgb(255, 255, 255);font-size:10pt; font-weight:bold;")
        self.send_txt.setObjectName("send_txt")
        self.verticalLayout_2.addWidget(self.send_txt)
        self.verticalLayout.addWidget(self.d_frame)
        self.d_send = QtWidgets.QPushButton(self)
        self.d_send.setMaximumSize(QtCore.QSize(80, 50))
        self.d_send.setText("Send")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        font.setKerning(True)
        self.d_send.setFont(font)
        self.d_send.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.d_send.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.d_send.setObjectName("d_send")
        self.verticalLayout.addWidget(self.d_send, alignment=QtCore.Qt.AlignRight)
        self.d_send.clicked.connect(self.send_message)
    
    def send_message(self):
        try:
            outlook=client.Dispatch("Outlook.Application")
            msg=self.send_txt.toPlainText()
            to=self.to_input.text()
            sub=self.sub_input.text()
            message=outlook.CreateItem(0)
            message.To=to
            message.Subject=sub
            message.Body=msg
            message.Send()
            print("sent")
            self.close()
        except Exception:
            print("error")

    


class Auth(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Auth,self).__init__()

        def login(self):
            try:
                user=self.log_name.text()
                password=self.log_pass.text()
                db = sqlite3.connect('./database/bmd303.db')
                cur = db.cursor()
                cur.execute('SELECT * from Staff WHERE st_name= "%s" AND st_pass="%s"' % (user, password))
                rec=cur.fetchone()
                cur.close()
                db.close()
                if rec is not None:
                   e_mail=rec[6]
                   role=rec[5]
                   img=rec[2]
                   pix=QtGui.QPixmap()
                   pix.loadFromData(img,"png")
                   self.user_photo.setPixmap(pix.scaled(150,150,QtCore.Qt.KeepAspectRatio))
                   self.user_photo.setAlignment(QtCore.Qt.AlignCenter)
                   self.main_pages_vwr.setCurrentIndex(0)
                   self.user_name.setText(user)
                   self.user_email.setText(e_mail)
                   self.user_role.setText(role)
                   self.nav_drw.show()
                   self.tgl_btn.show()
                   self.thread = QtCore.QThread()
                   self.thread.setTerminationEnabled(True)
                   self.email = Mail()
                   self.email.moveToThread(self.thread)

                   self.master = Master()
                   self.master.command.connect(self.email.run)

                    # Start the thread
                   self.thread.start()

                    # Emit the signal to start the task in the worker thread
                   self.master.command.emit()
                   

                   if role !="Admin":
                      self.home_options.removeTab(0)
                      self.home_options.setStyleSheet("QTabWidget::pane { border: 0; } QTabBar::tab { background: rgb(4, 4, 4);color: white;height:40px;width:740px;}")
                      connection=sqlite3.connect('database/bmd303.db')
                      self.staff_table.setHorizontalHeaderLabels(["ID","Name","Role","E-mail","Gender","Working Hours","Department"])
                      query="SELECT st_id,st_name,st_role,st_email,st_gender,st_workh,st_department FROM Staff"
                      res=connection.execute(query)
                      self.staff_table.setRowCount(0)
                      for row_num, row_data in enumerate(res):
                          self.staff_table.insertRow(row_num)
                          for col_num, data in enumerate(row_data):
                              self.staff_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))
                      connection.close()
                      self.staff_table.setColumnCount(7)
                      self.add_st_btn.hide()
                      self.update_st_btn.hide()
                      self.delete_st_btn.hide()
                      self.show_st_btn.hide()
                      if role=="Doctor":
                         self.pharmacy.hide()
                         self.radiology.hide()
                      elif role=="Pharmacist":
                          self.admission.hide()
                          self.radiology.hide()
                      elif role=="Radiologist":
                          self.pharmacy.hide()
                          self.admission_tab.removeTab(2)
                          self.admission_tab.removeTab(1)
                          self.admission_tab.setStyleSheet("QTabWidget::pane { border: 0; } QTabBar::tab { background: rgb(4, 4, 4);color: white;height:40px;Width:700px;}")
                          
                      elif role=="Nurse":
                          self.pharmacy.hide()
                          self.radiology.hide()
                          self.delete_p_btn.hide()
                          self.update_p_btn.hide()
                else:
                    QMessageBox.about(self," ","Invaild!!!!")
                    self.log_name.clear()
                    self.log_pass.clear()

            except Exception:
                QMessageBox.about(self," ","Invaild!!!!")
                self.log_name.clear()
                self.log_pass.clear()

               
        
        def log_clear(self):
            self.log_name.clear()
            self.log_pass.clear()

        def signup_clear(self):
            self.signup_name.clear()
            self.signup_pass.clear()
            self.signup_conf.clear()
            self.signup_role.clear()
            self.signup_email.clear()


        def sign_up(self):
            try:
                name=self.signup_name.text()
                email=self.signup_email.text()
                role=self.signup_role.text()
                pswrd=self.signup_pass.text()
                conf=self.signup_conf.text()
                if pswrd==conf and name !='' and role !='' and pswrd!='' and email!='' and conf!='':
                   outlook=client.Dispatch("Outlook.Application")
                   msg="\n\t Name: "+name+"\n\t E-mail: "+email+"\n\t Role: "+role+"\n\t Pass_word: "+pswrd
                   message=outlook.CreateItem(0)
                   message.To=credentials.MESSAGE_TO
                   message.Subject="New_signup_request "+str(randint(200,20000))
                   message.Body=msg
                   message.Send()
                   QMessageBox.about(self," ","Your request have been sent successfully!")
                   self.signup_name.clear()
                   self.signup_pass.clear()
                   self.signup_conf.clear()
                   self.signup_role.clear()
                   self.signup_email.clear()
                else:
                    QMessageBox.about(self," ","Check your inputs again!!!!")
                    self.signup_name.clear()
                    self.signup_pass.clear()
                    self.signup_conf.clear()
                    self.signup_role.clear()
                    self.signup_email.clear()
                   
            except Exception:
                QMessageBox.about(self," ","Invaild!!!!")
                self.signup_name.clear()
                self.signup_pass.clear()
                self.signup_conf.clear()
                self.signup_role.clear()
                self.signup_email.clear()

        def send_message(self):
            try:
                print("send message")
            except Exception:
                print("error")

        def get_inbox(self,l,msgs):
            pythoncom.CoInitialize()
            outlook =client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            inbox = outlook.GetDefaultFolder(6) 
            messages = inbox.Items
            messages.sort("ReceivedTime",True)
            message = messages.GetFirst()
            i=0
            while (messages and i<=6):
                if message.Class == 43:
                    body_sender = message.Sender
                else:
                    body_sender = message.SenderName 

                body_content = message.Body
                l.append(str(body_sender))
                msgs.append(str(body_content))
                message=messages.GetNext()
                i+=1
        def read_inbox(self):
            try:
                
                height=self.msgs_list.height()
                if height == 0:
                        new=370
                        self.animation=QtCore.QPropertyAnimation(self.msgs_list,b"maximumHeight")
                        self.animation.setDuration(300)
                        self.animation.setStartValue(height)
                        self.animation.setEndValue(new)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()
                        self.msgs_list.addItems(l)
                        self.thread.terminate()
                else:
                    new=0
                    self.animation=QtCore.QPropertyAnimation(self.msgs_list,b"maximumHeight")
                    self.animation.setDuration(300)
                    self.animation.setStartValue(height)
                    self.animation.setEndValue(new)
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                    self.animation.start()
                    self.msgs_list.clear()
                    


            except Exception as e:
                print(e)


        def item_click(self):
            global msgs
            cur=self.msgs_list.currentRow()
            res=ScrollMessageBox(msgs[cur],None)
            res.exec_()

        def send_msg(self):
            send=Ui_SendDialog()
            send.exec_()

           

        
                  



#############################################################
#QDialog code could be helpful in search
# d.setModal(True)
# d.resize(100,100)
# d.btn=QPushButton("ok",d)
# d.btn.setGeometry(QtCore.QRect(20,20,20,20))
# d.ed=QLineEdit(d)
# d.btn.clicked.connect(lambda:get(d,p_name))
# def get(d,pname):
#     x=d.ed.text()
#     return x
# d.exec()
# p_name=get(d,p_name)
# print(p_name)

########################################################

     

                    

