import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QFile, QTextStream, QPoint

import algor_login_window
import algor_main_window

from UI.user_form_ui import Ui_UserForm
from UI.delete_user_form_ui import Ui_DeleteUserForm

import UI.resource_rc


class UserForm(QMainWindow):
    def __init__(self):
        super(UserForm, self).__init__()

        self.ui = Ui_UserForm()
        self.ui.setupUi(self)

        # f_name = user_module.User('Netwin')
        # self.uiU.f_name_output.setText(f'{f_name.user_f_name()}')
        self.ui.widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.delete_user_button.clicked.connect(self.on_clicked_delete_user_button)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def on_clicked_delete_user_button(self):
        delete_user_form.show()
        # x = input('точно? Y/n')
        # if x == 'Y':
        #     user_form.hide()
        #     main_window.hide()
        #     cur_user = user_module.User(login=f'{login_window.ui.login_input.text()}')
        #     cur_user.delete_current_user()
        #     login_window.show()

    def change_user_password(self):
        ...

    def change_user_f_l_name(self):
        ...

    def change_user_email(self):
        ...

    def change_user_phone(self):
        ...


class DeleteUserForm(QtWidgets.QDialog):

    def __init__(self):
        super(DeleteUserForm, self).__init__()

        self.ui = Ui_DeleteUserForm()
        self.ui.setupUi(self)
        self.setModal(True)

        self.ui.widget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = QtWidgets.QApplication(sys.argv)

    login_window = algor_login_window.LoginWindow()
    login_window.show()

    user_form = UserForm()
    delete_user_form = DeleteUserForm()

    sys.exit(app.exec_())
