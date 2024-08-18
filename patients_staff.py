from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit
from PySide6 import QtWidgets,QtCore, QtGui
from PySide6.QtWidgets import QMessageBox,QDialog,QPushButton,QLineEdit
from main import Ui_HIS,get_image,set_image
import interface_actions as ac
import sqlite3
from datetime import datetime
import cv2

class Patients(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Patients,self).__init__()

        def view_pateints_data(self):
            connection=sqlite3.connect('database/bmd303.db')
            self.patients_table.setHorizontalHeaderLabels(["ID","Name","Address","Age","Gender","E-mail/Phone","National ID","Chronic Disease","Reg Date","Reg Time"])
            query="SELECT pat_id,pat_name,pat_address,pat_age,pat_gender,pat_email,pat_national,chronic_disease,pat_Date,pat_time FROM Patient"
            res=connection.execute(query)
            self.patients_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.patients_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.patients_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        def InsertPatientInfo(self,image):
            # print(get_image())
            try:
                if image is None:
                    im=open("./images/user_un.png","rb").read()
                else:
                    ii=cv2.imread(image)
                    cv2.imwrite("pat_img.png",ii)
                    im=open('pat_img.png',"rb").read()
                connection=sqlite3.connect('database/bmd303.db')
                cur = connection.cursor()
                date=datetime.today().strftime('%Y-%m-%d')
                time=datetime.today().strftime('%H:%M:%S')
                q = "INSERT INTO Patient(pat_id,pat_name,pat_email,pat_gender,pat_Date,pat_time,pat_address,chronic_disease,pat_birth_y,pat_birth_m,pat_birth_d,pat_image,pat_national) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
                i=(None,self.p_Name.text(),self.p_email.text(),self.p_gender.currentText(),date,time,self.p_address.text(),self.p_chronic.currentText(),self.p_year.currentText(),self.p_month.currentText(),self.p_day.currentText(),sqlite3.Binary(im),int(self.p_N_ID.text()),)
                cur.execute(q,i)
                connection.commit()
                QMessageBox.about(self," ","Record Added Successfully!"+"\nPatient_ID: "+str(cur.lastrowid) )
                cur.close()
                connection.close()
                self.p_address.clear()
                self.p_gender.setCurrentIndex(0)
                self.p_N_ID.clear()
                self.p_Name.clear()
                self.p_email.clear()
                self.p_chronic.setCurrentIndex(0)
                self.p_year.setCurrentIndex(0)
                self.p_month.setCurrentIndex(0)
                self.p_day.setCurrentIndex(0)
                self.view.photoViewer.clear()
                self.view.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)
            except Exception:
                QMessageBox.about(self," ","Repeated or Empty Data" )
                self.p_address.clear()
                self.p_gender.setCurrentIndex(0)
                self.p_N_ID.clear()
                self.p_Name.clear()
                self.p_email.clear()
                self.p_chronic.setCurrentIndex(0)
                self.p_year.setCurrentIndex(0)
                self.p_month.setCurrentIndex(0)
                self.p_day.setCurrentIndex(0)
                self.view.photoViewer.clear()
                self.view.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)
                


                
           

        def DeletePatientInfo(self):
            connection=sqlite3.connect('database/bmd303.db')
            connection.execute("PRAGMA foreign_keys=1")
            query="SELECT * FROM Patient"
            cur = connection.cursor()
            res=cur.execute(query)
            for row in enumerate(res):
                if row[0]==self.patients_table.currentRow():
                    data=row[1]
                    p_ID=data[0]
                    cur.execute("DELETE FROM Patient WHERE pat_id=?",(p_ID,))
                    connection.commit()
            cur.close()
            connection.close()

        def ModifyPatientInfo(self):
            try:
                connection=sqlite3.connect('database/bmd303.db')
                connection.execute("PRAGMA foreign_keys=1")
                query="SELECT pat_id,pat_name,pat_address,pat_age,pat_gender,pat_email,pat_national,chronic_disease FROM Patient"
                cur = connection.cursor()
                res=cur.execute(query)
                for row in enumerate(res):
                    if row[0]==self.patients_table.currentRow():
                        data=row[1]
                        #print(data)
                        p_ID=data[0]
                        p_name=data[1]
                        p_add=data[2]
                        p_gen=data[4]
                        p_em=data[5]
                        p_ntn=data[6]
                        p_chrnc=data[7]
                        old_pg=p_gen
                        p_name=self.patients_table.item(row[0],1).text()
                        p_add=self.patients_table.item(row[0],2).text()
                        p_gen=self.patients_table.item(row[0],4).text()
                        p_em=self.patients_table.item(row[0],5).text()
                        p_ntn=self.patients_table.item(row[0],6).text()
                        p_chrnc=self.patients_table.item(row[0],7).text()
                        if p_gen == "m":
                            p_gen="Male"
                        elif p_gen == "f":
                            p_gen="Female"
                        else:
                            p_gen=old_pg

                        s="UPDATE Patient SET pat_name=?,pat_address=?,pat_gender=?,pat_email=?,pat_national=?,chronic_disease=? WHERE Pat_id=?"
                        cur.execute(s,(p_name,p_add,p_gen,p_em,p_ntn,p_chrnc,p_ID))
                        connection.commit()
                cur.close()
                connection.close()
            except Exception:
                print("error in data types take care")


        def search_pat(self):
            try:
                pat_id=self.search_bar.text()
                db = sqlite3.connect('./database/bmd303.db')
                cur = db.cursor()
                cur.execute('SELECT * from Patient WHERE pat_id= "%s" ' % (pat_id))
                rec=cur.fetchone()
                cur.close()
                db.close()
                if rec is not None:
                   name=rec[1]
                   add=rec[6]
                   age=rec[13]
                   em_ph=rec[2]
                   nation=rec[12]
                   gen=rec[3]
                   pic=rec[11]
                   pix=QtGui.QPixmap()
                   pix.loadFromData(pic,"png")
                   self.pat_photo_s.setPixmap(pix.scaled(200,200,QtCore.Qt.KeepAspectRatio))
                   self.pat_name_s.setText("Name: "+name)
                   self.pat_phone_s.setText("Email/Phone: "+str(em_ph))
                   self.pat_address_s.setText("Address: "+add)
                   self.pat_age_s.setText("Age: "+str(age))
                   self.pat_national_s.setText("National ID: "+str(nation))
                   self.pat_gender_s.setText("Gender: "+gen)

                else:
                    QMessageBox.about(self," ","Record not found!!!!")
                    self.search_bar.clear()
                    self.pat_name_s.setText("Name: None")
                    self.pat_phone_s.setText("Email/Phone: None")
                    self.pat_address_s.setText("Address: None")
                    self.pat_age_s.setText("Age: None")
                    self.pat_national_s.setText("National ID: None")
                    self.pat_gender_s.setText("Gender: None")
                    self.pat_photo_s.setText(" ")

            except Exception:
                QMessageBox.about(self," ","Invalid!!!!")


        def clear_srch_pat(self):
            self.search_bar.clear()
            self.pat_name_s.setText("Name: None")
            self.pat_phone_s.setText("Email/Phone: None")
            self.pat_address_s.setText("Address: None")
            self.pat_age_s.setText("Age: None")
            self.pat_national_s.setText("National ID: None")
            self.pat_gender_s.setText("Gender: None")
            self.pat_photo_s.setText(" ")


