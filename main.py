from RoundProgressBar import roundProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtWidgets,QtCore, QtGui
from PySide6.QtGui import QStandardItemModel,QFont, QImage, QPixmap
from PyQt5.QtGui import QStandardItemModel,QFont, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PySide6.QtCore import Qt
import sqlite3



p_image=None

def get_image():
        return p_image
def set_image(num):
        global p_image
        p_image=num
        return p_image
class image_lbl(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumHeight(150)
        self.setMinimumWidth(150)
        self.setAcceptDrops(True)
        self.setText('\n\n Drop Image Here \n\n')
        self.setFont(QtGui.QFont('Arial',15))
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #fff;
                color: rgb(255, 255, 255);
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setMinimumWidth(250)
        self.setMaximumHeight(250)
        self.setAcceptDrops(True)
        mainLayout = QVBoxLayout()
        self.photoViewer = image_lbl()
        mainLayout.addWidget(self.photoViewer)
        mainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(mainLayout)
        

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QtGui.QPixmap(file_path).scaled(250,250,Qt.KeepAspectRatio))

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            global p_image
            p_image = event.mimeData().urls()[0].toLocalFile()
            self.set_image(p_image)
            event.accept()
            
        else:
            event.ignore()

    def clear_image(self):
        global p_image
        p_image=None
        self.view.photoViewer.clear()
        self.view.photoViewer.setText('\n\n Drop Image Here \n\n')

    def clear_st_image(self):
        global p_image
        p_image=None
        self.view3.photoViewer.clear()
        self.view3.photoViewer.setText('\n\n Drop Image Here \n\n')

    def clear_rad_image(self):
        global p_image
        p_image=None
        self.view2.photoViewer.clear()
        self.view2.photoViewer.setText('\n\n Drop Image Here \n\n')




