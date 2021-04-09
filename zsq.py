# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zsq.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 621)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app/草莓.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("\n"
"QPalette{background:#F0F0F0;}QGroupBox#gboxDevicePanel>QLabel{color:#CACAD0;}\n"
"\n"
"QWidget#frmMain,QWidget[Form=\"true\"]{\n"
"border:1px solid #575757;\n"
"border-radius:0px;\n"
"}\n"
"\n"
".QFrame{\n"
"border:1px solid #D8D8D8;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QLabel,QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QGroupBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox,QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"color:#232524;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"border-radius:0px;\n"
"color:#CACAD0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton,QWidget#widget_frm>QLabel{\n"
"border-style:none;\n"
"padding:10px;\n"
"color:#CACAD0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QToolButton:hover,QWidget#widget_frm>QLabel:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]{\n"
"color:#CACAD0;\n"
"border:1px solid #575757;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]:focus{\n"
"border:1px solid #FF0000;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox{\n"
"border:1px solid #D8D8D8;\n"
"border-radius:5px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#4D4D4D;\n"
"selection-color:#CACAD0;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
".QGroupBox{\n"
"border:1px solid #D8D8D8;\n"
"border-radius:5px;\n"
"\n"
"}\n"
"\n"
".QPushButton{\n"
"border-style:none;\n"
"border:1px solid #D8D8D8;\n"
"color:#CACAD0;\n"
"padding:5px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
".QPushButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
".QPushButton:disabled{\n"
"color:#838383;\n"
"background:#F4F4F4;\n"
"}\n"
"\n"
"QPushButton#btnSplitterH{\n"
"padding:2px;\n"
"min-height:8px;\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close,QPushButton#btnSplitterV,QPushButton#btnSplitterH{\n"
"border-radius:0px;\n"
"color:#CACAD0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover,QPushButton#btnSplitterV:hover,QPushButton#btnSplitterH:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,134,199,0),stop:1 #636363);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(238,0,0,128),stop:1 rgba(238,44,44,255));\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:#232524;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width:20px;\n"
"height:20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/app/Checkbox Unchecked-1.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/app/Checkbox Checked.png);\n"
"}\n"
"\n"
"QRadioButton{\n"
"color:#232524;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/image/radio_normal.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/image/radio_selected.png);\n"
"}\n"
"\n"
"QSpinBox::up-button,QDateEdit::up-button,QTimeEdit::up-button,QDateTimeEdit::up-button{\n"
"image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QSpinBox::down-button,QDateEdit::down-button,QTimeEdit::down-button,QDateTimeEdit::down-button{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox{\n"
"border-radius:3px;\n"
"padding:3px 5px 3px 5px;\n"
"border:1px solid #D8D8D8;\n"
"background:none;\n"
"selection-background-color:#4D4D4D;\n"
"selection-color:#CACAD0;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:1px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#D8D8D8;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow,QTimeEdit::down-arrow,QDateTimeEdit::down-arrow{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QMenu{\n"
"color:#CACAD0;\n"
"background-color:#4D4D4D;\n"
"margin:2px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px 3px 20px;\n"
"}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"color:#CACAD0;\n"
"border:0px solid #575757;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#575757;\n"
"}\n"
"\n"
"QProgressBar{\n"
"background:#D8D8D8;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #D8D8D8;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"width:5px;\n"
"margin:0.5px;\n"
"background-color:#4D4D4D;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#D8D8D8;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#575757;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #575757);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#D8D8D8;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#575757;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:13px;\n"
"margin-left:-2px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #575757);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"width:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"height:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,QScrollBar::handle:horizontal{\n"
"width:10px;\n"
"background:#575757;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover{\n"
"width:10px;\n"
"background:#292929;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:bottom;\n"
"subcontrol-origin:margin;\n"
"border-border-image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_right.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:top;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:left;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_left.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical,QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"width:10px;\n"
"background:#D8D8D8;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #D8D8D8;\n"
"selection-background-color:#636363;\n"
"selection-color:#232524;\n"
"alternate-background-color:#DDE0E7;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#CACAD0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{\n"
"color:#CACAD0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
"padding:5px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#CACAD0;\n"
"border:1px solid #575757;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border-radius:5px;\n"
"border:1px solid #D8D8D8;\n"
"color:#CACAD0;\n"
"min-width:55px;\n"
"min-height:20px;\n"
"padding:3px 8px 3px 8px;\n"
"margin:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #4D4D4D;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QToolTip,QGroupBox#gboxDevicePanel{\n"
"padding:3px;\n"
"border-radius: 5px;\n"
"color:#CACAD0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #636363,stop:1 #575757);\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 87))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 218, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/app/草莓.png"))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 16))
        self.pushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(233, 255, 215);\n"
