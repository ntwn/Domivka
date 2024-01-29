from time import sleep
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from UI.login_window_ui import Ui_LoginWindow

from my_patches import hash_password
import operation_for_db
import auth_module as auth_mod
import algor_main_window


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.user_registration = None

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # накладення тіні на панелі авторизації
        self.ui.background_field.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0))
        self.ui.enter_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.ui.registration_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.ui.registration_form.hide()

        # обробка кліку на кнопку "Увійти"
        self.ui.enter_button.clicked.connect(self.on_clicked_enter_button)

        # обробка кліку на кнопку "Зареєструватись"
        self.ui.registration_button.clicked.connect(self.on_clicked_registration_button)

        # відсілковування кнопок на клавіатурі
        self.keyPressEvent = self.on_key_press_event

        # обробка кліку на надпис "Реєстрація" та "Вхід"
        self.ui.log_reg_button_group.buttonClicked.connect(self.log_reg_form)

        # Вибір мови
        self.ui.lang_button_group.buttonClicked.connect(self.change_lang)

    def open_reg_form(self):
        self.ui.change_on_registration_button.setGeometry(QtCore.QRect(0, 0, 331, 51))
        self.ui.change_on_enter_button.setGeometry(QtCore.QRect(0, 50, 331, 20))
        self.ui.registration_form.show()
        self.ui.login_form.hide()
        self.ui.message_label.hide()

    def open_login_form(self):
        self.ui.change_on_enter_button.setGeometry(QtCore.QRect(0, 0, 331, 51))
        self.ui.change_on_registration_button.setGeometry(QtCore.QRect(0, 50, 331, 20))
        self.ui.login_form.show()
        self.ui.registration_form.hide()
        self.ui.message_label_reg.hide()

    def log_reg_form(self):
        radio_btn = self.sender()
        if radio_btn.checkedButton().text() in ('ВХІД', 'ENTER'):
            self.open_login_form()
        else:
            self.open_reg_form()

    # Зміна мови, це ппц який костиляка, треба розібратися і зробити гарно
    def change_lang(self):
        radio_btn = self.sender()
        if radio_btn.checkedButton().text() == 'EN':
            self.ui.company_name.setText("Domivka")
            self.ui.company_slogan.setText("Easy to control the house.")
            self.ui.login_input.setPlaceholderText("Login")
            self.ui.password_input.setPlaceholderText("Password")
            self.ui.enter_button.setText("Enter")
            self.ui.forgot_login_password.setText("Forgot login or password?")
            self.ui.password_input_reg_confirm.setPlaceholderText("Confirm password")
            self.ui.l_name_input_reg.setPlaceholderText("Last name")
            self.ui.login_input_reg.setPlaceholderText("Login")
            self.ui.password_input_reg.setPlaceholderText("Password")
            self.ui.f_name_input_reg.setPlaceholderText("First name")
            self.ui.registration_button.setText("Registration")
            self.ui.email_input_reg.setToolTip("<html><head/><body><p/></body></html>")
            self.ui.email_input_reg.setPlaceholderText("Email (not necessarily)")
            self.ui.change_on_registration_button.setText("REGISTRATION")
            self.ui.change_on_enter_button.setText("ENTER")
        else:
            self.ui.company_name.setText("Домівка")
            self.ui.company_slogan.setText("Керуємо будинком з легкістю.")
            self.ui.login_input.setPlaceholderText("Логін користувача")
            self.ui.password_input.setPlaceholderText("Пароль користувача")
            self.ui.enter_button.setText("Увійти")
            self.ui.forgot_login_password.setText("Забули логін чи пароль?")
            self.ui.password_input_reg_confirm.setPlaceholderText("Підтвердити пароль")
            self.ui.l_name_input_reg.setPlaceholderText("Прізвище")
            self.ui.login_input_reg.setPlaceholderText("Логін користувача")
            self.ui.password_input_reg.setPlaceholderText("Пароль")
            self.ui.f_name_input_reg.setPlaceholderText("Ім\'я")
            self.ui.registration_button.setText("Зареєструвати")
            self.ui.email_input_reg.setToolTip("<html><head/><body><p/></body></html>")
            self.ui.email_input_reg.setPlaceholderText("Email (не обов\'язково)")
            self.ui.change_on_registration_button.setText("РЕЄТРАЦІЯ")
            self.ui.change_on_enter_button.setText("ВХІД")

    def on_key_press_event(self, event):
        # Якщо натиснута кнопка Esc
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()
        # Якщо натиснута кнопка ENTER (Треба звернути увагу в майбутньому, код кнопки може відрізнятись)
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == 16777220:
            if self.ui.login_form.isHidden():
                self.on_clicked_registration_button()
            else:
                self.on_clicked_enter_button()

    def on_clicked_enter_button(self):
        self.ui.message_label.show()
        self.ui.message_label.setText('')
        user = auth_mod.Auth(user_login=f'{self.ui.login_input.text()}',
                             user_password=hash_password(f'{self.ui.password_input.text()}'))
        self.ui.message_label.setStyleSheet('color: rgb(230, 0, 0);')
        if user.login() == 'user_not_found':
            self.ui.message_label.setText('Не вірний логін')
        elif user.login() == 'password_not_valid':
            self.ui.message_label.setText('Не вірний пароль')
        else:
            self.close()
            sleep(0.5)
            main_window = algor_main_window.MainWindow()
            main_window.show()
            return True

    def on_clicked_registration_button(self):
        self.ui.message_label_reg.show()
        self.ui.message_label_reg.setText('')
        user = auth_mod.Auth(f_user_name=f'{self.ui.f_name_input_reg.text()}',
                             l_user_name=f'{self.ui.l_name_input_reg.text()}',
                             user_login=f'{self.ui.login_input_reg.text()}',
                             user_password=hash_password(f'{self.ui.password_input_reg.text()}'),
                             user_confirm_password=hash_password(f'{self.ui.password_input_reg_confirm.text()}'),
                             user_email=f'{self.ui.email_input_reg.text()}')
        if len(self.ui.password_input_reg.text()) < 5:
            self.ui.message_label_reg.setText('Пароль занадто короткий')
        elif user.register() == 'chip_login':
            self.ui.message_label_reg.setText('Логін занадто короткий')
        elif user.register() == 'login_exists':
            self.ui.message_label_reg.setText('Такий користувач вже існує')
        elif user.register() == 'wrong_confirm_password':
            self.ui.message_label_reg.setText('Не вірний пароль підтвердження')

        # В майбутньому реалізую сповіщення на пошту і увімкну цю перевірку
        #
        # elif user.register() == 'email_exists':
        #     self.ui.message_label_reg.setText('Такий email вже існує')
        # elif user.register() == 'email_not_valid':
        #     self.ui.message_label_reg.setText('Email не справжній')

        else:
            self.user_registration = operation_for_db.SQLiteDB(select_obj='*',
                                                               table_name='users',
                                                               f_user_name=f'{(self.ui.f_name_input_reg.text() or " ")}',
                                                               l_user_name=f'{(self.ui.l_name_input_reg.text() or " ")}',
                                                               user_login=f'{self.ui.login_input_reg.text()}',
                                                               user_password=f'{user.register()}',
                                                               user_email=f'{(self.ui.email_input_reg.text() or "unknown")}',
                                                               user_role='user')
            self.user_registration.insert_user()
            self.ui.message_label.setStyleSheet('color: rgb(0, 150, 0);')
            self.ui.message_label.setText('Реєстрація успішна! Авторизуйтесь')
            self.ui.message_label.show()
            self.ui.change_on_enter_button.setChecked(True)
            self.open_login_form()
