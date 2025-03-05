# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_bs.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 796)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel{\n"
"    color: rgb(0, 0, 127);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QComboBox{\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QLineEdit{\n"
"font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTableView{\n"
"    border-color: rgb(0, 85, 0);\n"
"    \n"
"    alternate-background-color: rgb(230, 201, 255);\n"
"    background-color: rgb(199, 205, 255);\n"
"/*    selection-background-color: rgb(85, 255, 0);*/\n"
"\n"
"}\n"
"QPushButton{\n"
"    /*background-color: rgb(170, 255, 127);*/\n"
"    \n"
"    font: 16pt \"Microsoft Sans Serif\";\n"
"    \n"
"    background-color: rgb(239, 239, 119);\n"
"}\n"
"QCheckBox{\n"
"font: 12pt \"Microsoft Sans Serif\";\n"
"    color: rgb(255, 85, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pushButton_art = QtWidgets.QPushButton(self.centralwidget)
        self.open_pushButton_art.setGeometry(QtCore.QRect(1030, 0, 191, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_pushButton_art.sizePolicy().hasHeightForWidth())
        self.open_pushButton_art.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.open_pushButton_art.setFont(font)
        self.open_pushButton_art.setStyleSheet("background-color: rgb(115, 170, 130);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("sourcefile/open2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_pushButton_art.setIcon(icon1)
        self.open_pushButton_art.setObjectName("open_pushButton_art")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 170, 64, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(91, 170, 135, 26))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(347, 171, 103, 26))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 171, 101, 20))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 174, 141, 20))
        self.label_4.setObjectName("label_4")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(596, 172, 151, 26))
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(21, 210, 64, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_r1c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r1c1.setGeometry(QtCore.QRect(91, 209, 71, 31))
        self.lineEdit_r1c1.setObjectName("lineEdit_r1c1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(213, 212, 74, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_r1c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r1c2.setGeometry(QtCore.QRect(300, 212, 60, 30))
        self.lineEdit_r1c2.setObjectName("lineEdit_r1c2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 210, 81, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_r1c3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r1c3.setEnabled(True)
        self.lineEdit_r1c3.setGeometry(QtCore.QRect(480, 210, 61, 31))
        self.lineEdit_r1c3.setObjectName("lineEdit_r1c3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 210, 81, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_r1c4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r1c4.setEnabled(True)
        self.lineEdit_r1c4.setGeometry(QtCore.QRect(650, 210, 61, 31))
        self.lineEdit_r1c4.setObjectName("lineEdit_r1c4")
        self.lineEdit_r2c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r2c2.setGeometry(QtCore.QRect(299, 270, 61, 31))
        self.lineEdit_r2c2.setObjectName("lineEdit_r2c2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(212, 270, 81, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 270, 81, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_r2c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r2c1.setGeometry(QtCore.QRect(100, 270, 61, 31))
        self.lineEdit_r2c1.setObjectName("lineEdit_r2c1")
        self.lineEdit_r3c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r3c1.setGeometry(QtCore.QRect(110, 330, 61, 31))
        self.lineEdit_r3c1.setObjectName("lineEdit_r3c1")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(206, 330, 81, 31))
        self.label_12.setObjectName("label_12")
        self.lineEdit_r3c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r3c2.setGeometry(QtCore.QRect(300, 330, 61, 31))
        self.lineEdit_r3c2.setObjectName("lineEdit_r3c2")
        self.add_pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton2.setEnabled(True)
        self.add_pushButton2.setGeometry(QtCore.QRect(20, 400, 161, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/add2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_pushButton2.setIcon(icon2)
        self.add_pushButton2.setObjectName("add_pushButton2")
        self.process_pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.process_pushButton3.setEnabled(False)
        self.process_pushButton3.setGeometry(QtCore.QRect(220, 400, 151, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.process_pushButton3.setIcon(icon3)
        self.process_pushButton3.setObjectName("process_pushButton3")
        self.process_tableView2 = QtWidgets.QTableView(self.centralwidget)
        self.process_tableView2.setGeometry(QtCore.QRect(10, 460, 1240, 301))
        self.process_tableView2.setAlternatingRowColors(True)
        self.process_tableView2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.process_tableView2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.process_tableView2.setObjectName("process_tableView2")
        self.open_tableView1 = QtWidgets.QTableView(self.centralwidget)
        self.open_tableView1.setGeometry(QtCore.QRect(10, 50, 1231, 81))
        self.open_tableView1.setAlternatingRowColors(True)
        self.open_tableView1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.open_tableView1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.open_tableView1.setObjectName("open_tableView1")
        self.open_tableView1.horizontalHeader().setCascadingSectionResizes(False)
        self.open_tableView1.horizontalHeader().setDefaultSectionSize(50)
        self.open_tableView1.horizontalHeader().setStretchLastSection(True)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(387, 406, 771, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.frame_act_size = QtWidgets.QFrame(self.centralwidget)
        self.frame_act_size.setGeometry(QtCore.QRect(610, 260, 431, 121))
        self.frame_act_size.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_act_size.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_act_size.setObjectName("frame_act_size")
        self.lineEdit_r3c3 = QtWidgets.QLineEdit(self.frame_act_size)
        self.lineEdit_r3c3.setEnabled(True)
        self.lineEdit_r3c3.setGeometry(QtCore.QRect(110, 70, 81, 31))
        self.lineEdit_r3c3.setText("")
        self.lineEdit_r3c3.setObjectName("lineEdit_r3c3")
        self.label_15 = QtWidgets.QLabel(self.frame_act_size)
        self.label_15.setGeometry(QtCore.QRect(13, 75, 91, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_r2c3 = QtWidgets.QLineEdit(self.frame_act_size)
        self.lineEdit_r2c3.setEnabled(True)
        self.lineEdit_r2c3.setGeometry(QtCore.QRect(110, 15, 81, 31))
        self.lineEdit_r2c3.setObjectName("lineEdit_r2c3")
        self.label_14 = QtWidgets.QLabel(self.frame_act_size)
        self.label_14.setGeometry(QtCore.QRect(13, 20, 91, 20))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.frame_act_size)
        self.label_16.setGeometry(QtCore.QRect(240, 70, 91, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_r2c4 = QtWidgets.QLineEdit(self.frame_act_size)
        self.lineEdit_r2c4.setEnabled(True)
        self.lineEdit_r2c4.setGeometry(QtCore.QRect(330, 15, 61, 31))
        self.lineEdit_r2c4.setObjectName("lineEdit_r2c4")
        self.lineEdit_r3c4 = QtWidgets.QLineEdit(self.frame_act_size)
        self.lineEdit_r3c4.setEnabled(True)
        self.lineEdit_r3c4.setGeometry(QtCore.QRect(330, 70, 61, 31))
        self.lineEdit_r3c4.setText("")
        self.lineEdit_r3c4.setObjectName("lineEdit_r3c4")
        self.label_13 = QtWidgets.QLabel(self.frame_act_size)
        self.label_13.setGeometry(QtCore.QRect(240, 15, 91, 31))
        self.label_13.setObjectName("label_13")
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(920, 171, 87, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox1.setFont(font)
        self.checkBox1.setChecked(False)
        self.checkBox1.setObjectName("checkBox1")
        self.frame_bleeding = QtWidgets.QFrame(self.centralwidget)
        self.frame_bleeding.setGeometry(QtCore.QRect(760, 205, 291, 41))
        self.frame_bleeding.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bleeding.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bleeding.setObjectName("frame_bleeding")
        self.lineEdit_r1c6 = QtWidgets.QLineEdit(self.frame_bleeding)
        self.lineEdit_r1c6.setGeometry(QtCore.QRect(230, 4, 61, 31))
        self.lineEdit_r1c6.setObjectName("lineEdit_r1c6")
        self.label_18 = QtWidgets.QLabel(self.frame_bleeding)
        self.label_18.setGeometry(QtCore.QRect(160, 4, 81, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_r1c5 = QtWidgets.QLineEdit(self.frame_bleeding)
        self.lineEdit_r1c5.setGeometry(QtCore.QRect(80, 4, 61, 31))
        self.lineEdit_r1c5.setObjectName("lineEdit_r1c5")
        self.label_17 = QtWidgets.QLabel(self.frame_bleeding)
        self.label_17.setGeometry(QtCore.QRect(11, 3, 81, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_BsKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_BsKey.setEnabled(False)
        self.lineEdit_BsKey.setGeometry(QtCore.QRect(1000, 137, 51, 31))
        self.lineEdit_BsKey.setToolTip("")
        self.lineEdit_BsKey.setReadOnly(True)
        self.lineEdit_BsKey.setObjectName("lineEdit_BsKey")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(174, 15, 601, 21))
        self.label_19.setObjectName("label_19")
        self.comboBox_PDFitem = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_PDFitem.setEnabled(False)
        self.comboBox_PDFitem.setGeometry(QtCore.QRect(1080, 138, 80, 26))
        self.comboBox_PDFitem.setToolTip("")
        self.comboBox_PDFitem.setObjectName("comboBox_PDFitem")
        self.open_pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.open_pushButton1.setGeometry(QtCore.QRect(800, 0, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_pushButton1.sizePolicy().hasHeightForWidth())
        self.open_pushButton1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.open_pushButton1.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/ITProg02/.designer/backup/sourcefile/open2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_pushButton1.setIcon(icon4)
        self.open_pushButton1.setObjectName("open_pushButton1")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(770, 174, 64, 20))
        self.label_21.setObjectName("label_21")
        self.comboBox_rotate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_rotate.setGeometry(QtCore.QRect(840, 172, 61, 26))
        self.comboBox_rotate.setObjectName("comboBox_rotate")
        self.comboBox_rotate.addItem("")
        self.comboBox_rotate.addItem("")
        self.comboBox_rotate.addItem("")
        self.comboBox_rotate.addItem("")
        self.lineEdit_Repeat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Repeat.setGeometry(QtCore.QRect(1130, 270, 60, 30))
        self.lineEdit_Repeat.setObjectName("lineEdit_Repeat")
        self.checkBox_blank2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_blank2.setGeometry(QtCore.QRect(1107, 172, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_blank2.setFont(font)
        self.checkBox_blank2.setChecked(False)
        self.checkBox_blank2.setObjectName("checkBox_blank2")
        self.checkBox_blank = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_blank.setGeometry(QtCore.QRect(1027, 172, 87, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_blank.setFont(font)
        self.checkBox_blank.setChecked(False)
        self.checkBox_blank.setObjectName("checkBox_blank")
        self.checkBox_addpage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_addpage.setGeometry(QtCore.QRect(1110, 212, 87, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_addpage.setFont(font)
        self.checkBox_addpage.setChecked(False)
        self.checkBox_addpage.setObjectName("checkBox_addpage")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1060, 274, 74, 20))
        self.label_22.setObjectName("label_22")
        self.label_art = QtWidgets.QLabel(self.centralwidget)
        self.label_art.setGeometry(QtCore.QRect(350, 140, 511, 21))
        self.label_art.setObjectName("label_art")
        self.lineEdit_StartSeq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_StartSeq.setGeometry(QtCore.QRect(1130, 320, 71, 30))
        self.lineEdit_StartSeq.setObjectName("lineEdit_StartSeq")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1060, 320, 71, 31))
        self.label_23.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_23.setLineWidth(1)
        self.label_23.setMidLineWidth(0)
        self.label_23.setObjectName("label_23")
        self.OpenExcel = QtWidgets.QPushButton(self.centralwidget)
        self.OpenExcel.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.OpenExcel.setObjectName("OpenExcel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.menu.setFont(font)
        self.menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menu.setToolTip("")
        self.menu.setWhatsThis("")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_importxls = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_importxls.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        self.action_importxls.setFont(font)
        self.action_importxls.setObjectName("action_importxls")
        self.action_output = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_output.setIcon(icon6)
        self.action_output.setObjectName("action_output")
        self.action2 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/8923926.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action2.setIcon(icon7)
        self.action2.setObjectName("action2")
        self.action_dele = QtWidgets.QAction(MainWindow)
        self.action_dele.setObjectName("action_dele")
        self.menu.addAction(self.action_importxls)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action_output)
        self.menu.addAction(self.action_dele)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox1.setCurrentIndex(2)
        self.comboBox2.setCurrentIndex(0)
        self.comboBox3.setCurrentIndex(0)
        self.comboBox_PDFitem.setCurrentIndex(-1)
        self.comboBox_rotate.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_BsKey, self.comboBox_PDFitem)
        MainWindow.setTabOrder(self.comboBox_PDFitem, self.open_pushButton1)
        MainWindow.setTabOrder(self.open_pushButton1, self.open_tableView1)
        MainWindow.setTabOrder(self.open_tableView1, self.open_pushButton_art)
        MainWindow.setTabOrder(self.open_pushButton_art, self.comboBox1)
        MainWindow.setTabOrder(self.comboBox1, self.comboBox2)
        MainWindow.setTabOrder(self.comboBox2, self.comboBox3)
        MainWindow.setTabOrder(self.comboBox3, self.comboBox_rotate)
        MainWindow.setTabOrder(self.comboBox_rotate, self.checkBox1)
        MainWindow.setTabOrder(self.checkBox1, self.checkBox_blank)
        MainWindow.setTabOrder(self.checkBox_blank, self.checkBox_blank2)
        MainWindow.setTabOrder(self.checkBox_blank2, self.lineEdit_r1c1)
        MainWindow.setTabOrder(self.lineEdit_r1c1, self.lineEdit_r1c2)
        MainWindow.setTabOrder(self.lineEdit_r1c2, self.lineEdit_r2c1)
        MainWindow.setTabOrder(self.lineEdit_r2c1, self.lineEdit_r2c2)
        MainWindow.setTabOrder(self.lineEdit_r2c2, self.lineEdit_r1c3)
        MainWindow.setTabOrder(self.lineEdit_r1c3, self.lineEdit_r1c4)
        MainWindow.setTabOrder(self.lineEdit_r1c4, self.lineEdit_r1c5)
        MainWindow.setTabOrder(self.lineEdit_r1c5, self.lineEdit_r1c6)
        MainWindow.setTabOrder(self.lineEdit_r1c6, self.checkBox_addpage)
        MainWindow.setTabOrder(self.checkBox_addpage, self.lineEdit_r2c3)
        MainWindow.setTabOrder(self.lineEdit_r2c3, self.lineEdit_r2c4)
        MainWindow.setTabOrder(self.lineEdit_r2c4, self.lineEdit_r3c3)
        MainWindow.setTabOrder(self.lineEdit_r3c3, self.lineEdit_r3c4)
        MainWindow.setTabOrder(self.lineEdit_r3c4, self.lineEdit_Repeat)
        MainWindow.setTabOrder(self.lineEdit_Repeat, self.lineEdit_StartSeq)
        MainWindow.setTabOrder(self.lineEdit_StartSeq, self.lineEdit_r3c1)
        MainWindow.setTabOrder(self.lineEdit_r3c1, self.lineEdit_r3c2)
        MainWindow.setTabOrder(self.lineEdit_r3c2, self.add_pushButton2)
        MainWindow.setTabOrder(self.add_pushButton2, self.process_pushButton3)
        MainWindow.setTabOrder(self.process_pushButton3, self.process_tableView2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF鋪數軟件"))
        self.open_pushButton_art.setText(_translate("MainWindow", "打開需排版稿件"))
        self.label_2.setText(_translate("MainWindow", "編號次序"))
        self.comboBox1.setCurrentText(_translate("MainWindow", "3:兜圈順序打印"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "1:從小到大"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "2:從大到小"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "3:兜圈順序打印"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "1:从左到右"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "2:从上到下"))
        self.label_3.setText(_translate("MainWindow", "PDF輸出方向"))
        self.label_4.setText(_translate("MainWindow", "出血位及顯示位置"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "0:排版後無出血位"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "1:左上角水平位置"))
        self.comboBox3.setItemText(2, _translate("MainWindow", "2:左上角垂直位置"))
        self.comboBox3.setItemText(3, _translate("MainWindow", "3:右上角水平位置"))
        self.comboBox3.setItemText(4, _translate("MainWindow", "4:右上角垂直位置"))
        self.comboBox3.setItemText(5, _translate("MainWindow", "5:左下角水平位置"))
        self.comboBox3.setItemText(6, _translate("MainWindow", "6:左下角垂直位置"))
        self.comboBox3.setItemText(7, _translate("MainWindow", "7:右下角水平位置"))
        self.comboBox3.setItemText(8, _translate("MainWindow", "8:右下角垂直位置"))
        self.label_5.setText(_translate("MainWindow", "橫排個數"))
        self.label_6.setText(_translate("MainWindow", "橫刀位(寸)"))
        self.label_7.setText(_translate("MainWindow", "左右出血位(寸)"))
        self.label_8.setText(_translate("MainWindow", "上下出血位(寸)"))
        self.label_9.setText(_translate("MainWindow", "豎刀位(寸)"))
        self.label_10.setText(_translate("MainWindow", "豎排個數"))
        self.label_11.setText(_translate("MainWindow", "一箱張數"))
        self.label_12.setText(_translate("MainWindow", "PDF檔頁數"))
        self.add_pushButton2.setText(_translate("MainWindow", "添加"))
        self.process_pushButton3.setText(_translate("MainWindow", "處理"))
        self.label_15.setText(_translate("MainWindow", "水平位置"))
        self.label_14.setText(_translate("MainWindow", "實際成品寬"))
        self.label_16.setText(_translate("MainWindow", "垂直位置"))
        self.label_13.setText(_translate("MainWindow", "實際成品高"))
        self.checkBox1.setText(_translate("MainWindow", "雙面打印"))
        self.frame_bleeding.setToolTip(_translate("MainWindow", "出血位"))
        self.label_18.setText(_translate("MainWindow", "下邊增減"))
        self.label_17.setText(_translate("MainWindow", "右邊增減"))
        self.label_19.setText(_translate("MainWindow", "補數檔案"))
        self.open_pushButton1.setText(_translate("MainWindow", "打開需排版PDF檔"))
        self.label_21.setText(_translate("MainWindow", "PDF角度"))
        self.comboBox_rotate.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_rotate.setItemText(1, _translate("MainWindow", "90"))
        self.comboBox_rotate.setItemText(2, _translate("MainWindow", "180"))
        self.comboBox_rotate.setItemText(3, _translate("MainWindow", "270"))
        self.lineEdit_Repeat.setText(_translate("MainWindow", "1"))
        self.checkBox_blank2.setText(_translate("MainWindow", "單面加稿件底頁"))
        self.checkBox_blank.setText(_translate("MainWindow", "加隔紙"))
        self.checkBox_addpage.setText(_translate("MainWindow", "加頁碼"))
        self.label_22.setText(_translate("MainWindow", "重復數量"))
        self.label_art.setText(_translate("MainWindow", "no_art"))
        self.lineEdit_StartSeq.setText(_translate("MainWindow", "1"))
        self.label_23.setText(_translate("MainWindow", "開始編號"))
        self.OpenExcel.setText(_translate("MainWindow", "打開 Excel 檔"))
        self.menu.setTitle(_translate("MainWindow", "功能選項"))
        self.action_importxls.setText(_translate("MainWindow", "顯示補數編號"))
        self.action_output.setText(_translate("MainWindow", "修改輸出PDF路徑"))
        self.action2.setText(_translate("MainWindow", "修改右邊和下邊出血位"))
        self.action2.setIconText(_translate("MainWindow", "修改右邊和下邊出血位"))
        self.action_dele.setText(_translate("MainWindow", "刪除行"))
import resourcefile_rc
