# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MyLabel import MyLabel
from resource import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 90, 441, 401))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.account_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_lineEdit.setMinimumSize(QtCore.QSize(293, 35))
        self.account_lineEdit.setMaximumSize(QtCore.QSize(293, 16777215))
        self.account_lineEdit.setStyleSheet("font: 14pt \"华文楷体\";")
        self.account_lineEdit.setClearButtonEnabled(True)
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.gridLayout.addWidget(self.account_lineEdit, 0, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setStyleSheet("font: 14pt \"华文楷体\";")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.login_label = QtWidgets.QPushButton(self.layoutWidget)
        self.login_label.setMinimumSize(QtCore.QSize(0, 40))
        self.login_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_label.setStyleSheet("font: 14pt \"华文楷体\";")
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 4, 0, 1, 2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(293, 35))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(293, 16777215))
        self.password_lineEdit.setStyleSheet("font: 14pt \"华文楷体\";")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setClearButtonEnabled(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 1)
        self.picture_label = MyLabel(self.layoutWidget)
        self.picture_label.setMinimumSize(QtCore.QSize(293, 190))
        self.picture_label.setMaximumSize(QtCore.QSize(293, 190))
        self.picture_label.setStyleSheet("font: 14pt \"华文楷体\";\n"
"background-color: rgb(0, 255, 255);")
        self.picture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picture_label.setObjectName("picture_label")
        self.gridLayout.addWidget(self.picture_label, 2, 1, 2, 1)
        self.account_label = QtWidgets.QLabel(self.layoutWidget)
        self.account_label.setStyleSheet("font: 14pt \"华文楷体\";")
        self.account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.account_label.setObjectName("account_label")
        self.gridLayout.addWidget(self.account_label, 0, 0, 1, 1)
        self.refresh_button = QtWidgets.QPushButton(self.layoutWidget)
        self.refresh_button.setMinimumSize(QtCore.QSize(50, 60))
        self.refresh_button.setStyleSheet("font: 14pt \"华文楷体\";")
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout.addWidget(self.refresh_button, 2, 0, 1, 1)
        self.autoSelect_button = QtWidgets.QPushButton(self.layoutWidget)
        self.autoSelect_button.setMinimumSize(QtCore.QSize(50, 60))
        self.autoSelect_button.setStyleSheet("font: 14pt \"华文楷体\";")
        self.autoSelect_button.setObjectName("autoSelect_button")
        self.gridLayout.addWidget(self.autoSelect_button, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 81))
        self.label.setStyleSheet("font: 14pt \"华文楷体\";\n"
"border-image: url(:/image/qiangpiao.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.refresh_button.clicked.connect(MainWindow.reFresh)
        self.autoSelect_button.clicked.connect(MainWindow.autoSelect)
        self.login_label.clicked.connect(MainWindow.login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.account_lineEdit.setPlaceholderText(_translate("MainWindow", "请在此处输入你的12306账号"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_label.setText(_translate("MainWindow", "Login"))
        self.password_lineEdit.setPlaceholderText(_translate("MainWindow", "请在此输入你的12306密码"))
        self.picture_label.setText(_translate("MainWindow", "验证码图片"))
        self.account_label.setText(_translate("MainWindow", "Account"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.autoSelect_button.setText(_translate("MainWindow", "AutoSelect"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