"   \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"   \n"
"    background-color: rgb(255, 226, 249);\n"
"}\n"
"")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/app/减号.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 16))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(233, 255, 215);\n"
"   \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"   \n"
"    background-color: rgb(255, 226, 249);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/app/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 16pt \"华文琥珀\";\n"
"border:2px solid rgb(79, 79, 79)\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(231, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 4, 1, 2)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 306))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 238);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tq_verticalLayout = QtWidgets.QVBoxLayout()
        self.tq_verticalLayout.setSpacing(0)
        self.tq_verticalLayout.setObjectName("tq_verticalLayout")
        self.gridLayout.addLayout(self.tq_verticalLayout, 0, 0, 4, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setMinimumSize(QtCore.QSize(268, 131))
        self.frame.setMaximumSize(QtCore.QSize(268, 131))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_5.setObjectName("label_5")
        self.checkBox1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox1.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.checkBox1.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    image: url(:/app/checkbox-checked (7).png);\n"
"}")
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox2.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.checkBox2.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (1).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"    image: url(:/app/checkbox-checked (6).png);\n"
"}")
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox3.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.checkBox3.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (2).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    image: url(:/app/checkbox-checked (5).png);\n"
"}")
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox4.setGeometry(QtCore.QRect(10, 96, 51, 20))
        self.checkBox4.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (3).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"    image: url(:/app/checkbox-checked (4).png);\n"
"}")
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox5.setGeometry(QtCore.QRect(90, 40, 51, 16))
        self.checkBox5.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (4).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/app/checkbox-checked (3).png);\n"
"}")
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox6.setGeometry(QtCore.QRect(90, 60, 51, 16))
        self.checkBox6.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (5).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/app/checkbox-checked (2).png);\n"
"}")
        self.checkBox6.setObjectName("checkBox6")
        self.checkBox7 = QtWidgets.QCheckBox(self.frame)
        self.checkBox7.setGeometry(QtCore.QRect(90, 80, 51, 16))
        self.checkBox7.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (6).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    image: url(:/app/checkbox-checked (1).png);\n"
"}")
        self.checkBox7.setObjectName("checkBox7")
        self.checkBox8 = QtWidgets.QCheckBox(self.frame)
        self.checkBox8.setGeometry(QtCore.QRect(90, 100, 51, 16))
        self.checkBox8.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (7).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    image: url(:/app/checkbox-checked.png);\n"
"}")
        self.checkBox8.setObjectName("checkBox8")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setMaximumSize(QtCore.QSize(268, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.flushed_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.flushed_pushButton.setMaximumSize(QtCore.QSize(44, 44))
        self.flushed_pushButton.setStyleSheet("\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(233, 255, 215);\n"
"   \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"   \n"
"    background-color: rgb(255, 226, 249);\n"
"}")
        self.flushed_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/app/刷新 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flushed_pushButton.setIcon(icon3)
        self.flushed_pushButton.setIconSize(QtCore.QSize(32, 32))
        self.flushed_pushButton.setObjectName("flushed_pushButton")
        self.gridLayout.addWidget(self.flushed_pushButton, 2, 2, 2, 1)
        self.atcheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.atcheckBox.setChecked(True)
        self.atcheckBox.setObjectName("atcheckBox")
        self.gridLayout.addWidget(self.atcheckBox, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 231))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 231))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 238);\n"
"GroupBox{\n"
"    border:2px solid rgb(79, 79, 79);}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(-1, 12, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 8)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.phoneLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.phoneLineEdit.setStyleSheet("")
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.gridLayout_4.addWidget(self.phoneLineEdit, 1, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 1, 4, 1, 1)
        self.hlCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.hlCheckBox.setChecked(True)
        self.hlCheckBox.setAutoExclusive(False)
        self.hlCheckBox.setObjectName("hlCheckBox")
        self.gridLayout_4.addWidget(self.hlCheckBox, 1, 5, 1, 1)
        self.bd_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.bd_checkBox.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (9).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"    image: url(:/app/checkbox-checked (9).png);\n"
