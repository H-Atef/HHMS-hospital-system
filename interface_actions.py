from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_HIS
from PySide6 import QtWidgets,QtCore, QtGui
import pandas as pd
from PySide6.QtGui import QStandardItemModel,QFont, QImage, QPixmap
from PyQt5.QtGui import QStandardItemModel,QFont, QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit,QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PySide6.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit,QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PySide6.QtCore import Qt 


#Globals
dval1=0
dval2=0
dval3=0
df=pd.read_csv("qr-code-attendance/attend.csv")

class Interface_actions(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Interface_actions,self).__init__()
                self.setAttribute(Qt.WA_DeleteOnClose)
                self.setupUi(self)
                self.dragPos = QtCore.QPoint()
                if self.main_pages_vwr.currentIndex()==5:
                        self.nav_drw.hide()
                        self.tgl_btn.hide()
                
        def mousePressEvent(self, event):
                self.dragPos = event.globalPos()

        def mouseMoveEvent(self, event):
                if event.buttons() == QtCore.Qt.LeftButton:
                        self.move(self.pos() + event.globalPos() - self.dragPos)
                        self.dragPos = event.globalPos()
                        event.accept()  

        def menu_slide(self):
            width=self.nav_drw.width()
            if width == 70:
                    newWidth=210
            else:
                    newWidth=70
            self.animation=QtCore.QPropertyAnimation(self.nav_drw,b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        def change_page(self,page_no):
                self.main_pages_vwr.setCurrentIndex(page_no)
                width=self.nav_drw.width()
                if width == 210:
                        newWidth=70
                else:
                        newWidth=70
                self.animation=QtCore.QPropertyAnimation(self.nav_drw,b"minimumWidth")
                self.animation.setDuration(300)
                self.animation.setStartValue(width)
                self.animation.setEndValue(newWidth)
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation.start()
        def Close(self):
                self.close()

        def minimize(self):
                 self.showMinimized()

        def drug_opt(self):
                height=self.opt_drw.height()
                if height == 0:
                        new=270
                        self.animation=QtCore.QPropertyAnimation(self.opt_drw,b"maximumHeight")
                        self.animation.setDuration(300)
                        self.animation.setStartValue(height)
                        self.animation.setEndValue(new)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()
                
                else:
                        new=0
                        self.animation=QtCore.QPropertyAnimation(self.opt_drw,b"maximumHeight")
                        self.animation.setDuration(300)
                        self.animation.setStartValue(height)
                        self.animation.setEndValue(new)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()


        def d_progress(self):
                number_of_nurses=df.Name.str.count('n-').sum()
                number_of_doctors=df.Name.str.count('d-').sum()
                global dval1,dval2,dval3
                self.pro1_d.rpb_setValue(dval1-1)
                self.pro2_d.rpb_setValue(dval2-1)
                self.pro3_d.rpb_setValue(dval3-1)
                m=number_of_doctors-number_of_nurses
                if(m>=0):
                        if dval1 > number_of_doctors:
                                dval1=number_of_doctors
                                self.timer.stop()
                        if dval2 > number_of_doctors:
                                dval2=number_of_doctors
                        if dval3 > number_of_nurses:
                                dval3=number_of_nurses

                if(m<0):
                        if dval1 > number_of_doctors:
                                dval1=number_of_doctors
                        if dval2 > number_of_doctors:
                                dval2=number_of_doctors
                        if dval3 > number_of_nurses:
                                dval3=number_of_nurses
                                self.timer.stop()
                dval1+=1
                dval2+=1
                dval3+=1
        
                