class Ui_HIS(object):
    def setupUi(self, HIS):
        HIS.setObjectName("HIS")
        HIS.resize(820, 550)
        HIS.setMinimumSize(QtCore.QSize(820, 550))
        HIS.setMaximumSize(QtCore.QSize(820, 550))
        HIS.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main = QtWidgets.QWidget(HIS)
        self.main.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.main.setObjectName("main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.main)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(4, 4, 4);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tog_frm = QtWidgets.QFrame(self.top_bar)
        self.tog_frm.setMinimumSize(QtCore.QSize(70, 0))
        self.tog_frm.setMaximumSize(QtCore.QSize(90, 16777215))
        self.tog_frm.setStyleSheet("QPushButton::hover{\n"
"\n"
"    background-color: rgb(145, 143, 143);\n"
"\n"
"}")
        self.tog_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tog_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tog_frm.setObjectName("tog_frm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tog_frm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tgl_btn = QtWidgets.QPushButton(self.tog_frm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tgl_btn.sizePolicy().hasHeightForWidth())
        self.tgl_btn.setSizePolicy(sizePolicy)
        self.tgl_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.tgl_btn.setMaximumSize(QtCore.QSize(90, 90))
        self.tgl_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(224, 255, 238);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.tgl_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/men.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tgl_btn.setIcon(icon)
        self.tgl_btn.setIconSize(QtCore.QSize(24, 24))
        self.tgl_btn.setFlat(True)
        self.tgl_btn.setObjectName("tgl_btn")
        self.verticalLayout_2.addWidget(self.tgl_btn)
        self.horizontalLayout.addWidget(self.tog_frm)
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.cntrl_frm = QtWidgets.QFrame(self.top_bar)
        self.cntrl_frm.setMinimumSize(QtCore.QSize(110, 40))
        self.cntrl_frm.setMaximumSize(QtCore.QSize(90, 50))
        self.cntrl_frm.setStyleSheet("")
        self.cntrl_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cntrl_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cntrl_frm.setObjectName("cntrl_frm")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.cntrl_frm)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimize_btn = QtWidgets.QPushButton(self.cntrl_frm)
        self.minimize_btn.setMinimumSize(QtCore.QSize(0, 26))
        self.minimize_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(224, 255, 238);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.minimize_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/minus_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QtCore.QSize(15, 15))
        self.minimize_btn.setFlat(True)
        self.minimize_btn.setObjectName("minimize_btn")
        self.horizontalLayout_3.addWidget(self.minimize_btn)
        self.cls_btn = QtWidgets.QPushButton(self.cntrl_frm)
        self.cls_btn.setMinimumSize(QtCore.QSize(0, 26))
        self.cls_btn.setStyleSheet("\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.cls_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/white_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cls_btn.setIcon(icon2)
        self.cls_btn.setIconSize(QtCore.QSize(24, 30))
        self.cls_btn.setFlat(True)
        self.cls_btn.setObjectName("cls_btn")
        self.horizontalLayout_3.addWidget(self.cls_btn)
        self.horizontalLayout.addWidget(self.cntrl_frm)
        self.verticalLayout.addWidget(self.top_bar)
        self.cont_1 = QtWidgets.QFrame(self.main)
        self.cont_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cont_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cont_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_1.setObjectName("cont_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cont_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nav_drw = QtWidgets.QFrame(self.cont_1)
        self.nav_drw.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_drw.sizePolicy().hasHeightForWidth())
        self.nav_drw.setSizePolicy(sizePolicy)
        self.nav_drw.setMinimumSize(QtCore.QSize(70, 70))
        self.nav_drw.setMaximumSize(QtCore.QSize(210, 510))
        self.nav_drw.setStyleSheet("background-color: rgb(4, 4, 4);")
        self.nav_drw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nav_drw.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nav_drw.setObjectName("nav_drw")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.nav_drw)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nav_mnu = QtWidgets.QFrame(self.nav_drw)
        self.nav_mnu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nav_mnu.setStyleSheet("QFrame{background-color: rgb(4, 4, 4);}\n"
"\n"
"QPushButton{\n"
"padding: 10px 10px;\n"
"background-color: rgb(4, 4, 4);\n"
"color:#ffffff;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font-weight: bold;\n"
"font-size:12px;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(224, 255, 238);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.nav_mnu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nav_mnu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nav_mnu.setObjectName("nav_mnu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.nav_mnu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.home = QtWidgets.QPushButton(self.nav_mnu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setMinimumSize(QtCore.QSize(70, 0))
        self.home.setMaximumSize(QtCore.QSize(210, 16777215))
        self.home.setStyleSheet("padding-left:70px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home.setIcon(icon3)
        self.home.setIconSize(QtCore.QSize(25, 25))
        self.home.setFlat(True)
        self.home.setObjectName("home")
        self.verticalLayout_4.addWidget(self.home)
        self.admission = QtWidgets.QPushButton(self.nav_mnu)
        self.admission.setStyleSheet("padding-left:100px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/addm1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.admission.setIcon(icon4)
        self.admission.setIconSize(QtCore.QSize(25, 25))
        self.admission.setFlat(True)
        self.admission.setObjectName("admission")
        self.verticalLayout_4.addWidget(self.admission)
        self.pharmacy = QtWidgets.QPushButton(self.nav_mnu)
        self.pharmacy.setStyleSheet("padding-left:100px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/pharma.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pharmacy.setIcon(icon5)
        self.pharmacy.setIconSize(QtCore.QSize(25, 25))
        self.pharmacy.setFlat(True)
        self.pharmacy.setObjectName("pharmacy")
        self.verticalLayout_4.addWidget(self.pharmacy)
        self.radiology = QtWidgets.QPushButton(self.nav_mnu)
        self.radiology.setStyleSheet("padding-left:100px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./images/forbidden.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.radiology.setIcon(icon6)
        self.radiology.setIconSize(QtCore.QSize(25, 25))
        self.radiology.setFlat(True)
        self.radiology.setObjectName("radiology")
        self.verticalLayout_4.addWidget(self.radiology)
        self.staff = QtWidgets.QPushButton(self.nav_mnu)
        self.staff.setStyleSheet("padding-left:70px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./images/doctor1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.staff.setIcon(icon7)
        self.staff.setIconSize(QtCore.QSize(25, 25))
        self.staff.setFlat(True)
        self.staff.setObjectName("staff")
        self.verticalLayout_4.addWidget(self.staff)
        self.verticalLayout_3.addWidget(self.nav_mnu)
        self.horizontalLayout_2.addWidget(self.nav_drw)
        self.pages_frm = QtWidgets.QFrame(self.cont_1)
        self.pages_frm.setMinimumSize(QtCore.QSize(800, 0))
        self.pages_frm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pages_frm.setStyleSheet("QFrame{background-color: rgb(4, 4, 4);}\n"
"\n"
"")
        self.pages_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pages_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages_frm.setObjectName("pages_frm")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pages_frm)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.main_pages_vwr = QtWidgets.QStackedWidget(self.pages_frm)
        self.main_pages_vwr.setMaximumSize(QtCore.QSize(740, 480))
        self.main_pages_vwr.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_pages_vwr.setObjectName("main_pages_vwr")
        self.Home_pg = QtWidgets.QWidget()
        self.Home_pg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.Home_pg.setObjectName("Home_pg")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Home_pg)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.home_options = QtWidgets.QTabWidget(self.Home_pg)
        self.home_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.home_options.setFont(font)
        self.home_options.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"  \n"
"QTabBar::tab \n"
"{\n"
"      background: rgb(4, 4, 4);\n"
"    color: white; \n"
"height:40px;\n"
"width:370px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 1 #C1D8E8, stop: 1 #F0F5F8); \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.home_options.setIconSize(QtCore.QSize(20, 20))
        self.home_options.setObjectName("home_options")
        self.stats_tab = QtWidgets.QWidget()
        self.stats_tab.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.443, y1:0.863, x2:0.443, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.926136 rgba(255, 255, 255, 255));")
        self.stats_tab.setObjectName("stats_tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.stats_tab)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 150)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.view_diagrams = QtWidgets.QFrame(self.stats_tab)
        self.view_diagrams.setMinimumSize(QtCore.QSize(0, 370))
        self.view_diagrams.setMaximumSize(QtCore.QSize(16777215, 400))
        self.view_diagrams.setStyleSheet("background: none;")
        self.view_diagrams.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.view_diagrams.setFrameShadow(QtWidgets.QFrame.Raised)
        self.view_diagrams.setObjectName("view_diagrams")
        self.gridLayout = QtWidgets.QGridLayout(self.view_diagrams)
        self.gridLayout.setObjectName("gridLayout")
        self.di1_lbl_1 = QtWidgets.QLabel(self.view_diagrams)
        self.di1_lbl_1.setMinimumSize(QtCore.QSize(0, 30))
        self.di1_lbl_1.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.di1_lbl_1.setFont(font)
        self.di1_lbl_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.di1_lbl_1.setAlignment(QtCore.Qt.AlignCenter)
        self.di1_lbl_1.setObjectName("di1_lbl_1")
        self.gridLayout.addWidget(self.di1_lbl_1, 0, 0, 1, 1)
        self.di1_lbl_2 = QtWidgets.QLabel(self.view_diagrams)
        self.di1_lbl_2.setMinimumSize(QtCore.QSize(0, 30))
        self.di1_lbl_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.di1_lbl_2.setFont(font)
        self.di1_lbl_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.di1_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.di1_lbl_2.setObjectName("di1_lbl_2")
        self.gridLayout.addWidget(self.di1_lbl_2, 0, 1, 1, 1)
        self.di1_lbl_3 = QtWidgets.QLabel(self.view_diagrams)
        self.di1_lbl_3.setMinimumSize(QtCore.QSize(0, 30))
        self.di1_lbl_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.di1_lbl_3.setFont(font)
        self.di1_lbl_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.di1_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.di1_lbl_3.setObjectName("di1_lbl_3")
        self.gridLayout.addWidget(self.di1_lbl_3, 0, 2, 1, 1)
        self.diagram_1 = QtWidgets.QFrame(self.view_diagrams)
        self.diagram_1.setMinimumSize(QtCore.QSize(200, 200))
        self.diagram_1.setMaximumSize(QtCore.QSize(150, 200))
        self.diagram_1.setStyleSheet("QFrame{border:3px solid;\n"
"border-color: transparent;\n"
"border-radius:100;}")
        self.diagram_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagram_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagram_1.setObjectName("diagram_1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.diagram_1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pro1_d = roundProgressBar(self.diagram_1)
        self.pro1_d.setObjectName("pro1_d")
        self.horizontalLayout_6.addWidget(self.pro1_d)
        self.gridLayout.addWidget(self.diagram_1, 1, 0, 1, 1)
        self.diagram_2 = QtWidgets.QFrame(self.view_diagrams)
        self.diagram_2.setMinimumSize(QtCore.QSize(200, 200))
        self.diagram_2.setMaximumSize(QtCore.QSize(150, 200))
        self.diagram_2.setStyleSheet("QFrame{border:3px solid;\n"
"border-color: transparent;\n"
"border-radius:100;}")
        self.diagram_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagram_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagram_2.setObjectName("diagram_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.diagram_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pro2_d = roundProgressBar(self.diagram_2)
        self.pro2_d.setObjectName("pro2_d")
        self.horizontalLayout_7.addWidget(self.pro2_d)
        self.gridLayout.addWidget(self.diagram_2, 1, 1, 1, 1)
        self.diagram_3 = QtWidgets.QFrame(self.view_diagrams)
        self.diagram_3.setMinimumSize(QtCore.QSize(200, 200))
        self.diagram_3.setMaximumSize(QtCore.QSize(150, 200))
        self.diagram_3.setStyleSheet("QFrame{\n"
"border:3px solid;\n"
"border-color: transparent;\n"
"border-radius:100;}")
        self.diagram_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagram_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagram_3.setObjectName("diagram_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.diagram_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pro3_d = roundProgressBar(self.diagram_3)
        self.pro3_d.setObjectName("pro3_d")
        self.horizontalLayout_8.addWidget(self.pro3_d)
        self.gridLayout.addWidget(self.diagram_3, 1, 2, 1, 1)
        self.horizontalLayout_5.addWidget(self.view_diagrams)
        self.home_options.addTab(self.stats_tab, "")
        self.profile_tab = QtWidgets.QWidget()
        self.profile_tab.setObjectName("profile_tab")
        self.inbox_btn = QtWidgets.QPushButton(self.profile_tab)
        self.inbox_btn.setGeometry(QtCore.QRect(590, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.inbox_btn.setFont(font)
        self.inbox_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 188, 138);\n"
"color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.inbox_btn.setObjectName("inbox_btn")
        self.msg_frame = QtWidgets.QFrame(self.profile_tab)
        self.msg_frame.setGeometry(QtCore.QRect(520, 60, 211, 370))
        self.msg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msg_frame.setObjectName("msg_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.msg_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.msgs_list = QtWidgets.QListWidget(self.msg_frame)
        self.msgs_list.setMaximumSize(QtCore.QSize(16777215, 0))
        self.msgs_list.setObjectName("msgs_list")
        self.msgs_list.setSpacing(6)
        self.msgs_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.msgs_list.setStyleSheet("QListWidget{border-style:none;font-size:9pt; font-weight:bold;}"
        "QListWidget::item{border-style:solid; border-width:2px; border-radius:7px;border-color:black; }"
        "QListWidget::item:selected{background-color:rgb(0, 188, 138); color:white;}"
        )
        self.verticalLayout_8.addWidget(self.msgs_list)
        self.inbox_btn_2 = QtWidgets.QPushButton(self.profile_tab)
        self.inbox_btn_2.setGeometry(QtCore.QRect(520, 10, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.inbox_btn_2.setFont(font)
        self.inbox_btn_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 188, 138);\n"
"color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.inbox_btn_2.setObjectName("inbox_btn_2")
        self.layoutWidget = QtWidgets.QWidget(self.profile_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 70, 232, 306))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.user_photo = QtWidgets.QLabel(self.layoutWidget)
        self.user_photo.setMinimumSize(QtCore.QSize(230, 230))
        self.user_photo.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:115px;\n"
"")
        self.user_photo.setText("")
        self.user_photo.setObjectName("user_photo")
        self.verticalLayout_9.addWidget(self.user_photo)
        self.user_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_name.setFont(font)
        self.user_name.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name.setObjectName("user_name")
        self.verticalLayout_9.addWidget(self.user_name)
        self.user_email = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_email.setFont(font)
        self.user_email.setAlignment(QtCore.Qt.AlignCenter)
        self.user_email.setObjectName("user_email")
        self.verticalLayout_9.addWidget(self.user_email)
        self.user_role = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_role.setFont(font)
        self.user_role.setAlignment(QtCore.Qt.AlignCenter)
        self.user_role.setObjectName("user_role")
        self.verticalLayout_9.addWidget(self.user_role)
        self.home_options.addTab(self.profile_tab, "")
        self.verticalLayout_6.addWidget(self.home_options)
        self.main_pages_vwr.addWidget(self.Home_pg)
        self.admission_pg = QtWidgets.QWidget()
        self.admission_pg.setStyleSheet("background-color: rgb(4, 4, 4);")
        self.admission_pg.setObjectName("admission_pg")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.admission_pg)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.admission_tab = QtWidgets.QTabWidget(self.admission_pg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.admission_tab.setFont(font)
        self.admission_tab.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"  \n"
"QTabBar::tab \n"
"{\n"
"      background: rgb(4, 4, 4);\n"
"    color: white; \n"
"height:40px;\n"
"width:246.4px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: black;\n"
"    border-color: #40494E;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.admission_tab.setIconSize(QtCore.QSize(24, 24))
        self.admission_tab.setObjectName("admission_tab")
        self.add_p_tab = QtWidgets.QWidget()
        self.add_p_tab.setObjectName("add_p_tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.add_p_tab)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_p_scrollArea = QtWidgets.QScrollArea(self.add_p_tab)
        self.add_p_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_p_scrollArea.setStyleSheet("background-color:black;\n"
"border:none;")
        self.add_p_scrollArea.setWidgetResizable(False)
        self.add_p_scrollArea.setObjectName("add_p_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 420))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.p_adding_info_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.p_adding_info_btn.setGeometry(QtCore.QRect(660, 360, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_adding_info_btn.setFont(font)
        self.p_adding_info_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.p_adding_info_btn.setObjectName("p_adding_info_btn")
        self.p_name_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_name_lbl.setGeometry(QtCore.QRect(300, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_name_lbl.setFont(font)
        self.p_name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_name_lbl.setObjectName("p_name_lbl")
        self.p_n_ID_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_n_ID_lbl.setGeometry(QtCore.QRect(300, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_n_ID_lbl.setFont(font)
        self.p_n_ID_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_n_ID_lbl.setObjectName("p_n_ID_lbl")
        self.p_add_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_add_lbl.setGeometry(QtCore.QRect(300, 110, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_add_lbl.setFont(font)
        self.p_add_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_add_lbl.setObjectName("p_add_lbl")
        self.p_gender_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_gender_lbl.setGeometry(QtCore.QRect(300, 175, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_gender_lbl.setFont(font)
        self.p_gender_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_gender_lbl.setObjectName("p_gender_lbl")
        self.p_chronic_lbl_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_chronic_lbl_2.setGeometry(QtCore.QRect(300, 205, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_chronic_lbl_2.setFont(font)
        self.p_chronic_lbl_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_chronic_lbl_2.setObjectName("p_chronic_lbl_2")
        self.p_month_lbl_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_month_lbl_4.setGeometry(QtCore.QRect(300, 288, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_month_lbl_4.setFont(font)
        self.p_month_lbl_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_month_lbl_4.setObjectName("p_month_lbl_4")
        self.p_day_lbl_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_day_lbl_5.setGeometry(QtCore.QRect(300, 318, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_day_lbl_5.setFont(font)
        self.p_day_lbl_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_day_lbl_5.setObjectName("p_day_lbl_5")
        self.p_year_lbl_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_year_lbl_6.setGeometry(QtCore.QRect(300, 255, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_year_lbl_6.setFont(font)
        self.p_year_lbl_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_year_lbl_6.setObjectName("p_year_lbl_6")
        self.p_photo = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.p_photo.setGeometry(QtCore.QRect(10, 40, 250, 250))
        self.gridLay = QtWidgets.QGridLayout(self.p_photo)
        self.gridLay.setContentsMargins(0, 0, 0, 0)
        self.gridLay.setObjectName("gridLay")
        self.view = AppDemo()
        self.gridLay.addWidget(self.view, 0, 0, 0, 0)
        self.p_email_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.p_email_lbl.setGeometry(QtCore.QRect(300, 145, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_email_lbl.setFont(font)
        self.p_email_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_email_lbl.setObjectName("p_email_lbl")
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setGeometry(QtCore.QRect(420, 20, 281, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.p_Name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.p_Name.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_Name.setFont(font)
        self.p_Name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.p_Name.setText("")
        self.p_Name.setObjectName("p_Name")
        self.verticalLayout_11.addWidget(self.p_Name)
        self.p_N_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.p_N_ID.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_N_ID.setFont(font)
        self.p_N_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.p_N_ID.setObjectName("p_N_ID")
        self.verticalLayout_11.addWidget(self.p_N_ID)
        self.p_address = QtWidgets.QLineEdit(self.layoutWidget1)
        self.p_address.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_address.setFont(font)
        self.p_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.p_address.setObjectName("p_address")
        self.verticalLayout_11.addWidget(self.p_address)
        self.p_email = QtWidgets.QLineEdit(self.layoutWidget1)
        self.p_email.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_email.setFont(font)
        self.p_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.p_email.setObjectName("p_email")
        self.verticalLayout_11.addWidget(self.p_email)
        self.p_gender = QtWidgets.QComboBox(self.layoutWidget1)
        self.p_gender.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_gender.setFont(font)
        self.p_gender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.p_gender.setEditable(False)
        self.p_gender.setObjectName("p_gender")
        self.p_gender.addItem("")
        self.p_gender.addItem("")
        self.verticalLayout_11.addWidget(self.p_gender)
        self.p_chronic = QtWidgets.QComboBox(self.layoutWidget1)
        self.p_chronic.setMinimumSize(QtCore.QSize(211, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_chronic.setFont(font)
        self.p_chronic.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.p_chronic.setEditable(False)
        self.p_chronic.setObjectName("p_chronic")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.p_chronic.addItem("")
        self.verticalLayout_11.addWidget(self.p_chronic)
        self.p_brith_lbl_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.p_brith_lbl_3.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_brith_lbl_3.setFont(font)
        self.p_brith_lbl_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.p_brith_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.p_brith_lbl_3.setObjectName("p_brith_lbl_3")
        self.verticalLayout_11.addWidget(self.p_brith_lbl_3)
        self.p_year = QtWidgets.QComboBox(self.layoutWidget1)
        self.p_year.setMinimumSize(QtCore.QSize(211, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_year.setFont(font)    
        self.p_year.addItems([str(x) for x in range(1920,2020)])
        self.p_year.setEditable(True)
        self.p_year.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"") 
        self.p_year.setObjectName("p_year")
        self.verticalLayout_11.addWidget(self.p_year)
        self.p_month = QtWidgets.QComboBox(self.layoutWidget1)
        self.p_month.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_month.setFont(font)
        self.p_month.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.p_month.setEditable(False)
        self.p_month.setObjectName("p_month")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.p_month.addItem("")
        self.verticalLayout_11.addWidget(self.p_month)
        self.p_day = QtWidgets.QComboBox(self.layoutWidget1)
        self.p_day.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_day.setFont(font)
        self.p_day.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.p_day.setEditable(False)
        self.p_day.setObjectName("p_day")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.p_day.addItem("")
        self.verticalLayout_11.addWidget(self.p_day)
        self.p_clr_image_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.p_clr_image_btn.setGeometry(QtCore.QRect(40, 300, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.p_clr_image_btn.setFont(font)
        self.p_clr_image_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.p_clr_image_btn.setObjectName("p_clr_image_btn")
        self.add_p_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.add_p_scrollArea)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./images/add_patient_info-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.admission_tab.addTab(self.add_p_tab, icon8, "")
        self.view_p_tab = QtWidgets.QWidget()
        self.view_p_tab.setObjectName("view_p_tab")
        self.patients_table = QtWidgets.QTableWidget(self.view_p_tab)
        self.patients_table.setGeometry(QtCore.QRect(90, 20, 551, 361))
        self.patients_table.setStyleSheet("border:none;\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.patients_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.patients_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.patients_table.setRowCount(200)
        self.patients_table.setColumnCount(10)
        self.patients_table.setObjectName("patients_table")
        self.show_p_btn = QtWidgets.QPushButton(self.view_p_tab)
        self.show_p_btn.setGeometry(QtCore.QRect(310, 390, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.show_p_btn.setFont(font)
        self.show_p_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(224, 255, 238);\n"
"    border-style:inset;\n"
"\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./images/view_p.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.show_p_btn.setIcon(icon9)
        self.show_p_btn.setIconSize(QtCore.QSize(20, 20))
        self.show_p_btn.setFlat(True)
        self.show_p_btn.setObjectName("show_p_btn")
        self.delete_p_btn = QtWidgets.QPushButton(self.view_p_tab)
        self.delete_p_btn.setGeometry(QtCore.QRect(160, 390, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.delete_p_btn.setFont(font)
        self.delete_p_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./images/sign-delete-p.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.delete_p_btn.setIcon(icon10)
        self.delete_p_btn.setIconSize(QtCore.QSize(20, 18))
        self.delete_p_btn.setFlat(True)
        self.delete_p_btn.setObjectName("delete_p_btn")
        self.update_p_btn = QtWidgets.QPushButton(self.view_p_tab)
        self.update_p_btn.setGeometry(QtCore.QRect(460, 390, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.update_p_btn.setFont(font)
        self.update_p_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"    background-color: rgb(0, 216, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./images/update-p.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.update_p_btn.setIcon(icon11)
        self.update_p_btn.setIconSize(QtCore.QSize(20, 17))
        self.update_p_btn.setFlat(True)
        self.update_p_btn.setObjectName("update_p_btn")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./images/k.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.admission_tab.addTab(self.view_p_tab, icon12, "")
        self.search_p_tab = QtWidgets.QWidget()
        self.search_p_tab.setObjectName("search_p_tab")
        self.search_bar = QtWidgets.QLineEdit(self.search_p_tab)
        self.search_bar.setGeometry(QtCore.QRect(160, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.search_bar.setFont(font)
        self.search_bar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.search_bar.setText("")
        self.search_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.search_bar.setObjectName("search_bar")
        self.pat_search_btn = QtWidgets.QPushButton(self.search_p_tab)
        self.pat_search_btn.setGeometry(QtCore.QRect(540, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_search_btn.setFont(font)
        self.pat_search_btn.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./images/search_p2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pat_search_btn.setIcon(icon13)
        self.pat_search_btn.setObjectName("pat_search_btn")
        self.dwnld_pdata_btn = QtWidgets.QPushButton(self.search_p_tab)
        self.dwnld_pdata_btn.setGeometry(QtCore.QRect(660, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.dwnld_pdata_btn.setFont(font)
        self.dwnld_pdata_btn.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.dwnld_pdata_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./images/dwnld.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dwnld_pdata_btn.setIcon(icon14)
        self.dwnld_pdata_btn.setIconSize(QtCore.QSize(45, 45))
        self.dwnld_pdata_btn.setObjectName("dwnld_pdata_btn")
        self.pat_photo_s = QtWidgets.QLabel(self.search_p_tab)
        self.pat_photo_s.setGeometry(QtCore.QRect(60, 110, 210, 210))
        self.pat_photo_s.setStyleSheet("color: rgb(4, 4, 4);\n"
"background-color: rgb(4, 4, 4);\n"
"border-style:outset;\n"
"border-radius:100px;")
        self.pat_photo_s.setText("")
        self.pat_photo_s.setAlignment(QtCore.Qt.AlignCenter)
        self.pat_photo_s.setObjectName("pat_photo_s")
        self.search_data = QtWidgets.QFrame(self.search_p_tab)
        self.search_data.setGeometry(QtCore.QRect(310, 90, 421, 281))
        self.search_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_data.setObjectName("search_data")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.search_data)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pat_name_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_name_s.setFont(font)
        self.pat_name_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_name_s.setObjectName("pat_name_s")
        self.verticalLayout_10.addWidget(self.pat_name_s)
        self.pat_age_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_age_s.setFont(font)
        self.pat_age_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_age_s.setObjectName("pat_age_s")
        self.verticalLayout_10.addWidget(self.pat_age_s)
        self.pat_phone_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_phone_s.setFont(font)
        self.pat_phone_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_phone_s.setObjectName("pat_phone_s")
        self.verticalLayout_10.addWidget(self.pat_phone_s)
        self.pat_national_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_national_s.setFont(font)
        self.pat_national_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_national_s.setObjectName("pat_national_s")
        self.verticalLayout_10.addWidget(self.pat_national_s)
        self.pat_gender_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_gender_s.setFont(font)
        self.pat_gender_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_gender_s.setObjectName("pat_gender_s")
        self.verticalLayout_10.addWidget(self.pat_gender_s)
        self.pat_address_s = QtWidgets.QLabel(self.search_data)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_address_s.setFont(font)
        self.pat_address_s.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_address_s.setObjectName("pat_address_s")
        self.verticalLayout_10.addWidget(self.pat_address_s)
        self.pat_cancel_search_btn_2 = QtWidgets.QPushButton(self.search_p_tab)
        self.pat_cancel_search_btn_2.setGeometry(QtCore.QRect(640, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_cancel_search_btn_2.setFont(font)
        self.pat_cancel_search_btn_2.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.pat_cancel_search_btn_2.setObjectName("pat_cancel_search_btn_2")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.admission_tab.addTab(self.search_p_tab, icon15, "")
        self.verticalLayout_7.addWidget(self.admission_tab)
        self.main_pages_vwr.addWidget(self.admission_pg)
        self.pharma_pg = QtWidgets.QWidget()
        self.pharma_pg.setObjectName("pharma_pg")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.pharma_pg)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.pharma_tab = QtWidgets.QTabWidget(self.pharma_pg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pharma_tab.setFont(font)
        self.pharma_tab.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"  \n"
"QTabBar::tab \n"
"{\n"
"      background: rgb(4, 4, 4);\n"
"    color: white; \n"
"height:40px;\n"
"width:246.4px;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: black;\n"
"    border-color: #40494E;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pharma_tab.setIconSize(QtCore.QSize(27, 27))
        self.pharma_tab.setObjectName("pharma_tab")
        self.orders_tab = QtWidgets.QWidget()
        self.orders_tab.setObjectName("orders_tab")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.orders_tab)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.orders_scrollArea = QtWidgets.QScrollArea(self.orders_tab)
        self.orders_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.orders_scrollArea.setStyleSheet("background-color:black;\n"
"border:none;")
        self.orders_scrollArea.setWidgetResizable(False)
        self.orders_scrollArea.setObjectName("orders_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 720, 420))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.mdcn_no_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.mdcn_no_lbl.setGeometry(QtCore.QRect(70, 125, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.mdcn_no_lbl.setFont(font)
        self.mdcn_no_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.mdcn_no_lbl.setObjectName("mdcn_no_lbl")
        self.mdcn_id_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.mdcn_id_lbl.setGeometry(QtCore.QRect(70, 165, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.mdcn_id_lbl.setFont(font)
        self.mdcn_id_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.mdcn_id_lbl.setObjectName("mdcn_id_lbl")
        self.mdcn_code_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.mdcn_code_lbl.setGeometry(QtCore.QRect(70, 205, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.mdcn_code_lbl.setFont(font)
        self.mdcn_code_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.mdcn_code_lbl.setObjectName("mdcn_code_lbl")
        self.mdcn_amount_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.mdcn_amount_lbl.setGeometry(QtCore.QRect(70, 245, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.mdcn_amount_lbl.setFont(font)
        self.mdcn_amount_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.mdcn_amount_lbl.setObjectName("mdcn_amount_lbl")
        self.layoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(200, 110, 281, 171))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.phar_no_input = QtWidgets.QLabel(self.layoutWidget_3)
        self.phar_no_input.setMaximumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.phar_no_input.setFont(font)
        self.phar_no_input.setStyleSheet("background-color: black; color:white;\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.phar_no_input.setText("")
        self.phar_no_input.setObjectName("phar_no_input")
        self.verticalLayout_18.addWidget(self.phar_no_input)
        self.phar_id_input = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.phar_id_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.phar_id_input.setFont(font)
        self.phar_id_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.phar_id_input.setObjectName("phar_id_input")
        self.verticalLayout_18.addWidget(self.phar_id_input)
        self.phar_code_input = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.phar_code_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.phar_code_input.setFont(font)
        self.phar_code_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.phar_code_input.setObjectName("phar_code_input")
        self.verticalLayout_18.addWidget(self.phar_code_input)
        self.phar_amnt_input = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.phar_amnt_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.phar_amnt_input.setFont(font)
        self.phar_amnt_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.phar_amnt_input.setObjectName("phar_amnt_input")
        self.verticalLayout_18.addWidget(self.phar_amnt_input)
        self.submit_phar_order = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.submit_phar_order.setGeometry(QtCore.QRect(250, 300, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.submit_phar_order.setFont(font)
        self.submit_phar_order.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.submit_phar_order.setObjectName("submit_phar_order")
        
        self.clr_phar_order = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.clr_phar_order.setGeometry(QtCore.QRect(250, 350, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.clr_phar_order.setFont(font)
        self.clr_phar_order.setText("Finish")
        self.clr_phar_order.setStyleSheet("QPushButton{\n"
"background-color:#32CD32;\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: #32CD32;\n"
" border-style:inset;\n"
"\n"
"}")
        self.clr_phar_order.setObjectName("clr_phar_order")




        self.orders_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_10.addWidget(self.orders_scrollArea)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./images/medicine_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pharma_tab.addTab(self.orders_tab, icon16, "")
        self.view_orders_tab = QtWidgets.QWidget()
        self.view_orders_tab.setObjectName("view_orders_tab")
        self.phar_opt_frame = QtWidgets.QFrame(self.view_orders_tab)
        self.phar_opt_frame.setGeometry(QtCore.QRect(500, 60, 211, 370))
        self.phar_opt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phar_opt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phar_opt_frame.setObjectName("phar_opt_frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.phar_opt_frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.opt_drw = QtWidgets.QFrame(self.phar_opt_frame)
        self.opt_drw.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_drw.sizePolicy().hasHeightForWidth())
        self.opt_drw.setSizePolicy(sizePolicy)
        self.opt_drw.setMinimumSize(QtCore.QSize(0, 0))
        self.opt_drw.setMaximumSize(QtCore.QSize(16777215, 0))
        self.opt_drw.setStyleSheet("background-color: rgb(4, 4, 4);")
        self.opt_drw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.opt_drw.setFrameShadow(QtWidgets.QFrame.Raised)
        self.opt_drw.setObjectName("opt_drw")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.opt_drw)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.opt_mnu = QtWidgets.QFrame(self.opt_drw)
        self.opt_mnu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.opt_mnu.setStyleSheet("QFrame{background-color: rgb(4, 4, 4);}\n"
"\n"
"QPushButton{\n"
"padding: 10px 10px;\n"
"background-color: white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font-weight: bold;\n"
"font-size:12px;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(0, 170, 255);\n"
"    border-style:inset;\n"
"color:white;\n"
"\n"
"}")
        self.opt_mnu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.opt_mnu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.opt_mnu.setObjectName("opt_mnu")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.opt_mnu)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.outpatient = QtWidgets.QPushButton(self.opt_mnu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outpatient.sizePolicy().hasHeightForWidth())
        self.outpatient.setSizePolicy(sizePolicy)
        self.outpatient.setMinimumSize(QtCore.QSize(70, 0))
        self.outpatient.setMaximumSize(QtCore.QSize(210, 16777215))
        self.outpatient.setStyleSheet("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("./images/patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.outpatient.setIcon(icon17)
        self.outpatient.setIconSize(QtCore.QSize(25, 25))
        self.outpatient.setFlat(True)
        self.outpatient.setObjectName("outpatient")
        self.verticalLayout_22.addWidget(self.outpatient)
        self.inpatient = QtWidgets.QPushButton(self.opt_mnu)
        self.inpatient.setStyleSheet("")
        self.inpatient.setIcon(icon17)
        self.inpatient.setIconSize(QtCore.QSize(25, 25))
        self.inpatient.setFlat(True)
        self.inpatient.setObjectName("inpatient")
        self.verticalLayout_22.addWidget(self.inpatient)
        self.delete_order = QtWidgets.QPushButton(self.opt_mnu)
        self.delete_order.setStyleSheet("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("./images/minus_PNG25.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.delete_order.setIcon(icon18)
        self.delete_order.setIconSize(QtCore.QSize(20, 20))
        self.delete_order.setFlat(True)
        self.delete_order.setObjectName("delete_order")
        self.verticalLayout_22.addWidget(self.delete_order)
        self.search_order = QtWidgets.QPushButton(self.opt_mnu)
        self.search_order.setStyleSheet("")
        self.search_order.setIcon(icon15)
        self.search_order.setIconSize(QtCore.QSize(23, 25))
        self.search_order.setFlat(True)
        self.search_order.setObjectName("search_order")
        self.verticalLayout_22.addWidget(self.search_order)
        self.load_orders = QtWidgets.QPushButton(self.opt_mnu)
        self.load_orders.setStyleSheet("")
        self.load_orders.setIcon(icon9)
        self.load_orders.setIconSize(QtCore.QSize(22, 25))
        self.load_orders.setFlat(True)
        self.load_orders.setObjectName("load_orders")
        self.verticalLayout_22.addWidget(self.load_orders)
        self.verticalLayout_21.addWidget(self.opt_mnu)
        self.verticalLayout_19.addWidget(self.opt_drw)
        self.phar_options = QtWidgets.QPushButton(self.view_orders_tab)
        self.phar_options.setGeometry(QtCore.QRect(495, 3, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.phar_options.setFont(font)
        self.phar_options.setStyleSheet("QPushButton{\n"
"color:black;\n"
"    background-color: white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(0, 170, 255);\n"
"color: white;\n"
"    border-style:inset;\n"
"\n"
"}")
        self.phar_options.setObjectName("phar_options")
        self.orders_table = QtWidgets.QTableWidget(self.view_orders_tab)
        self.orders_table.setGeometry(QtCore.QRect(10, 30, 451, 361))
        self.orders_table.setStyleSheet("border:none;\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.orders_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.orders_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.orders_table.setRowCount(200)
        self.orders_table.setColumnCount(4)
        self.orders_table.setObjectName("orders_table")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("./images/pharma2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap("./images/pharma2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pharma_tab.addTab(self.view_orders_tab, icon19, "")
        self.drug_list_tab = QtWidgets.QWidget()
        self.drug_list_tab.setObjectName("drug_list_tab")
        self.drug_table = QtWidgets.QTableWidget(self.drug_list_tab)
        self.drug_table.setGeometry(QtCore.QRect(90, 20, 550, 360))
        self.drug_table.setStyleSheet("border:none;\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.drug_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.drug_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.drug_table.setRowCount(200)
        self.drug_table.setColumnCount(5)
        self.drug_table.setObjectName("drug_table")
        self.layoutWidget_4 = QtWidgets.QWidget(self.drug_list_tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(90, 390, 551, 32))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.delete_drug_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        self.delete_drug_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.delete_drug_btn.setFont(font)
        self.delete_drug_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color:white;\n"
"    border-style:inset;\n"
"\n"
"}")
        self.delete_drug_btn.setIcon(icon10)
        self.delete_drug_btn.setIconSize(QtCore.QSize(20, 18))
        self.delete_drug_btn.setFlat(True)
        self.delete_drug_btn.setObjectName("delete_drug_btn")
        self.horizontalLayout_11.addWidget(self.delete_drug_btn)
        self.show_drug_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        self.show_drug_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.show_drug_btn.setFont(font)
        self.show_drug_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(0, 144, 216);\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 170, 255);\n"
"    border-style:inset;\n"
"color:white;\n"
"\n"
"}")
        self.show_drug_btn.setIcon(icon9)
        self.show_drug_btn.setIconSize(QtCore.QSize(20, 20))
        self.show_drug_btn.setFlat(True)
        self.show_drug_btn.setObjectName("show_drug_btn")
        self.horizontalLayout_11.addWidget(self.show_drug_btn)
        self.update_drug_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        self.update_drug_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.update_drug_btn.setFont(font)
        self.update_drug_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 0);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    color:white;\n"
"    background-color: rgb(0, 216, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.update_drug_btn.setIcon(icon11)
        self.update_drug_btn.setIconSize(QtCore.QSize(20, 17))
        self.update_drug_btn.setFlat(True)
        self.update_drug_btn.setObjectName("update_drug_btn")
        self.horizontalLayout_11.addWidget(self.update_drug_btn)
        self.search_drug_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        self.search_drug_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.search_drug_btn.setFont(font)
        self.search_drug_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"color:white;\n"
"\n"
"}")
        self.search_drug_btn.setIcon(icon13)
        self.search_drug_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_drug_btn.setFlat(True)
        self.search_drug_btn.setObjectName("search_drug_btn")
        self.horizontalLayout_11.addWidget(self.search_drug_btn)
        self.add_drug_btn = QtWidgets.QPushButton(self.layoutWidget_4)
        self.add_drug_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.add_drug_btn.setFont(font)
        self.add_drug_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(255, 255, 255);\n"
"color: rgb(59, 0, 0);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(93, 0, 0);\n"
"color:white;\n"
"    border-style:inset;\n"
"\n"
"}")
        self.add_drug_btn.setIcon(icon16)
        self.add_drug_btn.setIconSize(QtCore.QSize(22, 25))
        self.add_drug_btn.setFlat(True)
        self.add_drug_btn.setObjectName("add_drug_btn")
        self.horizontalLayout_11.addWidget(self.add_drug_btn)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("./images/drug_l.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pharma_tab.addTab(self.drug_list_tab, icon20, "")
        self.verticalLayout_20.addWidget(self.pharma_tab)
        self.main_pages_vwr.addWidget(self.pharma_pg)
        self.rad_pg = QtWidgets.QWidget()
        self.rad_pg.setObjectName("rad_pg")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.rad_pg)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.rad_options = QtWidgets.QTabWidget(self.rad_pg)
        self.rad_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_options.setFont(font)
        self.rad_options.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"  \n"
"QTabBar::tab \n"
"{\n"
"      background: rgb(4, 4, 4);\n"
"    color: white; \n"
"height:40px;\n"
"width:370px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 1 #C1D8E8, stop: 1 #F0F5F8); \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.rad_options.setIconSize(QtCore.QSize(20, 20))
        self.rad_options.setObjectName("rad_options")
        self.rad_add_tab = QtWidgets.QWidget()
        self.rad_add_tab.setStyleSheet("background-color:rgb(4, 4, 4);")
        self.rad_add_tab.setObjectName("rad_add_tab")
        self.rad_photo_in = QtWidgets.QWidget(self.rad_add_tab)
        self.rad_photo_in.setGeometry(QtCore.QRect(10, 60, 300, 300))
        self.rad_photo_in.setObjectName("rad_photo_in")
        self.gridLay2 = QtWidgets.QGridLayout(self.rad_photo_in)
        self.gridLay2.setContentsMargins(0, 0, 0, 0)
        self.view2= AppDemo()
        self.gridLay2.addWidget(self.view2, 0, 0, 0, 0)
        self.rad_adding_btn = QtWidgets.QPushButton(self.rad_add_tab)
        self.rad_adding_btn.setGeometry(QtCore.QRect(670, 380, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_adding_btn.setFont(font)
        self.rad_adding_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.rad_adding_btn.setObjectName("rad_adding_btn")
        self.rad_clr_image_btn = QtWidgets.QPushButton(self.rad_add_tab)
        self.rad_clr_image_btn.setGeometry(QtCore.QRect(60, 370, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_clr_image_btn.setFont(font)
        self.rad_clr_image_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.rad_clr_image_btn.setObjectName("rad_clr_image_btn")
        self.widget = QtWidgets.QWidget(self.rad_add_tab)
        self.widget.setGeometry(QtCore.QRect(360, 10, 291, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.rad_pat_lbl = QtWidgets.QLabel(self.widget)
        self.rad_pat_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_pat_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_pat_lbl.setFont(font)
        self.rad_pat_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_pat_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_pat_lbl.setObjectName("rad_pat_lbl")
        self.verticalLayout_14.addWidget(self.rad_pat_lbl)
        self.rad_pat_id = QtWidgets.QLineEdit(self.widget)
        self.rad_pat_id.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_pat_id.setFont(font)
        self.rad_pat_id.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.rad_pat_id.setText("")
        self.rad_pat_id.setObjectName("rad_pat_id")
        self.verticalLayout_14.addWidget(self.rad_pat_id)
        self.rad_type_lbl = QtWidgets.QLabel(self.widget)
        self.rad_type_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_type_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_type_lbl.setFont(font)
        self.rad_type_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_type_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_type_lbl.setObjectName("rad_type_lbl")
        self.verticalLayout_14.addWidget(self.rad_type_lbl)
        self.rad_type = QtWidgets.QComboBox(self.widget)
        self.rad_type.setMinimumSize(QtCore.QSize(0, 25))
        self.rad_type.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_type.setFont(font)
        self.rad_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.rad_type.setEditable(False)
        self.rad_type.setObjectName("rad_type")
        rad_types=["Bitewing X-Ray","Periapical X-Ray","Occlusal X-Ray","Dental CT","MRI","Panoramic X-Ray","Other"]
        self.rad_type.addItems(rad_types)
        self.verticalLayout_14.addWidget(self.rad_type)
        self.rad_rep_lbl = QtWidgets.QLabel(self.widget)
        self.rad_rep_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_rep_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_rep_lbl.setFont(font)
        self.rad_rep_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_rep_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_rep_lbl.setObjectName("rad_rep_lbl")
        self.verticalLayout_14.addWidget(self.rad_rep_lbl)
        self.rad_report = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.rad_report.setFont(font)
        self.rad_report.setStyleSheet("border:none;\n"
"background-color:white;\n"
"border-radius:10px;")
        self.rad_report.setObjectName("rad_report")
        self.verticalLayout_14.addWidget(self.rad_report)
        self.rad_conc_lbl = QtWidgets.QLabel(self.widget)
        self.rad_conc_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_conc_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_conc_lbl.setFont(font)
        self.rad_conc_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_conc_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_conc_lbl.setObjectName("rad_conc_lbl")
        self.verticalLayout_14.addWidget(self.rad_conc_lbl)
        self.rad_conc = QtWidgets.QTextEdit(self.widget)
        self.rad_conc.setStyleSheet("border:none;\n"
"background-color:white;\n"
"border-radius:10px;")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.rad_conc.setFont(font)
        self.rad_conc.setObjectName("rad_conc")
        self.verticalLayout_14.addWidget(self.rad_conc)
        self.rad_options.addTab(self.rad_add_tab, "")
        self.rad_search_tab = QtWidgets.QWidget()
        self.rad_search_tab.setObjectName("rad_search_tab")
        self.rad_search_btn = QtWidgets.QPushButton(self.rad_search_tab)
        self.rad_search_btn.setGeometry(QtCore.QRect(540, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_search_btn.setFont(font)
        self.rad_search_btn.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.rad_search_btn.setIcon(icon13)
        self.rad_search_btn.setObjectName("rad_search_btn")
        self.search_rad_bar = QtWidgets.QLineEdit(self.rad_search_tab)
        self.search_rad_bar.setGeometry(QtCore.QRect(160, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.search_rad_bar.setFont(font)
        self.search_rad_bar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.search_rad_bar.setText("")
        self.search_rad_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.search_rad_bar.setObjectName("search_rad_bar")
        self.rad_photo_search = QtWidgets.QLabel(self.rad_search_tab)
        self.rad_photo_search.setGeometry(QtCore.QRect(20, 100, 300, 300))
        self.rad_photo_search.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:black;\n"
"border-style:outset;\n"
"")
        self.rad_photo_search.setText("")
        self.rad_photo_search.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_photo_search.setObjectName("rad_photo_search")
        self.search_radno_bar = QtWidgets.QLineEdit(self.rad_search_tab)
        self.search_radno_bar.setGeometry(QtCore.QRect(160, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.search_radno_bar.setFont(font)
        self.search_radno_bar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.search_radno_bar.setText("")
        self.search_radno_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.search_radno_bar.setObjectName("search_radno_bar")
        self.dwnld_raddata_btn = QtWidgets.QPushButton(self.rad_search_tab)
        self.dwnld_raddata_btn.setGeometry(QtCore.QRect(660, 390, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.dwnld_raddata_btn.setFont(font)
        self.dwnld_raddata_btn.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.dwnld_raddata_btn.setText("")
        self.dwnld_raddata_btn.setIcon(icon14)
        self.dwnld_raddata_btn.setIconSize(QtCore.QSize(45, 45))
        self.dwnld_raddata_btn.setObjectName("dwnld_raddata_btn")
        self.rad_patsrch_lbl = QtWidgets.QLabel(self.rad_search_tab)
        self.rad_patsrch_lbl.setGeometry(QtCore.QRect(15, 25, 121, 20))
        self.rad_patsrch_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_patsrch_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_patsrch_lbl.setFont(font)
        self.rad_patsrch_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_patsrch_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_patsrch_lbl.setObjectName("rad_patsrch_lbl")
        self.rad_no_lbl = QtWidgets.QLabel(self.rad_search_tab)
        self.rad_no_lbl.setGeometry(QtCore.QRect(30, 65, 121, 20))
        self.rad_no_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.rad_no_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_no_lbl.setFont(font)
        self.rad_no_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad_no_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rad_no_lbl.setObjectName("rad_no_lbl")
        self.search_data_2 = QtWidgets.QFrame(self.rad_search_tab)
        self.search_data_2.setGeometry(QtCore.QRect(360, 130, 341, 241))
        self.search_data_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_data_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_data_2.setObjectName("search_data_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.search_data_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pat_name_rad = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_name_rad.setFont(font)
        self.pat_name_rad.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_name_rad.setObjectName("pat_name_rad")
        self.verticalLayout_15.addWidget(self.pat_name_rad)
        self.pat_age_rad = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_age_rad.setFont(font)
        self.pat_age_rad.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_age_rad.setObjectName("pat_age_rad")
        self.verticalLayout_15.addWidget(self.pat_age_rad)
        self.pat_phone_rad = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_phone_rad.setFont(font)
        self.pat_phone_rad.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_phone_rad.setObjectName("pat_phone_rad")
        self.verticalLayout_15.addWidget(self.pat_phone_rad)
        self.pat_national_rar = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_national_rar.setFont(font)
        self.pat_national_rar.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_national_rar.setObjectName("pat_national_rar")
        self.verticalLayout_15.addWidget(self.pat_national_rar)
        self.pat_gender_rad = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_gender_rad.setFont(font)
        self.pat_gender_rad.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_gender_rad.setObjectName("pat_gender_rad")
        self.verticalLayout_15.addWidget(self.pat_gender_rad)
        self.pat_address_rad = QtWidgets.QLabel(self.search_data_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.pat_address_rad.setFont(font)
        self.pat_address_rad.setStyleSheet("color: rgb(255, 255, 255);")
        self.pat_address_rad.setObjectName("pat_address_rad")
        self.verticalLayout_15.addWidget(self.pat_address_rad)
        self.rad_cancel_search_btn = QtWidgets.QPushButton(self.rad_search_tab)
        self.rad_cancel_search_btn.setGeometry(QtCore.QRect(630, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.rad_cancel_search_btn.setFont(font)
        self.rad_cancel_search_btn.setStyleSheet("QPushButton{border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 79, 238);\n"
" border-style:inset;\n"
"color:white;\n"
"}")
        self.rad_cancel_search_btn.setObjectName("rad_cancel_search_btn")
        self.rad_options.addTab(self.rad_search_tab, "")
        self.verticalLayout_12.addWidget(self.rad_options)
        self.main_pages_vwr.addWidget(self.rad_pg)
        self.staff_pg = QtWidgets.QWidget()
        self.staff_pg.setObjectName("staff_pg")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.staff_pg)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.staff_frm = QtWidgets.QFrame(self.staff_pg)
        self.staff_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staff_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.staff_frm.setObjectName("staff_frm")
        self.staff_table = QtWidgets.QTableWidget(self.staff_frm)
        self.staff_table.setGeometry(QtCore.QRect(100, 40, 551, 360))
        self.staff_table.setStyleSheet("border:none;\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.staff_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.staff_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.staff_table.setRowCount(200)
        self.staff_table.setColumnCount(10)
        self.staff_table.setObjectName("staff_table")
        self.layoutWidget_2 = QtWidgets.QWidget(self.staff_frm)
        self.layoutWidget_2.setGeometry(QtCore.QRect(100, 410, 551, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.delete_st_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.delete_st_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.delete_st_btn.setFont(font)
        self.delete_st_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color:white;\n"
"    border-style:inset;\n"
"\n"
"}")
        self.delete_st_btn.setIcon(icon10)
        self.delete_st_btn.setIconSize(QtCore.QSize(20, 18))
        self.delete_st_btn.setFlat(True)
        self.delete_st_btn.setObjectName("delete_st_btn")
        self.horizontalLayout_9.addWidget(self.delete_st_btn)
        self.show_st_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.show_st_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.show_st_btn.setFont(font)
        self.show_st_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(0, 144, 216);\n"
"    background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 170, 255);\n"
"    border-style:inset;\n"
"color:white;\n"
"\n"
"}")
        self.show_st_btn.setIcon(icon9)
        self.show_st_btn.setIconSize(QtCore.QSize(20, 20))
        self.show_st_btn.setFlat(True)
        self.show_st_btn.setObjectName("show_st_btn")
        self.horizontalLayout_9.addWidget(self.show_st_btn)
        self.update_st_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.update_st_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.update_st_btn.setFont(font)
        self.update_st_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 0);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    color:white;\n"
"    background-color: rgb(0, 216, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.update_st_btn.setIcon(icon11)
        self.update_st_btn.setIconSize(QtCore.QSize(20, 17))
        self.update_st_btn.setFlat(True)
        self.update_st_btn.setObjectName("update_st_btn")
        self.horizontalLayout_9.addWidget(self.update_st_btn)
        self.add_st_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.add_st_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.add_st_btn.setFont(font)
        self.add_st_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(255, 255, 255);\n"
"color: rgb(59, 0, 0);\n"
"\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(93, 0, 0);\n"
"color:white;\n"
"    border-style:inset;\n"
"\n"
"}")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("./images/doc_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_st_btn.setIcon(icon21)
        self.add_st_btn.setIconSize(QtCore.QSize(25, 25))
        self.add_st_btn.setFlat(True)
        self.add_st_btn.setObjectName("add_st_btn")
        self.horizontalLayout_9.addWidget(self.add_st_btn)
        self.verticalLayout_17.addWidget(self.staff_frm)
        self.main_pages_vwr.addWidget(self.staff_pg)
        self.login_pg = QtWidgets.QWidget()
        self.login_pg.setObjectName("login_pg")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.login_pg)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.log_options = QtWidgets.QTabWidget(self.login_pg)
        self.log_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.log_options.setFont(font)
        self.log_options.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"  \n"
"QTabBar::tab \n"
"{\n"
"      background: rgb(4, 4, 4);\n"
"    color: white; \n"
"height:40px;\n"
"width:370px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 1 #C1D8E8, stop: 1 #F0F5F8); \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.log_options.setIconSize(QtCore.QSize(20, 20))
        self.log_options.setObjectName("log_options")
        self.login_tab = QtWidgets.QWidget()
        self.login_tab.setStyleSheet("background-color:rgb(4, 4, 4);")
        self.login_tab.setObjectName("login_tab")
        self.hos_logo = QtWidgets.QLabel(self.login_tab)
        self.hos_logo.setGeometry(QtCore.QRect(280, 50, 151, 151))
        self.hos_logo.setText("")
        self.hos_logo.setPixmap(QtGui.QPixmap("./images/hos_logo.png"))
        self.hos_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.hos_logo.setObjectName("hos_logo")
        self.log_name = QtWidgets.QLineEdit(self.login_tab)
        self.log_name.setGeometry(QtCore.QRect(250, 220, 211, 31))
        self.log_name.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.log_name.setFont(font)
        self.log_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.log_name.setObjectName("log_name")
        self.log_pass = QtWidgets.QLineEdit(self.login_tab)
        self.log_pass.setGeometry(QtCore.QRect(250, 270, 211, 31))
        self.log_pass.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.log_pass.setFont(font)
        self.log_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.log_pass.setObjectName("log_pass")
        self.user_labl_nam = QtWidgets.QLabel(self.login_tab)
        self.user_labl_nam.setGeometry(QtCore.QRect(160, 225, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_labl_nam.setFont(font)
        self.user_labl_nam.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_labl_nam.setObjectName("user_labl_nam")
        self.user_labl_pass = QtWidgets.QLabel(self.login_tab)
        self.user_labl_pass.setGeometry(QtCore.QRect(160, 278, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_labl_pass.setFont(font)
        self.user_labl_pass.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_labl_pass.setObjectName("user_labl_pass")
        self.signin_btn = QtWidgets.QPushButton(self.login_tab)
        self.signin_btn.setGeometry(QtCore.QRect(250, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signin_btn.setFont(font)
        self.signin_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(0, 102, 150);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 102, 150);\n"
" border-style:inset;\n"
"\n"
"}")
        self.signin_btn.setObjectName("signin_btn")
        self.sign_clr_btn = QtWidgets.QPushButton(self.login_tab)
        self.sign_clr_btn.setGeometry(QtCore.QRect(370, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.sign_clr_btn.setFont(font)
        self.sign_clr_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.sign_clr_btn.setObjectName("sign_clr_btn")
        self.log_options.addTab(self.login_tab, "")
        self.signup_tab = QtWidgets.QWidget()
        self.signup_tab.setObjectName("signup_tab")
        self.usr_labl_up = QtWidgets.QLabel(self.signup_tab)
        self.usr_labl_up.setGeometry(QtCore.QRect(140, 95, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.usr_labl_up.setFont(font)
        self.usr_labl_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.usr_labl_up.setObjectName("usr_labl_up")
        self.signup_btn = QtWidgets.QPushButton(self.signup_tab)
        self.signup_btn.setGeometry(QtCore.QRect(240, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(0, 102, 150);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 102, 150);\n"
" border-style:inset;\n"
"\n"
"}")
        self.signup_btn.setObjectName("signup_btn")
        self.user_lbl_email_up = QtWidgets.QLabel(self.signup_tab)
        self.user_lbl_email_up.setGeometry(QtCore.QRect(140, 148, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_lbl_email_up.setFont(font)
        self.user_lbl_email_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_lbl_email_up.setObjectName("user_lbl_email_up")
        self.signup_pass = QtWidgets.QLineEdit(self.signup_tab)
        self.signup_pass.setGeometry(QtCore.QRect(240, 190, 211, 31))
        self.signup_pass.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_pass.setFont(font)
        self.signup_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.signup_pass.setObjectName("signup_pass")
        self.signup_email = QtWidgets.QLineEdit(self.signup_tab)
        self.signup_email.setGeometry(QtCore.QRect(240, 140, 211, 31))
        self.signup_email.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_email.setFont(font)
        self.signup_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.signup_email.setObjectName("signup_email")
        self.signup_clr_btn = QtWidgets.QPushButton(self.signup_tab)
        self.signup_clr_btn.setGeometry(QtCore.QRect(360, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_clr_btn.setFont(font)
        self.signup_clr_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.signup_clr_btn.setObjectName("signup_clr_btn")
        self.signup_conf = QtWidgets.QLineEdit(self.signup_tab)
        self.signup_conf.setGeometry(QtCore.QRect(240, 240, 211, 31))
        self.signup_conf.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_conf.setFont(font)
        self.signup_conf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.signup_conf.setObjectName("signup_conf")
        self.signup_role = QtWidgets.QLineEdit(self.signup_tab)
        self.signup_role.setGeometry(QtCore.QRect(240, 290, 211, 31))
        self.signup_role.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_role.setFont(font)
        self.signup_role.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.signup_role.setObjectName("signup_role")
        self.user_labl_pass_up = QtWidgets.QLabel(self.signup_tab)
        self.user_labl_pass_up.setGeometry(QtCore.QRect(140, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_labl_pass_up.setFont(font)
        self.user_labl_pass_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_labl_pass_up.setObjectName("user_labl_pass_up")
        self.user_labl_role_up = QtWidgets.QLabel(self.signup_tab)
        self.user_labl_role_up.setGeometry(QtCore.QRect(140, 298, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_labl_role_up.setFont(font)
        self.user_labl_role_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_labl_role_up.setObjectName("user_labl_role_up")
        self.signup_name = QtWidgets.QLineEdit(self.signup_tab)
        self.signup_name.setGeometry(QtCore.QRect(240, 90, 211, 31))
        self.signup_name.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.signup_name.setFont(font)
        self.signup_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.signup_name.setObjectName("signup_name")
        self.user_labl_conf_up = QtWidgets.QLabel(self.signup_tab)
        self.user_labl_conf_up.setGeometry(QtCore.QRect(140, 245, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.user_labl_conf_up.setFont(font)
        self.user_labl_conf_up.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_labl_conf_up.setObjectName("user_labl_conf_up")
        self.log_options.addTab(self.signup_tab, "")
        self.verticalLayout_13.addWidget(self.log_options)
        self.main_pages_vwr.addWidget(self.login_pg)
        self.sorry_pg = QtWidgets.QWidget()
        self.sorry_pg.setObjectName("sorry_pg")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.sorry_pg)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.sry_frm = QtWidgets.QFrame(self.sorry_pg)
        self.sry_frm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sry_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sry_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sry_frm.setObjectName("sry_frm")
        self.sry_lbl = QtWidgets.QLabel(self.sry_frm)
        self.sry_lbl.setGeometry(QtCore.QRect(110, 260, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.sry_lbl.setFont(font)
        self.sry_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.sry_lbl.setObjectName("sry_lbl")
        self.sry_sign = QtWidgets.QLabel(self.sry_frm)
        self.sry_sign.setGeometry(QtCore.QRect(270, 50, 201, 181))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.sry_sign.setFont(font)
        self.sry_sign.setText("")
        self.sry_sign.setPixmap(QtGui.QPixmap("./images/sorry.png"))
        self.sry_sign.setScaledContents(True)
        self.sry_sign.setAlignment(QtCore.Qt.AlignCenter)
        self.sry_sign.setObjectName("sry_sign")
        self.verticalLayout_16.addWidget(self.sry_frm)
        self.main_pages_vwr.addWidget(self.sorry_pg)
        self.add_drug_pg = QtWidgets.QWidget()
        self.add_drug_pg.setObjectName("add_drug_pg")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.add_drug_pg)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.add_drug_frame = QtWidgets.QFrame(self.add_drug_pg)
        self.add_drug_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_drug_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_drug_frame.setObjectName("add_drug_frame")
        self.drug_adding_btn = QtWidgets.QPushButton(self.add_drug_frame)
        self.drug_adding_btn.setGeometry(QtCore.QRect(390, 410, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_adding_btn.setFont(font)
        self.drug_adding_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.drug_adding_btn.setObjectName("drug_adding_btn")
        self.layoutWidget_5 = QtWidgets.QWidget(self.add_drug_frame)
        self.layoutWidget_5.setGeometry(QtCore.QRect(210, 10, 291, 391))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        
        self.drug_name_lbl = QtWidgets.QLabel(self.layoutWidget_5)
        self.drug_name_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.drug_name_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_name_lbl.setFont(font)
        self.drug_name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.drug_name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.drug_name_lbl.setObjectName("drug_name_lbl")
        self.verticalLayout_25.addWidget(self.drug_name_lbl)
        self.drug_name_input = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.drug_name_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_name_input.setFont(font)
        self.drug_name_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.drug_name_input.setText("")
        self.drug_name_input.setObjectName("drug_name_input")
        self.verticalLayout_25.addWidget(self.drug_name_input)
        self.drug_amount_lbl = QtWidgets.QLabel(self.layoutWidget_5)
        self.drug_amount_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.drug_amount_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_amount_lbl.setFont(font)
        self.drug_amount_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.drug_amount_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.drug_amount_lbl.setObjectName("drug_amount_lbl")
        self.verticalLayout_25.addWidget(self.drug_amount_lbl)
        self.drug_amount_input = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.drug_amount_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_amount_input.setFont(font)
        self.drug_amount_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.drug_amount_input.setText("")
        self.drug_amount_input.setObjectName("drug_amount_input")
        self.verticalLayout_25.addWidget(self.drug_amount_input)
        self.drug_price_lbl = QtWidgets.QLabel(self.layoutWidget_5)
        self.drug_price_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.drug_price_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_price_lbl.setFont(font)
        self.drug_price_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.drug_price_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.drug_price_lbl.setObjectName("drug_price_lbl")
        self.verticalLayout_25.addWidget(self.drug_price_lbl)
        self.drug_price_input = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.drug_price_input.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_price_input.setFont(font)
        self.drug_price_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.drug_price_input.setText("")
        self.drug_price_input.setObjectName("drug_price_input")
        self.verticalLayout_25.addWidget(self.drug_price_input)
        self.drug_desc_lbl = QtWidgets.QLabel(self.layoutWidget_5)
        self.drug_desc_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.drug_desc_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_desc_lbl.setFont(font)
        self.drug_desc_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.drug_desc_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.drug_desc_lbl.setObjectName("drug_desc_lbl")
        self.verticalLayout_25.addWidget(self.drug_desc_lbl)
        self.drug_desc_input = QtWidgets.QTextEdit(self.layoutWidget_5)
        self.drug_desc_input.setMinimumSize(QtCore.QSize(0, 100))
        self.drug_desc_input.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setLegacyWeight(75)
        self.drug_desc_input.setFont(font)
        self.drug_desc_input.setStyleSheet("border:none;\n"
"background-color:white;\n"
"border-radius:10px;")
        self.drug_desc_input.setObjectName("drug_desc_input")
        self.verticalLayout_25.addWidget(self.drug_desc_input)
        self.drug_clr_btn = QtWidgets.QPushButton(self.add_drug_frame)
        self.drug_clr_btn.setGeometry(QtCore.QRect(280, 410, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.drug_clr_btn.setFont(font)
        self.drug_clr_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.drug_clr_btn.setObjectName("drug_clr_btn")
        self.verticalLayout_23.addWidget(self.add_drug_frame)
        self.main_pages_vwr.addWidget(self.add_drug_pg)
        self.add_staff_pg = QtWidgets.QWidget()
        self.add_staff_pg.setObjectName("add_staff_pg")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.add_staff_pg)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.add_staff_frame = QtWidgets.QFrame(self.add_staff_pg)
        self.add_staff_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_staff_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_staff_frame.setObjectName("add_staff_frame")
        self.layoutWidget_6 = QtWidgets.QWidget(self.add_staff_frame)
        self.layoutWidget_6.setGeometry(QtCore.QRect(430, 20, 281, 400))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.st_name = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.st_name.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_name.setFont(font)
        self.st_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.st_name.setText("")
        self.st_name.setObjectName("st_name")
        self.verticalLayout_26.addWidget(self.st_name)
        self.st_address = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.st_address.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_address.setFont(font)
        self.st_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.st_address.setObjectName("st_address")
        self.verticalLayout_26.addWidget(self.st_address)
        self.st_email = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.st_email.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_email.setFont(font)
        self.st_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.st_email.setObjectName("st_email")
        self.verticalLayout_26.addWidget(self.st_email)
        self.st_salary = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.st_salary.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_salary.setFont(font)
        self.st_salary.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.st_salary.setObjectName("st_salary")
        self.verticalLayout_26.addWidget(self.st_salary)
        self.st_pass = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.st_pass.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_pass.setFont(font)
        self.st_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"border-width:1px;\n"
"")
        self.st_pass.setObjectName("st_pass")
        self.verticalLayout_26.addWidget(self.st_pass)
        self.st_role = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_role.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_role.setFont(font)
        self.st_role.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_role.setEditable(False)
        self.st_role.setObjectName("st_role")
        self.st_role.addItem("")
        self.st_role.addItem("")
        self.st_role.addItem("")
        self.st_role.addItem("")
        self.st_role.addItem("")
        self.verticalLayout_26.addWidget(self.st_role)
        self.st_dep = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_dep.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_dep.setFont(font)
        self.st_dep.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_dep.setEditable(False)
        self.st_dep.setObjectName("st_dep")
        self.st_dep.addItem("")
        self.st_dep.addItem("")
        self.st_dep.addItem("")
        self.st_dep.addItem("")
        self.st_dep.addItem("")
        self.verticalLayout_26.addWidget(self.st_dep)
        self.st_gender = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_gender.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_gender.setFont(font)
        self.st_gender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_gender.setEditable(False)
        self.st_gender.setObjectName("st_gender")
        self.st_gender.addItem("")
        self.st_gender.addItem("")
        self.verticalLayout_26.addWidget(self.st_gender)
        self.st_work = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_work.setMinimumSize(QtCore.QSize(211, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_work.setFont(font)
        self.st_work.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_work.setEditable(False)
        self.st_work.setObjectName("st_work")
        self.st_work.addItem("")
        self.st_work.addItem("")
        self.st_work.addItem("")
        self.st_work.addItem("")
        self.st_work.setItemText(3, "")
        self.verticalLayout_26.addWidget(self.st_work)
        self.st_birth_lbl = QtWidgets.QLabel(self.layoutWidget_6)
        self.st_birth_lbl.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_birth_lbl.setFont(font)
        self.st_birth_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_birth_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.st_birth_lbl.setObjectName("st_birth_lbl")
        self.verticalLayout_26.addWidget(self.st_birth_lbl)
        self.st_year = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_year.setMinimumSize(QtCore.QSize(211, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_year.setFont(font)
        self.st_year.addItems([str(x) for x in range(1920,2020)])
        self.st_year.setEditable(True)
        self.st_year.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"") 
        self.st_year.setObjectName("st_year")
        self.verticalLayout_26.addWidget(self.st_year)
        self.st_month = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_month.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_month.setFont(font)
        self.st_month.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_month.setEditable(False)
        self.st_month.setObjectName("st_month")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.st_month.addItem("")
        self.verticalLayout_26.addWidget(self.st_month)
        self.st_day = QtWidgets.QComboBox(self.layoutWidget_6)
        self.st_day.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_day.setFont(font)
        self.st_day.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"\n"
"\n"
"\n"
"")
        self.st_day.setEditable(False)
        self.st_day.setObjectName("st_day")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.st_day.addItem("")
        self.verticalLayout_26.addWidget(self.st_day)
        self.st_month_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_month_lbl.setGeometry(QtCore.QRect(310, 365, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_month_lbl.setFont(font)
        self.st_month_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_month_lbl.setObjectName("st_month_lbl")
        self.st_name_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_name_lbl.setGeometry(QtCore.QRect(310, 25, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_name_lbl.setFont(font)
        self.st_name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_name_lbl.setObjectName("st_name_lbl")
        self.st_year_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_year_lbl.setGeometry(QtCore.QRect(310, 335, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_year_lbl.setFont(font)
        self.st_year_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_year_lbl.setObjectName("st_year_lbl")
        self.st_pass_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_pass_lbl.setGeometry(QtCore.QRect(310, 165, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_pass_lbl.setFont(font)
        self.st_pass_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_pass_lbl.setObjectName("st_pass_lbl")
        self.st_pass_lbl.setText("Password:")

        self.st_gender_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_gender_lbl.setGeometry(QtCore.QRect(310, 255, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_gender_lbl.setFont(font)
        self.st_gender_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_gender_lbl.setObjectName("st_gender_lbl")
        self.st_day_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_day_lbl.setGeometry(QtCore.QRect(310, 393, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_day_lbl.setFont(font)
        self.st_day_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_day_lbl.setObjectName("st_day_lbl")
        self.st_add_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_add_lbl.setGeometry(QtCore.QRect(310, 60, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_add_lbl.setFont(font)
        self.st_add_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_add_lbl.setObjectName("st_add_lbl")
        self.st_email_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_email_lbl.setGeometry(QtCore.QRect(310, 95, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_email_lbl.setFont(font)
        self.st_email_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_email_lbl.setObjectName("st_email_lbl")
        self.st_photo = QtWidgets.QWidget(self.add_staff_frame)
        self.st_photo.setGeometry(QtCore.QRect(30, 80, 250, 250))
        self.st_photo.setObjectName("st_photo")
        self.gridLay3 = QtWidgets.QGridLayout(self.st_photo)
        self.gridLay3.setContentsMargins(0, 0, 0, 0)
        self.view3= AppDemo()
        self.gridLay3.addWidget(self.view3, 0, 0, 0, 0)
        
        self.st_clr_image_btn = QtWidgets.QPushButton(self.add_staff_frame)
        self.st_clr_image_btn.setGeometry(QtCore.QRect(60, 340, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_clr_image_btn.setFont(font)
        self.st_clr_image_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"background-color: rgb(170, 0, 127);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 127);\n"
" border-style:inset;\n"
"\n"
"}")
        self.st_clr_image_btn.setObjectName("st_clr_image_btn")
        self.st_role_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_role_lbl.setGeometry(QtCore.QRect(310, 195, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_role_lbl.setFont(font)
        self.st_role_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_role_lbl.setObjectName("st_role_lbl")
        self.st_dep_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_dep_lbl.setGeometry(QtCore.QRect(310, 225, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_dep_lbl.setFont(font)
        self.st_dep_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_dep_lbl.setObjectName("st_dep_lbl")
        self.st_salary_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_salary_lbl.setGeometry(QtCore.QRect(310, 130, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_salary_lbl.setFont(font)
        self.st_salary_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_salary_lbl.setObjectName("st_salary_lbl")
        self.st_work_lbl = QtWidgets.QLabel(self.add_staff_frame)
        self.st_work_lbl.setGeometry(QtCore.QRect(310, 290, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_work_lbl.setFont(font)
        self.st_work_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.st_work_lbl.setObjectName("st_work_lbl")
        self.st_adding_btn = QtWidgets.QPushButton(self.add_staff_frame)
        self.st_adding_btn.setGeometry(QtCore.QRect(610, 430, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_adding_btn.setFont(font)
        self.st_adding_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.st_adding_btn.setObjectName("st_adding_btn")
        self.st_clr_btn = QtWidgets.QPushButton(self.add_staff_frame)
        self.st_clr_btn.setGeometry(QtCore.QRect(500, 430, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.st_clr_btn.setFont(font)
        self.st_clr_btn.setStyleSheet("QPushButton{\n" "outline: none; \n" 
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style:inset;\n"
"\n"
"}")
        self.st_clr_btn.setObjectName("st_clr_btn")
        self.verticalLayout_24.addWidget(self.add_staff_frame)
        self.main_pages_vwr.addWidget(self.add_staff_pg)
        self.verticalLayout_5.addWidget(self.main_pages_vwr)
        self.horizontalLayout_2.addWidget(self.pages_frm)
        self.verticalLayout.addWidget(self.cont_1)
        HIS.setCentralWidget(self.main)

        self.retranslateUi(HIS)
        self.main_pages_vwr.setCurrentIndex(5)
        self.home_options.setCurrentIndex(1)
        self.admission_tab.setCurrentIndex(0)
        self.pharma_tab.setCurrentIndex(0)
        self.rad_options.setCurrentIndex(0)
        self.log_options.setCurrentIndex(0)
        self.dwnld_pdata_btn.hide()
        self.dwnld_raddata_btn.hide()
        db=sqlite3.connect('database/bmd303.db')
        cur=db.cursor()
        query="select order_no from Order_mdcn order by order_no desc limit 1"
        cur.execute(query)
        rec=cur.fetchone()
        self.phar_no_input.setText(str(rec[0]+1))
        
        QtCore.QMetaObject.connectSlotsByName(HIS)



    def retranslateUi(self, HIS):
        _translate = QtCore.QCoreApplication.translate
        HIS.setWindowTitle(_translate("HIS", "MainWindow"))
        self.home.setText(_translate("HIS", "Home"))
        self.admission.setText(_translate("HIS", "Admission"))
        self.pharmacy.setText(_translate("HIS", "Pharmacy"))
        self.radiology.setText(_translate("HIS", "Radiology"))
        self.staff.setText(_translate("HIS", "Staff"))
        self.di1_lbl_1.setText(_translate("HIS", "Available Sets"))
        self.di1_lbl_2.setText(_translate("HIS", "Available Doctors"))
        self.di1_lbl_3.setText(_translate("HIS", "Available Nurses"))
        self.home_options.setTabText(self.home_options.indexOf(self.stats_tab), _translate("HIS", "Home"))
        self.inbox_btn.setText(_translate("HIS", "Inbox"))
        self.inbox_btn_2.setText(_translate("HIS", "+"))
        self.user_name.setText(_translate("HIS", "M&%^^&  M Sami"))
        self.user_email.setText(_translate("HIS", "hero@gmail.ktf"))
        self.user_role.setText(_translate("HIS", "None"))
        self.home_options.setTabText(self.home_options.indexOf(self.profile_tab), _translate("HIS", "Profile"))
        self.p_adding_info_btn.setText(_translate("HIS", "+"))
        self.p_name_lbl.setText(_translate("HIS", "Name:"))
        self.p_n_ID_lbl.setText(_translate("HIS", "National_ID:"))
        self.p_add_lbl.setText(_translate("HIS", "Address:"))
        self.p_gender_lbl.setText(_translate("HIS", "Gender:"))
        self.p_chronic_lbl_2.setText(_translate("HIS", "Chronic Disease: "))
        self.p_month_lbl_4.setText(_translate("HIS", "Month:"))
        self.p_day_lbl_5.setText(_translate("HIS", "Day:"))
        self.p_year_lbl_6.setText(_translate("HIS", "Year:"))
        self.p_email_lbl.setText(_translate("HIS", "@/Phone:"))
        self.p_gender.setItemText(0, _translate("HIS", "Male"))
        self.p_gender.setItemText(1, _translate("HIS", "Female"))
        self.p_chronic.setItemText(0, _translate("HIS", "Diabetes"))
        self.p_chronic.setItemText(1, _translate("HIS", "Cystic Fibrosis"))
        self.p_chronic.setItemText(2, _translate("HIS", "Artritis"))
        self.p_chronic.setItemText(3, _translate("HIS", "Eating Disorders"))
        self.p_chronic.setItemText(4, _translate("HIS", "Obesity"))
        self.p_chronic.setItemText(5, _translate("HIS", "Asthma"))
        self.p_chronic.setItemText(6, _translate("HIS", "Cancer"))
        self.p_chronic.setItemText(7, _translate("HIS", "Other"))
        self.p_chronic.setItemText(8, _translate("HIS", "N/P"))
        self.p_brith_lbl_3.setText(_translate("HIS", "Birth_Date"))
        self.p_month.setItemText(0, _translate("HIS", "Jan"))
        self.p_month.setItemText(1, _translate("HIS", "Feb"))
        self.p_month.setItemText(2, _translate("HIS", "Mar"))
        self.p_month.setItemText(3, _translate("HIS", "Apr"))
        self.p_month.setItemText(4, _translate("HIS", "May"))
        self.p_month.setItemText(5, _translate("HIS", "Jun"))
        self.p_month.setItemText(6, _translate("HIS", "Jul"))
        self.p_month.setItemText(7, _translate("HIS", "Aug"))
        self.p_month.setItemText(8, _translate("HIS", "Sep"))
        self.p_month.setItemText(9, _translate("HIS", "Oct"))
        self.p_month.setItemText(10, _translate("HIS", "Nov"))
        self.p_month.setItemText(11, _translate("HIS", "Dec"))
        self.p_day.setItemText(0, _translate("HIS", "1"))
        self.p_day.setItemText(1, _translate("HIS", "2"))
        self.p_day.setItemText(2, _translate("HIS", "3"))
        self.p_day.setItemText(3, _translate("HIS", "4"))
        self.p_day.setItemText(4, _translate("HIS", "5"))
        self.p_day.setItemText(5, _translate("HIS", "6"))
        self.p_day.setItemText(6, _translate("HIS", "7"))
        self.p_day.setItemText(7, _translate("HIS", "8"))
        self.p_day.setItemText(8, _translate("HIS", "9"))
        self.p_day.setItemText(9, _translate("HIS", "10"))
        self.p_day.setItemText(10, _translate("HIS", "11"))
        self.p_day.setItemText(11, _translate("HIS", "12"))
        self.p_day.setItemText(12, _translate("HIS", "13"))
        self.p_day.setItemText(13, _translate("HIS", "14"))
        self.p_day.setItemText(14, _translate("HIS", "15"))
        self.p_day.setItemText(15, _translate("HIS", "16"))
        self.p_day.setItemText(16, _translate("HIS", "17"))
        self.p_day.setItemText(17, _translate("HIS", "18"))
        self.p_day.setItemText(18, _translate("HIS", "19"))
        self.p_day.setItemText(19, _translate("HIS", "20"))
        self.p_day.setItemText(20, _translate("HIS", "21"))
        self.p_day.setItemText(21, _translate("HIS", "22"))
        self.p_day.setItemText(22, _translate("HIS", "23"))
        self.p_day.setItemText(23, _translate("HIS", "24"))
        self.p_day.setItemText(24, _translate("HIS", "25"))
        self.p_day.setItemText(25, _translate("HIS", "26"))
        self.p_day.setItemText(26, _translate("HIS", "27"))
        self.p_day.setItemText(27, _translate("HIS", "28"))
        self.p_day.setItemText(28, _translate("HIS", "29"))
        self.p_day.setItemText(29, _translate("HIS", "30"))
        self.p_day.setItemText(30, _translate("HIS", "31"))
        self.p_clr_image_btn.setText(_translate("HIS", "Clear Image"))
        self.admission_tab.setTabText(self.admission_tab.indexOf(self.add_p_tab), _translate("HIS", "Add new patient"))
        self.show_p_btn.setText(_translate("HIS", "Load"))
        self.delete_p_btn.setText(_translate("HIS", "Delete"))
        self.update_p_btn.setText(_translate("HIS", "Update"))
        self.admission_tab.setTabText(self.admission_tab.indexOf(self.view_p_tab), _translate("HIS", "View Records"))
        self.pat_search_btn.setText(_translate("HIS", "Search"))
        self.pat_name_s.setText(_translate("HIS", "Name: None"))
        self.pat_age_s.setText(_translate("HIS", "Age: None"))
        self.pat_phone_s.setText(_translate("HIS", "Email/Phone: None"))
        self.pat_national_s.setText(_translate("HIS", "National_ID: None"))
        self.pat_gender_s.setText(_translate("HIS", "Gender: None"))
        self.pat_address_s.setText(_translate("HIS", "Address: None"))
        self.pat_cancel_search_btn_2.setText(_translate("HIS", "X"))
        self.admission_tab.setTabText(self.admission_tab.indexOf(self.search_p_tab), _translate("HIS", "Search"))
        self.mdcn_no_lbl.setText(_translate("HIS", "Order No:"))
        self.mdcn_id_lbl.setText(_translate("HIS", "Patient_ID:"))
        self.mdcn_code_lbl.setText(_translate("HIS", "Medicine Code:"))
        self.mdcn_amount_lbl.setText(_translate("HIS", "Amount:"))
        self.submit_phar_order.setText(_translate("HIS", "Add Item"))
        self.pharma_tab.setTabText(self.pharma_tab.indexOf(self.orders_tab), _translate("HIS", "Add new order"))
        self.outpatient.setText(_translate("HIS", "Non-registered"))
        self.inpatient.setText(_translate("HIS", "Registered"))
        self.delete_order.setText(_translate("HIS", "Delete Order"))
        self.search_order.setText(_translate("HIS", "Search Order"))
        self.load_orders.setText(_translate("HIS", "All orders"))
        self.phar_options.setText(_translate("HIS", "Options"))
        self.pharma_tab.setTabText(self.pharma_tab.indexOf(self.view_orders_tab), _translate("HIS", "View orders"))
        self.delete_drug_btn.setText(_translate("HIS", "Delete"))
        self.show_drug_btn.setText(_translate("HIS", "Load"))
        self.update_drug_btn.setText(_translate("HIS", "Update"))
        self.search_drug_btn.setText(_translate("HIS", "Search"))
        self.add_drug_btn.setText(_translate("HIS", "Add"))
        self.pharma_tab.setTabText(self.pharma_tab.indexOf(self.drug_list_tab), _translate("HIS", "Drugs list"))
        self.rad_adding_btn.setText(_translate("HIS", "+"))
        self.rad_clr_image_btn.setText(_translate("HIS", "Clear Image"))
        self.rad_pat_lbl.setText(_translate("HIS", "Patient_ID"))
        self.rad_type_lbl.setText(_translate("HIS", "Radiography Type"))
        self.rad_rep_lbl.setText(_translate("HIS", "Report"))
        self.rad_conc_lbl.setText(_translate("HIS", "Conclusion"))
        self.rad_options.setTabText(self.rad_options.indexOf(self.rad_add_tab), _translate("HIS", "Add "))
        self.rad_search_btn.setText(_translate("HIS", "Search"))
        self.rad_patsrch_lbl.setText(_translate("HIS", "Patient ID:"))
        self.rad_no_lbl.setText(_translate("HIS", "Image Number:"))
        self.pat_name_rad.setText(_translate("HIS", "Name: None"))
        self.pat_age_rad.setText(_translate("HIS", "Age: None"))
        self.pat_phone_rad.setText(_translate("HIS", "Phone Number: None"))
        self.pat_national_rar.setText(_translate("HIS", "National_ID: None"))
        self.pat_gender_rad.setText(_translate("HIS", "Gender: None"))
        self.pat_address_rad.setText(_translate("HIS", "Address: None"))
        self.rad_cancel_search_btn.setText(_translate("HIS", "X"))
        self.rad_options.setTabText(self.rad_options.indexOf(self.rad_search_tab), _translate("HIS", "Search"))
        self.delete_st_btn.setText(_translate("HIS", "Delete"))
        self.show_st_btn.setText(_translate("HIS", "Load"))
        self.update_st_btn.setText(_translate("HIS", "Update"))
        self.add_st_btn.setText(_translate("HIS", "Add"))
        self.user_labl_nam.setText(_translate("HIS", "Name:"))
        self.user_labl_pass.setText(_translate("HIS", "Password:"))
        self.signin_btn.setText(_translate("HIS", "Sign in"))
        self.sign_clr_btn.setText(_translate("HIS", "Clear"))
        self.log_options.setTabText(self.log_options.indexOf(self.login_tab), _translate("HIS", "Login"))
        self.usr_labl_up.setText(_translate("HIS", "Name:"))
        self.signup_btn.setText(_translate("HIS", "Send"))
        self.user_lbl_email_up.setText(_translate("HIS", "E-mail:"))
        self.signup_clr_btn.setText(_translate("HIS", "Clear"))
        self.user_labl_pass_up.setText(_translate("HIS", "Password:"))
        self.user_labl_role_up.setText(_translate("HIS", "Role:"))
        self.user_labl_conf_up.setText(_translate("HIS", "Confirm_pass:"))
        self.log_options.setTabText(self.log_options.indexOf(self.signup_tab), _translate("HIS", "Sign up"))
        self.sry_lbl.setText(_translate("HIS", "Sorry, This Feature is not available for your Role"))
        self.drug_adding_btn.setText(_translate("HIS", "+"))
        self.drug_name_lbl.setText(_translate("HIS", "Drug Name"))
        self.drug_amount_lbl.setText(_translate("HIS", "Drug Amount"))
        self.drug_price_lbl.setText(_translate("HIS", "Drug Price"))
        self.drug_desc_lbl.setText(_translate("HIS", "Drug Description"))
        self.drug_clr_btn.setText(_translate("HIS", "-"))
        self.st_role.setItemText(0, _translate("HIS", "Pharmacist"))
        self.st_role.setItemText(1, _translate("HIS", "Doctor"))
        self.st_role.setItemText(2, _translate("HIS", "Nurse"))
        self.st_role.setItemText(3, _translate("HIS", "Radiologist"))
        self.st_role.setItemText(4, _translate("HIS", "Admin"))
        self.st_dep.setItemText(0, _translate("HIS", "Radiology"))
        self.st_dep.setItemText(1, _translate("HIS", "Pharmacy"))
        self.st_dep.setItemText(2, _translate("HIS", "Addmission"))
        self.st_dep.setItemText(3, _translate("HIS", "Dental"))
        self.st_dep.setItemText(4, _translate("HIS", "Other"))
        self.st_gender.setItemText(0, _translate("HIS", "Male"))
        self.st_gender.setItemText(1, _translate("HIS", "Female"))
        self.st_work.setItemText(0, _translate("HIS", "7am : 3pm"))
        self.st_work.setItemText(1, _translate("HIS", "3pm : 11pm"))
        self.st_work.setItemText(2, _translate("HIS", "11pm : 7am"))
        self.st_birth_lbl.setText(_translate("HIS", "Birth_Date"))
        self.st_month.setItemText(0, _translate("HIS", "Jan"))
        self.st_month.setItemText(1, _translate("HIS", "Feb"))
        self.st_month.setItemText(2, _translate("HIS", "Mar"))
        self.st_month.setItemText(3, _translate("HIS", "Apr"))
        self.st_month.setItemText(4, _translate("HIS", "May"))
        self.st_month.setItemText(5, _translate("HIS", "Jun"))
        self.st_month.setItemText(6, _translate("HIS", "Jul"))
        self.st_month.setItemText(7, _translate("HIS", "Aug"))
        self.st_month.setItemText(8, _translate("HIS", "Sep"))
        self.st_month.setItemText(9, _translate("HIS", "Oct"))
        self.st_month.setItemText(10, _translate("HIS", "Nov"))
        self.st_month.setItemText(11, _translate("HIS", "Dec"))
        self.st_day.setItemText(0, _translate("HIS", "1"))
        self.st_day.setItemText(1, _translate("HIS", "2"))
        self.st_day.setItemText(2, _translate("HIS", "3"))
        self.st_day.setItemText(3, _translate("HIS", "4"))
        self.st_day.setItemText(4, _translate("HIS", "5"))
        self.st_day.setItemText(5, _translate("HIS", "6"))
        self.st_day.setItemText(6, _translate("HIS", "7"))
        self.st_day.setItemText(7, _translate("HIS", "8"))
        self.st_day.setItemText(8, _translate("HIS", "9"))
        self.st_day.setItemText(9, _translate("HIS", "10"))
        self.st_day.setItemText(10, _translate("HIS", "11"))
        self.st_day.setItemText(11, _translate("HIS", "12"))
        self.st_day.setItemText(12, _translate("HIS", "13"))
        self.st_day.setItemText(13, _translate("HIS", "14"))
        self.st_day.setItemText(14, _translate("HIS", "15"))
        self.st_day.setItemText(15, _translate("HIS", "16"))
        self.st_day.setItemText(16, _translate("HIS", "17"))
        self.st_day.setItemText(17, _translate("HIS", "18"))
        self.st_day.setItemText(18, _translate("HIS", "19"))
        self.st_day.setItemText(19, _translate("HIS", "20"))
        self.st_day.setItemText(20, _translate("HIS", "21"))
        self.st_day.setItemText(21, _translate("HIS", "22"))
        self.st_day.setItemText(22, _translate("HIS", "23"))
        self.st_day.setItemText(23, _translate("HIS", "24"))
        self.st_day.setItemText(24, _translate("HIS", "25"))
        self.st_day.setItemText(25, _translate("HIS", "26"))
        self.st_day.setItemText(26, _translate("HIS", "27"))
        self.st_day.setItemText(27, _translate("HIS", "28"))
        self.st_day.setItemText(28, _translate("HIS", "29"))
        self.st_day.setItemText(29, _translate("HIS", "30"))
        self.st_day.setItemText(30, _translate("HIS", "31"))
        self.st_month_lbl.setText(_translate("HIS", "Month:"))
        self.st_name_lbl.setText(_translate("HIS", "Name:"))
        self.st_year_lbl.setText(_translate("HIS", "Year:"))
        self.st_gender_lbl.setText(_translate("HIS", "Gender:"))
        self.st_day_lbl.setText(_translate("HIS", "Day:"))
        self.st_add_lbl.setText(_translate("HIS", "Address:"))
        self.st_email_lbl.setText(_translate("HIS", "Email:"))
        self.st_clr_image_btn.setText(_translate("HIS", "Clear Image"))
        self.st_role_lbl.setText(_translate("HIS", "Role:"))
        self.st_dep_lbl.setText(_translate("HIS", "Department:"))
        self.st_salary_lbl.setText(_translate("HIS", "Salary:"))
        self.st_work_lbl.setText(_translate("HIS", "WorkingHR:"))
        self.st_adding_btn.setText(_translate("HIS", "+"))
        self.st_clr_btn.setText(_translate("HIS", "-"))

#########################################################################
     #Diagrams section
        self.pro1_d.rpb_setBarStyle('Hybrid1')
        self.pro3_d.rpb_setBarStyle('Hybrid1')
        self.pro1_d.rpb_setInitialPos('West')
        self.pro2_d.rpb_setInitialPos('East')
        self.pro3_d.rpb_setInitialPos('South')
        self.pro1_d.rpb_setDirection('Clockwise')
        self.pro3_d.rpb_setDirection('AntiClockwise')
        self.pro1_d.rpb_setTextFont("Bold")
        self.pro2_d.rpb_setTextFont("Bold")
        self.pro3_d.rpb_setTextFont("Bold")
        self.pro1_d.rpb_setTextColor((4,4,4))
        self.pro1_d.rpb_setLineColor((4,4,4))
        self.pro1_d.rpb_setLineStyle("DotLine")
        self.pro1_d.rpb_setLineWidth(4)
        self.pro1_d.rpb_setCircleColor((255,193,7))
        self.pro1_d.rpb_setTextFormat("Value")
        self.pro2_d.rpb_setTextFormat("Value")
        self.pro3_d.rpb_setTextFormat("Value")
        self.pro1_d.rpb_setPathColor((255,193,7))
        self.pro2_d.rpb_setTextColor((255,255,255))
        self.pro2_d.rpb_setLineColor((0,0,0))
        self.pro2_d.rpb_setLineStyle("DashLine")
        self.pro2_d.rpb_setPathColor((255,255,255))
        self.pro2_d.rpb_setLineWidth(10)
        self.pro2_d.rpb_setPathWidth(4)
        self.pro3_d.rpb_setTextColor((0,0,0))
        self.pro3_d.rpb_setLineColor((0,0,0))
        self.pro3_d.rpb_setLineStyle("DashLine")
        self.pro3_d.rpb_setPathColor((255,182,193))
        self.pro3_d.rpb_setCircleColor((255,182,193))
        self.pro3_d.rpb_setLineWidth(10)
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(lambda:ac.Interface_actions.d_progress(self))
        self.timer.start(1000)
        self.timer.singleShot(0,lambda: self.pro1_d.rpb_setValue(0))
        self.timer.singleShot(0,lambda: self.pro2_d.rpb_setValue(0))
        self.timer.singleShot(0,lambda: self.pro3_d.rpb_setValue(0))
########################################################################################  
        self.tgl_btn.clicked.connect(lambda:ac.Interface_actions.menu_slide(self))
        self.cls_btn.clicked.connect(lambda:ac.Interface_actions.Close(self))
        self.minimize_btn.clicked.connect(lambda:ac.Interface_actions.minimize(self))
        self.admission.clicked.connect(lambda:ac.Interface_actions.change_page(self,1))
        self.home.clicked.connect(lambda:ac.Interface_actions.change_page(self,0))
        self.pharmacy.clicked.connect(lambda:ac.Interface_actions.change_page(self,2))
        self.radiology.clicked.connect(lambda:ac.Interface_actions.change_page(self,3))
        self.staff.clicked.connect(lambda:ac.Interface_actions.change_page(self,4))
        self.add_st_btn.clicked.connect(lambda:ac.Interface_actions.change_page(self,8))
        self.add_drug_btn.clicked.connect(lambda:ac.Interface_actions.change_page(self,7))
        self.show_p_btn.clicked.connect(lambda:pa.Patients.view_pateints_data(self))
        self.p_adding_info_btn.clicked.connect(lambda:pa.Patients.InsertPatientInfo(self,p_image))
        self.delete_p_btn.clicked.connect(lambda:pa.Patients.DeletePatientInfo(self))
        self.delete_p_btn.clicked.connect(lambda:pa.Patients.view_pateints_data(self))
        self.update_p_btn.clicked.connect(lambda:pa.Patients.ModifyPatientInfo(self))
        self.update_p_btn.clicked.connect(lambda:pa.Patients.view_pateints_data(self))
        self.pat_search_btn.clicked.connect(lambda:pa.Patients.search_pat(self))
        self.pat_cancel_search_btn_2.clicked.connect(lambda:pa.Patients.clear_srch_pat(self))
        self.signin_btn.clicked.connect(lambda:au.Auth.login(self))
        self.sign_clr_btn.clicked.connect(lambda:au.Auth.log_clear(self))
        self.signup_clr_btn.clicked.connect(lambda:au.Auth.signup_clear(self))
        self.signup_btn.clicked.connect(lambda:au.Auth.sign_up(self))
        self.inbox_btn.clicked.connect(lambda:au.Auth.read_inbox(self))
        self.msgs_list.itemClicked.connect(lambda:au.Auth.item_click(self))
        self.inbox_btn_2.clicked.connect(lambda:au.Auth.send_msg(self))
        self.p_clr_image_btn.clicked.connect(lambda:AppDemo.clear_image(self))
        self.show_st_btn.clicked.connect(lambda:pa.Staff.view_staff(self))
        self.update_st_btn.clicked.connect(lambda:pa.Staff.update_staff(self))
        self.update_st_btn.clicked.connect(lambda:pa.Staff.view_staff(self))
        self.delete_st_btn.clicked.connect(lambda:pa.Staff.delete_staff(self))
        self.delete_st_btn.clicked.connect(lambda:pa.Staff.view_staff(self))
        self.st_adding_btn.clicked.connect(lambda:pa.Staff.add_staff(self,p_image))
        self.st_clr_btn.clicked.connect(lambda:pa.Staff.cancel_add_staff(self))
        self.st_clr_image_btn.clicked.connect(lambda:AppDemo.clear_st_image(self))
        self.phar_options.clicked.connect(lambda:ac.Interface_actions.drug_opt(self))
        self.drug_adding_btn.clicked.connect(lambda:pr.Pharma.InsertDrugInfo(self))
        self.drug_clr_btn.clicked.connect(lambda:pr.Pharma.ClearDrugData(self))
        self.show_drug_btn.clicked.connect(lambda:pr.Pharma.view_drug_data(self))
        self.delete_drug_btn.clicked.connect(lambda:pr.Pharma.DeleteDrugInfo(self))
        self.delete_drug_btn.clicked.connect(lambda:pr.Pharma.view_drug_data(self))
        self.update_drug_btn.clicked.connect(lambda:pr.Pharma.ModifyDrugInfo(self))
        self.update_drug_btn.clicked.connect(lambda:pr.Pharma.view_drug_data(self))
        self.search_drug_btn.clicked.connect(lambda:pr.Pharma.search_drug(self))
        self.submit_phar_order.clicked.connect(lambda:pr.Pharma.add_order(self))
        self.clr_phar_order.clicked.connect(lambda:pr.Pharma.clear_order(self))
        self.load_orders.clicked.connect(lambda:pr.Pharma.ViewAllOrders(self))
        self.inpatient.clicked.connect(lambda:pr.Pharma.ViewInOrders(self))
        self.outpatient.clicked.connect(lambda:pr.Pharma.ViewOutOrders(self))
        self.delete_order.clicked.connect(lambda:pr.Pharma.DeleteOrders(self))
        self.delete_order.clicked.connect(lambda:pr.Pharma.ViewAllOrders(self))
        self.search_order.clicked.connect(lambda:pr.Pharma.search_order(self))
        self.rad_adding_btn.clicked.connect(lambda:pr.Radiology.add_rad(self,p_image))
        self.rad_clr_image_btn.clicked.connect(lambda:AppDemo.clear_rad_image(self))
        self.rad_search_btn.clicked.connect(lambda:pr.Radiology.search_rad(self))
        self.rad_cancel_search_btn.clicked.connect(lambda:pr.Radiology.clr_rad_search(self))
######################################################################################

import interface_actions as ac
import patients_staff as pa
import rad_pharma as pr
import auth as au
import images

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w=ac.Interface_actions()
    w.show()
    sys.exit(app.exec())
