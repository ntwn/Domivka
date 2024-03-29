# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\user_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(886, 700)
        UserForm.setMinimumSize(QtCore.QSize(886, 700))
        UserForm.setMaximumSize(QtCore.QSize(886, 700))
        self.widget = QtWidgets.QWidget(UserForm)
        self.widget.setGeometry(QtCore.QRect(248, 120, 300, 460))
        self.widget.setMinimumSize(QtCore.QSize(300, 460))
        self.widget.setMaximumSize(QtCore.QSize(300, 460))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_button.setFont(font)
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_button.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(139, 139, 139);\n"
"padding-top: 7px;")
        self.close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QtCore.QSize(14, 14))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_5.addWidget(self.close_button)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setStyleSheet("border-image: url(:/avatar/avatar/men_anonim_avatar.svg);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.f_name_output = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.f_name_output.setFont(font)
        self.f_name_output.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.f_name_output.setStyleSheet("padding-right: 3px;")
        self.f_name_output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f_name_output.setObjectName("f_name_output")
        self.horizontalLayout.addWidget(self.f_name_output)
        self.l_name_output = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l_name_output.setFont(font)
        self.l_name_output.setStyleSheet("padding-left: 3px;")
        self.l_name_output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l_name_output.setObjectName("l_name_output")
        self.horizontalLayout.addWidget(self.l_name_output)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.change_f_l_name_password_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.change_f_l_name_password_button.setFont(font)
        self.change_f_l_name_password_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgba(0, 0, 0, 200);")
        self.change_f_l_name_password_button.setObjectName("change_f_l_name_password_button")
        self.horizontalLayout_4.addWidget(self.change_f_l_name_password_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.phone_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("color: rgba(190, 120, 0, 200);")
        self.phone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_label.setObjectName("phone_label")
        self.verticalLayout_2.addWidget(self.phone_label)
        self.phone_output = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.phone_output.setFont(font)
        self.phone_output.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_output.setObjectName("phone_output")
        self.verticalLayout_2.addWidget(self.phone_output)
        self.email_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color: rgba(190, 120, 0, 200);")
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.verticalLayout_2.addWidget(self.email_label)
        self.email_output = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.email_output.setFont(font)
        self.email_output.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email_output.setAlignment(QtCore.Qt.AlignCenter)
        self.email_output.setObjectName("email_output")
        self.verticalLayout_2.addWidget(self.email_output)
        self.change_email_phone_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.change_email_phone_button.setFont(font)
        self.change_email_phone_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.change_email_phone_button.setObjectName("change_email_phone_button")
        self.verticalLayout_2.addWidget(self.change_email_phone_button)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete_user_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.delete_user_button.setFont(font)
        self.delete_user_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_user_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgba(190, 0, 0, 230);\n"
"padding-bottom: 10px;")
        self.delete_user_button.setObjectName("delete_user_button")
        self.horizontalLayout_3.addWidget(self.delete_user_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.login_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"padding-bottom: 10px;")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.horizontalLayout_3.addWidget(self.login_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.retranslateUi(UserForm)
        self.close_button.clicked.connect(UserForm.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(UserForm)

    def retranslateUi(self, UserForm):
        _translate = QtCore.QCoreApplication.translate
        UserForm.setWindowTitle(_translate("UserForm", "Form"))
        self.f_name_output.setText(_translate("UserForm", "Власне Ім\'я"))
        self.l_name_output.setText(_translate("UserForm", "Прізвище"))
        self.change_f_l_name_password_button.setText(_translate("UserForm", "Змінити дані/пароль"))
        self.phone_label.setText(_translate("UserForm", "мобільний номер"))
        self.phone_output.setText(_translate("UserForm", "+380 97 000 00 00"))
        self.email_label.setText(_translate("UserForm", "електрона пошта"))
        self.email_output.setText(_translate("UserForm", "exemple@gmail.com"))
        self.change_email_phone_button.setText(_translate("UserForm", "Змінити номер та email"))
        self.delete_user_button.setText(_translate("UserForm", "Видалити користувача"))
        self.login_label.setText(_translate("UserForm", "login"))
