# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 162)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.le_imap_server = QtWidgets.QLineEdit(Dialog)
        self.le_imap_server.setObjectName("le_imap_server")
        self.gridLayout.addWidget(self.le_imap_server, 1, 0, 1, 1)
        self.le_smtp_server = QtWidgets.QLineEdit(Dialog)
        self.le_smtp_server.setObjectName("le_smtp_server")
        self.gridLayout.addWidget(self.le_smtp_server, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.sp_imap_port = QtWidgets.QSpinBox(Dialog)
        self.sp_imap_port.setMaximum(9999)
        self.sp_imap_port.setObjectName("sp_imap_port")
        self.gridLayout.addWidget(self.sp_imap_port, 3, 0, 1, 1)
        self.sp_smtp_port = QtWidgets.QSpinBox(Dialog)
        self.sp_smtp_port.setMaximum(9999)
        self.sp_smtp_port.setObjectName("sp_smtp_port")
        self.gridLayout.addWidget(self.sp_smtp_port, 3, 1, 1, 1)
        self.cb_ssl = QtWidgets.QCheckBox(Dialog)
        self.cb_ssl.setObjectName("cb_ssl")
        self.gridLayout.addWidget(self.cb_ssl, 4, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_ok = QtWidgets.QPushButton(Dialog)
        self.pb_ok.setObjectName("pb_ok")
        self.horizontalLayout.addWidget(self.pb_ok)
        self.pb_cancel = QtWidgets.QPushButton(Dialog)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout.addWidget(self.pb_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.pb_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройка почтогово сервиса"))
        self.label_1.setText(_translate("Dialog", "Сервер IMAP"))
        self.label_2.setText(_translate("Dialog", "Сервер SMTP"))
        self.label_3.setText(_translate("Dialog", "Порт IMAP"))
        self.label_4.setText(_translate("Dialog", "Порт SMTP"))
        self.cb_ssl.setText(_translate("Dialog", "Использовать SSL"))
        self.pb_ok.setText(_translate("Dialog", "OK"))
        self.pb_cancel.setText(_translate("Dialog", "Отмена"))

