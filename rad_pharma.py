from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit,QScrollArea,QLabel,QWidget,QVBoxLayout
from PySide6 import QtWidgets,QtCore, QtGui
from PySide6.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit, QWidget,QScrollArea,QLabel,QWidget,QVBoxLayout
from main import Ui_HIS,get_image,set_image
import interface_actions as ac
import sqlite3
from datetime import datetime
import cv2







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
      self.setStyleSheet("QScrollArea{min-width:250 px; min-height: 250px; } QMessageBox{background-color:black;}"
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











class Pharma(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Pharma,self).__init__()

        def view_drug_data(self):
            connection=sqlite3.connect('database/bmd303.db')
            self.drug_table.setHorizontalHeaderLabels(["Code","Name","Description","Price","Amount"])
            query="SELECT * FROM Drug"
            res=connection.execute(query)
            self.drug_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.drug_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.drug_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        def InsertDrugInfo(self):
            try:
                connection=sqlite3.connect('database/bmd303.db')
                cur=connection.cursor()
                q = "INSERT INTO Drug(drug_code,drug_name,drug_desc,drug_price,drug_amount) VALUES(?,?,?,?,?)"
                i=(None,self.drug_name_input.text(),self.drug_desc_input.toPlainText(),self.drug_price_input.text(),self.drug_amount_input.text(),)
                cur.execute(q,i)
                connection.commit()
                cur.close()
                connection.close()
                QMessageBox.about(self," ","Drug Added Successfully!" )
                self.drug_name_input.clear()
                self.drug_desc_input.clear()
                self.drug_price_input.clear()
                self.drug_amount_input.clear()
                self.main_pages_vwr.setCurrentIndex(2)
            except Exception:
                QMessageBox.about(self," ","Invalid !!!!" )
                self.drug_name_input.clear()
                self.drug_desc_input.clear()
                self.drug_price_input.clear()
                self.drug_amount_input.clear()

        def ClearDrugData(self):
            self.drug_name_input.clear()
            self.drug_desc_input.clear()
            self.drug_price_input.clear()
            self.drug_amount_input.clear()

        

        def DeleteDrugInfo(self):
            connection=sqlite3.connect('database/bmd303.db')
            connection.execute("PRAGMA foreign_keys=1")
            query="SELECT * FROM Drug"
            cur = connection.cursor()
            res=cur.execute(query)
            for row in enumerate(res):
                if row[0]==self.drug_table.currentRow():
                    data=row[1]
                    d_ID=data[0]
                    cur.execute("DELETE FROM Drug WHERE drug_code=?",(d_ID,))
                    connection.commit()
            cur.close()
            connection.close()

        def ModifyDrugInfo(self):
            try:
                connection=sqlite3.connect('database/bmd303.db')
                connection.execute("PRAGMA foreign_keys=1")
                query="SELECT * FROM Drug"
                cur = connection.cursor()
                res=cur.execute(query)
                for row in enumerate(res):
                    if row[0]==self.drug_table.currentRow():
                        data=row[1]
                        #print(data)
                        d_ID=data[0]
                        d_name=data[1]
                        d_desc=data[2]
                        d_price=data[3]
                        d_amount=data[4]
                        d_name=self.drug_table.item(row[0],1).text()
                        d_desc=self.drug_table.item(row[0],2).text()
                        d_price=self.drug_table.item(row[0],3).text()
                        d_amount=self.drug_table.item(row[0],4).text()
                        s="UPDATE Drug SET drug_name=?,drug_desc=?,drug_price=?,drug_amount=? WHERE drug_code=?"
                        cur.execute(s,(d_name,d_desc,d_price,d_amount,d_ID))
                        connection.commit()
                cur.close()
                connection.close()
            except Exception:
                QMessageBox.about(self," ","error in data types take care")


        def search_drug(self):
            try:

                d_id=QtWidgets.QInputDialog.getText(self,"Drug Search","Enter Drug Code")
                # print(d_id)
                db = sqlite3.connect('./database/bmd303.db')
                self.drug_table.setHorizontalHeaderLabels(["Code","Name","Description","Price","Amount"])
                res=db.execute('SELECT * from Drug WHERE drug_code= "%s" ' % (d_id[0]))
                if d_id[1]==False:
                    db.close()
                    return

                elif res.fetchone() is None:
                   QMessageBox.about(self," ","Drug not found!!!!")
                   db.close()
                else:
                    db = sqlite3.connect('./database/bmd303.db')
                    res=db.execute('SELECT * from Drug WHERE drug_code= "%s" ' % (d_id[0]))
                    self.drug_table.setRowCount(0)
                    for row_num, row_data in enumerate(res):
                        self.drug_table.insertRow(row_num)
                        for col_num, data in enumerate(row_data):
                            self.drug_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

                    db.close()
                    

            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")



        def add_order(self):
            try:
                db=sqlite3.connect('database/bmd303.db')
                cur=db.cursor()
                dr_code=self.phar_code_input.text()
                query='select drug_price from Drug where drug_code= "%s" '%(dr_code)
                cur.execute(query)
                price=cur.fetchone()
                cur.close()
                db.close()

                db2=sqlite3.connect('database/bmd303.db')
                cur2=db2.cursor()
                p_id=self.phar_id_input.text()
                query2='select pat_id from Patient where pat_id= "%s" '%(p_id)
                cur2.execute(query2)
                pt_id=cur2.fetchone()
                if pt_id is None:
                    pt_id='Non-registered'
                else:
                    pt_id=pt_id[0]
                cur2.close()
                db2.close()
                connection=sqlite3.connect('database/bmd303.db')
                cur=connection.cursor()
                q = "INSERT INTO Order_mdcn(order_items,order_no,order_id,mdcn_code,mdcn_price,mdcn_amount,tran_date) VALUES(?,?,?,?,?,?,?)"
                date=datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                i=(None,self.phar_no_input.text(),pt_id,self.phar_code_input.text(),price[0],self.phar_amnt_input.text(),date,)
                cur.execute(q,i)
                connection.commit()
                cur.close()
                connection.close()
                QMessageBox.about(self," ","Order Added Successfully!" )
            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")

        def clear_order(self):
            self.phar_code_input.clear()
            self.phar_amnt_input.clear()
            self.phar_id_input.clear()
            db=sqlite3.connect('database/bmd303.db')
            cur=db.cursor()
            query="select order_no from Order_mdcn order by order_no desc limit 1"
            cur.execute(query)
            rec=cur.fetchone()
            self.phar_no_input.setText(str(rec[0]+1))

        def ViewAllOrders(self):
            connection=sqlite3.connect('database/bmd303.db')
            self.orders_table.setColumnCount(4)
            self.orders_table.setHorizontalHeaderLabels(["Order No","ID","Number of Items","Total"])
            query="select order_no,order_id,count(*),sum(tot) from Order_mdcn group by order_no, order_id"
            res=connection.execute(query)
            self.orders_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.orders_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.orders_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()
        
        def ViewInOrders(self):
            self.orders_table.setColumnCount(4)
            self.orders_table.setHorizontalHeaderLabels(["Order No","ID","Number of Items","Total"])
            connection=sqlite3.connect('database/bmd303.db')
            query="select order_no,order_id,count(*),sum(tot) from Order_mdcn where not order_id='Non-registered' group by order_no;"
            res=connection.execute(query)
            self.orders_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.orders_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.orders_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        def ViewOutOrders(self):
            connection=sqlite3.connect('database/bmd303.db')
            self.orders_table.setColumnCount(3)
            self.orders_table.setHorizontalHeaderLabels(["Order No","Number of Items","Total"])
            query="select order_no,count(*),sum(tot) from Order_mdcn where order_id='Non-registered' group by order_no;"
            res=connection.execute(query)
            self.orders_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.orders_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.orders_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        def DeleteOrders(self):
            try:

                orderno=QtWidgets.QInputDialog.getText(self,"Order Delete","Enter Order Number")
                if orderno[1]==False:
                    return
                db = sqlite3.connect('./database/bmd303.db')
                cur = db.cursor()
                res=cur.execute('DELETE from Order_mdcn WHERE order_no=?', (orderno[0],))
                db.commit()
                cur.close()
                db.close()
                if res.rowcount ==0 and orderno[1]==True:
                    QMessageBox.about(self," ","Order is Not Found")

                elif res.rowcount > 0:
                    QMessageBox.about(self," ","Order is deleted successfully!!!")
               
                    
            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")

        def search_order(self):
            try:

                order=QtWidgets.QInputDialog.getText(self,"Order Search","Enter Order Number")
                # print(d_id)
                db = sqlite3.connect('./database/bmd303.db')
                res=db.execute('select order_no,order_id,count(*),sum(tot) from Order_mdcn where order_no= "%s" group by order_no,order_id;' % (order[0]))
                if order[1]==False:
                    db.close()
                    return

                elif res.fetchone() is None:
                   QMessageBox.about(self," ","Order not found!!!!")
                   db.close()
                else:
                    db = sqlite3.connect('./database/bmd303.db')
                    res=db.execute('select order_no,order_id,count(*),sum(tot) from Order_mdcn where order_no= "%s" group by order_no,order_id;' % (order[0]))
                    self.orders_table.setHorizontalHeaderLabels(["Order No","ID","Number of Items","Total"])
                    self.orders_table.setRowCount(0)
                    for row_num, row_data in enumerate(res):
                        self.orders_table.insertRow(row_num)
                        for col_num, data in enumerate(row_data):
                            self.orders_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

                    db.close()
                    

            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")







class Radiology(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Radiology,self).__init__()

        def add_rad(self,img):
            try:
                ii=cv2.imread(img)
                cv2.imwrite("rad_img.png",ii)
                im=open('rad_img.png',"rb").read()
                db2=sqlite3.connect('database/bmd303.db')
                cur2=db2.cursor()
                p_id=self.rad_pat_id.text()
                query2='select pat_id from Patient where pat_id= "%s" '%(p_id)
                cur2.execute(query2)
                pt_id=cur2.fetchone()
                cur2.close()
                db2.close()
                connection=sqlite3.connect('database/bmd303.db')
                cur = connection.cursor()
                date=datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                q = "INSERT INTO Radiology(image_id,patient_id,med_image,image_type,img_date,report,conclusion) VALUES(?,?,?,?,?,?,?)"
                i=(None,pt_id[0],sqlite3.Binary(im),self.rad_type.currentText(),date,self.rad_report.toPlainText(),self.rad_conc.toPlainText())
                cur.execute(q,i)
                connection.commit()
                QMessageBox.about(self," ","Record Added Successfully!" +"\nRad_No: "+str(cur.lastrowid))
                cur.close()
                connection.close()
                self.rad_pat_id.clear()
                self.rad_type.setCurrentIndex(0)
                self.rad_report.clear()
                self.rad_conc.clear()
                self.view2.photoViewer.clear()
                self.view2.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)
            except Exception:
                QMessageBox.about(self," ","Invalid!!!" )
                self.rad_pat_id.clear()
                self.rad_type.setCurrentIndex(0)
                self.rad_report.clear()
                self.rad_conc.clear()
                self.view2.photoViewer.clear()
                self.view2.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)


        def search_rad(self):
            try:
                pat_id=self.search_rad_bar.text()
                img_num=self.search_radno_bar.text()
                db = sqlite3.connect('./database/bmd303.db')
                cur = db.cursor()
                cur.execute('SELECT pat_name,pat_age,pat_email,pat_national,pat_gender,pat_address,med_image,report,conclusion,image_type,img_date from Patient,Radiology WHERE patient_id=pat_id and pat_id= "%s" and image_id="%s" ' % (pat_id,img_num))
                rec=cur.fetchone()
                cur.close()
                db.close()
                if rec is not None:
                   name=rec[0]
                   age=rec[1]
                   em_ph=rec[2]
                   nation=rec[3]
                   gen=rec[4]
                   add=rec[5]
                   pic=rec[6]
                   report=rec[7]
                   conc=rec[8]
                   img_type=rec[9]
                   img_dat=rec[10]
                   pix=QtGui.QPixmap()
                   pix.loadFromData(pic,"png")
                   self.rad_photo_search.setPixmap(pix.scaled(300,300,QtCore.Qt.KeepAspectRatio))
                   self.pat_name_rad.setText("Name: "+name)
                   self.pat_phone_rad.setText("Email/Phone: "+str(em_ph))
                   self.pat_address_rad.setText("Address: "+add)
                   self.pat_age_rad.setText("Age: "+str(age))
                   self.pat_national_rar.setText("National ID: "+str(nation))
                   self.pat_gender_rad.setText("Gender: "+gen)
                   more="Date:\n"+img_dat+"\n\nImage Type:\n"+img_type+"\n\nReport:\n"+report+"\n\nConclusion:\n"+conc
                   res=ScrollMessageBox(more,None)
                   res.exec_()

                else:
                    QMessageBox.about(self," ","Record not found!!!!")
                    self.search_rad_bar.clear()
                    self.search_radno_bar.clear()
                    self.pat_name_rad.setText("Name: None")
                    self.pat_phone_rad.setText("Email/Phone: None")
                    self.pat_address_rad.setText("Address: None")
                    self.pat_age_rad.setText("Age: None")
                    self.pat_national_rar.setText("National ID: None")
                    self.pat_gender_rad.setText("Gender: None")
                    self.rad_photo_search.setText(" ")

            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")

        def clr_rad_search(self):
             self.search_rad_bar.clear()
             self.search_radno_bar.clear()
             self.pat_name_rad.setText("Name: None")
             self.pat_phone_rad.setText("Email/Phone: None")
             self.pat_address_rad.setText("Address: None")
             self.pat_age_rad.setText("Age: None")
             self.pat_national_rar.setText("National ID: None")
             self.pat_gender_rad.setText("Gender: None")
             self.rad_photo_search.setText(" ")


        


     

                    