"}")
        self.bd_checkBox.setObjectName("bd_checkBox")
        self.gridLayout_4.addWidget(self.bd_checkBox, 1, 6, 1, 1)
        self.sendPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.sendPushButton.setMinimumSize(QtCore.QSize(81, 0))
        self.sendPushButton.setStyleSheet("QPushButton{background-color: rgb(255, 221, 229);}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(233, 255, 215);\n"
"   \n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"   \n"
"    background-color: rgb(255, 226, 249);\n"
"}\n"
"")
        self.sendPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/app/发送.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendPushButton.setIcon(icon4)
        self.sendPushButton.setIconSize(QtCore.QSize(32, 32))
        self.sendPushButton.setObjectName("sendPushButton")
        self.gridLayout_4.addWidget(self.sendPushButton, 1, 7, 2, 1)
        self.webHookLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.webHookLineEdit.setStyleSheet("")
        self.webHookLineEdit.setObjectName("webHookLineEdit")
        self.gridLayout_4.addWidget(self.webHookLineEdit, 2, 0, 1, 2)
        self.sercertLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.sercertLineEdit.setStyleSheet("")
        self.sercertLineEdit.setObjectName("sercertLineEdit")
        self.gridLayout_4.addWidget(self.sercertLineEdit, 2, 2, 1, 1)
        self.autoJumCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.autoJumCheckBox.setChecked(True)
        self.autoJumCheckBox.setTristate(False)
        self.autoJumCheckBox.setObjectName("autoJumCheckBox")
        self.gridLayout_4.addWidget(self.autoJumCheckBox, 2, 3, 1, 2)
        self.ltCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.ltCheckBox.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"image: url(:/app/checkbox-unchecked (8).png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    \n"
"    \n"
"    image: url(:/app/checkbox-checked (8).png);\n"
"}")
        self.ltCheckBox.setObjectName("ltCheckBox")
        self.gridLayout_4.addWidget(self.ltCheckBox, 2, 5, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "案源发送（张书侨）"))
        self.label_3.setText(_translate("Form", "案源分发V2.0"))
        self.label_5.setText(_translate("Form", "勾选后跳过发送："))
        self.checkBox1.setText(_translate("Form", "1 王"))
        self.checkBox2.setText(_translate("Form", "2 周"))
        self.checkBox3.setText(_translate("Form", "3 彭"))
        self.checkBox4.setText(_translate("Form", "4 李"))
        self.checkBox5.setText(_translate("Form", "5 贺"))
        self.checkBox6.setText(_translate("Form", "6 余"))
        self.checkBox7.setText(_translate("Form", "7 郎"))
        self.checkBox8.setText(_translate("Form", "8 尹"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.checkBox_3.setText(_translate("Form", "自动写入EXCEL"))
        self.atcheckBox.setText(_translate("Form", "@收件人"))
        self.groupBox_2.setTitle(_translate("Form", "输入区"))
        self.label_2.setText(_translate("Form", "客户手机号*："))
        self.label_6.setText(_translate("Form", "发送至："))
        self.comboBox.setItemText(0, _translate("Form", "1.王"))
        self.comboBox.setItemText(1, _translate("Form", "2.周"))
        self.comboBox.setItemText(2, _translate("Form", "3.彭"))
        self.comboBox.setItemText(3, _translate("Form", "4.李"))
        self.comboBox.setItemText(4, _translate("Form", "5.贺"))
        self.comboBox.setItemText(5, _translate("Form", "6.余"))
        self.comboBox.setItemText(6, _translate("Form", "7.郎"))
        self.comboBox.setItemText(7, _translate("Form", "8.尹"))
        self.hlCheckBox.setText(_translate("Form", "华律"))
        self.bd_checkBox.setText(_translate("Form", "百度"))
        self.autoJumCheckBox.setText(_translate("Form", "自动跳转开关"))
        self.ltCheckBox.setText(_translate("Form", "律图"))

import app_rc