class Staff(QtWidgets.QMainWindow,Ui_HIS):
        def __init__(self):
                super(Staff,self).__init__()
        
        def view_staff(self):
            connection=sqlite3.connect('database/bmd303.db')
            self.staff_table.setHorizontalHeaderLabels(["ID","Name","Address","Role","E-mail","Gender","Working Hours","Department","Salary","Password","Age"])
            query="SELECT st_id,st_name,st_address,st_role,st_email,st_gender,st_workh,st_department,st_salary,st_pass,st_age FROM Staff"
            res=connection.execute(query)
            self.staff_table.setRowCount(0)
    
            for row_num, row_data in enumerate(res):
                self.staff_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.staff_table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))

            connection.close()

        def delete_staff(self):
            connection=sqlite3.connect('database/bmd303.db')
            query="SELECT * FROM Staff"
            cur = connection.cursor()
            res=cur.execute(query)
            for row in enumerate(res):
                if row[0]==self.staff_table.currentRow():
                    data=row[1]
                    p_ID=data[0]
                    cur.execute("DELETE FROM Staff WHERE st_id=?",(p_ID,))
                    connection.commit()
            cur.close()
            connection.close()

        def update_staff(self):
            try:
                connection=sqlite3.connect('database/bmd303.db')
                query="SELECT st_id,st_name,st_address,st_role,st_email,st_gender,st_workh,st_department,st_salary,st_pass FROM Staff"
                cur = connection.cursor()
                res=cur.execute(query)
                for row in enumerate(res):
                    if row[0]==self.staff_table.currentRow():
                        data=row[1]
                        #print(data)
                        s_ID=data[0]
                        s_name=data[1]
                        s_add=data[2]
                        s_role=data[3]
                        s_em=data[4]
                        s_gen=data[5]
                        s_w=data[6]
                        s_dep=data[7]
                        s_sal=data[8]
                        s_pass=data[9]
                        old_pg=s_gen

                        s_name=self.staff_table.item(row[0],1).text()
                        s_add=self.staff_table.item(row[0],2).text()
                        s_role=self.staff_table.item(row[0],3).text()
                        s_em=self.staff_table.item(row[0],4).text()
                        s_gen=self.staff_table.item(row[0],5).text()
                        s_w=self.staff_table.item(row[0],6).text()
                        s_dep=self.staff_table.item(row[0],7).text()
                        s_sal=self.staff_table.item(row[0],8).text()
                        s_pass=self.staff_table.item(row[0],9).text()
                        if s_gen == "m":
                            s_gen="Male"
                        elif s_gen == "f":
                            s_gen="Female"
                        else:
                            s_gen=old_pg

                            
                        s="UPDATE Staff SET st_name=?,st_address=?,st_role=?,st_email=?,st_gender=?,st_workh=?,st_department=?,st_salary=?,st_pass=? WHERE st_id=?"
                        cur.execute(s,(s_name,s_add,s_role,s_em,s_gen,s_w,s_dep,s_sal,s_pass,s_ID))
                        connection.commit()
                cur.close()
                connection.close()
            except Exception:
                QMessageBox.about(self," ","Invalid, Try Again!!!!")

        
        def add_staff(self,image):
            # print(get_image())
            try:
                if image is None:
                    im=open("./images/user_un.png","rb").read()
                else:
                    ii=cv2.imread(image)
                    cv2.imwrite("st_img.png",ii)
                    im=open('st_img.png',"rb").read()
                connection=sqlite3.connect('database/bmd303.db')
                cur = connection.cursor()
                q = "INSERT INTO Staff(st_id,st_name,st_image,st_pass,st_address,st_role,st_email,st_gender,st_workh,st_salary,st_birth_y,st_birth_m,st_birth_d,st_department) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                i=(None,self.st_name.text(),sqlite3.Binary(im),self.st_pass.text(),self.st_address.text(),self.st_role.currentText(),self.st_email.text(),self.st_gender.currentText(),self.st_work.currentText(),self.st_salary.text(),self.st_year.currentText(),self.st_month.currentText(),self.st_day.currentText(),self.st_dep.currentText(),)
                cur.execute(q,i)
                connection.commit()
                cur.close()
                connection.close()
                QMessageBox.about(self," ","Record Added Successfully!" )
                self.st_address.clear()
                self.st_role.setCurrentIndex(0)
                self.st_work.setCurrentIndex(0)
                self.st_pass.clear()
                self.st_salary.clear()
                self.st_name.clear()
                self.st_email.clear()
                self.st_dep.setCurrentIndex(0)
                self.st_gender.setCurrentIndex(0)
                self.st_year.setCurrentIndex(0)
                self.st_month.setCurrentIndex(0)
                self.st_day.setCurrentIndex(0)
                self.view3.photoViewer.clear()
                self.view3.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)
                self.main_pages_vwr.setCurrentIndex(4)
            except Exception:
                QMessageBox.about(self," ","Repeated or Empty Data" )
                self.st_address.clear()
                self.st_role.setCurrentIndex(0)
                self.st_work.setCurrentIndex(0)
                self.st_pass.clear()
                self.st_salary.clear()
                self.st_name.clear()
                self.st_email.clear()
                self.st_dep.setCurrentIndex(0)
                self.st_gender.setCurrentIndex(0)
                self.st_year.setCurrentIndex(0)
                self.st_month.setCurrentIndex(0)
                self.st_day.setCurrentIndex(0)
                self.view3.photoViewer.clear()
                self.view3.photoViewer.setText('\n\n Drop Image Here \n\n')
                set_image(None)

        def cancel_add_staff(self):
            self.st_address.clear()
            self.st_role.setCurrentIndex(0)
            self.st_work.setCurrentIndex(0)
            self.st_pass.clear()
            self.st_salary.clear()
            self.st_name.clear()
            self.st_email.clear()
            self.st_dep.setCurrentIndex(0)
            self.st_gender.setCurrentIndex(0)
            self.st_year.setCurrentIndex(0)
            self.st_month.setCurrentIndex(0)
            self.st_day.setCurrentIndex(0)
            self.view3.photoViewer.clear()
            self.view3.photoViewer.setText('\n\n Drop Image Here \n\n')
            set_image(None)
               
            

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

     

                    

