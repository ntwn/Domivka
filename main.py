import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QFile, QTextStream, QPoint

from UI.main_window_ui import Ui_MainWindow
from UI.login_window_ui import Ui_LoginWindow
from UI.user_form_ui import Ui_UserForm
from UI.delete_user_form_ui import Ui_DeleteUserForm


import operation_for_db
import auth_module as auth_mod
import my_patches
import user_module
import UI.resource_rc


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
        # self.ui.pic2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
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
        self.ui.change_on_registration_button.clicked.connect(self.on_clicked_change_on_registration_button)
        self.ui.change_on_enter_button.clicked.connect(self.on_clicked_change_on_enter_button)

    def on_clicked_change_on_registration_button(self):
        self.ui.change_on_enter_button.setGeometry(QtCore.QRect(490, 85, 110, 20))
        self.ui.change_on_enter_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 12pt \"Century Gothic\";\n"
                                                  "color: rgb(157, 157, 157);\n"
                                                  "border: 0;")
        self.ui.change_on_registration_button.setGeometry(QtCore.QRect(435, 40, 220, 40))
        self.ui.change_on_registration_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 32pt \"Century Gothic\";\n"
                                                  "color: rgb(0, 0, 0);\n"
                                                  "border: 0;")

        self.ui.registration_form.show()
        self.ui.login_form.hide()
        self.ui.message_label.hide()

    def on_clicked_change_on_enter_button(self):
        self.ui.change_on_registration_button.setGeometry(QtCore.QRect(490, 85, 110, 20))
        self.ui.change_on_registration_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 12pt \"Century Gothic\";\n"
                                                  "color: rgb(157, 157, 157);\n"
                                                  "border: 0;")
        self.ui.change_on_enter_button.setGeometry(QtCore.QRect(435, 40, 220, 40))
        self.ui.change_on_enter_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                  "font: 32pt \"Century Gothic\";\n"
                                                  "color: rgb(0, 0, 0);\n"
                                                  "border: 0;")

        self.ui.login_form.show()
        self.ui.registration_form.hide()
        self.ui.message_label_reg.hide()

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
                             user_password=f'{self.ui.password_input.text()}')
        self.ui.message_label.setStyleSheet('color: rgb(230, 0, 0);')
        if user.login() == 'user_not_found':
            self.ui.message_label.setText('Не вірний логін')
        elif user.login() == 'password_not_valid':
            self.ui.message_label.setText('Не вірний пароль')
        else:

            login_window.close()
            # if 'root' in user.login():
            #     print(f'root access required')
            #     main_window.show()
            main_window.show()
            return True

    def on_clicked_registration_button(self):
        self.ui.message_label_reg.show()
        self.ui.message_label_reg.setText('')
        user = auth_mod.Auth(f_user_name=f'{self.ui.f_name_input_reg.text()}',
                             l_user_name=f'{self.ui.l_name_input_reg.text()}',
                             user_login=f'{self.ui.login_input_reg.text()}',
                             user_password=f'{self.ui.password_input_reg.text()}',
                             user_confirm_password=f'{self.ui.password_input_reg_confirm.text()}',
                             user_email=f'{self.ui.email_input_reg.text()}')
        if user.register() == 'chip_login':
            self.ui.message_label_reg.setText('Логін занадто короткий')
        elif user.register() == 'login_exists':
            self.ui.message_label_reg.setText('Такий користувач вже існує')
        elif user.register() == 'chip_password':
            self.ui.message_label_reg.setText('Пароль занадто короткий')
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
            self.on_clicked_change_on_enter_button()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # відсілковування кнопок на клавіатурі
        self.keyPressEvent = self.on_search_key_press_event

        self.ui.maximized_btn.clicked.connect(self.on_maximized_btn_clicked)
        self.ui.normalize_btn.clicked.connect(self.on_normalize_btn_clicked)
        self.ui.normalize_btn.hide()

    # роблю вікно переміщуваним, бо self.setWindowFlags(QtCore.Qt.FramelessWindowHint) забирає таку можливість
    # def mousePressEvent(self, event):
    #     self.oldPosition = event.globalPos()
    #
    # def mouseMoveEvent(self, event):
    #     delta = QPoint(event.globalPos() - self.oldPosition)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.oldPosition = event.globalPos()

    # обробка кнопок (розгорнути/згорнути)
    def on_maximized_btn_clicked(self):
        self.ui.normalize_btn.show()
        self.ui.maximized_btn.hide()

    def on_normalize_btn_clicked(self):
        self.ui.normalize_btn.hide()
        self.ui.maximized_btn.show()

    # Робота з полем пошуку
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip() or ' '
        if search_text:
            self.ui.search_label.setText(search_text)
        return search_text

    def on_search_key_press_event(self, event):
        # Якщо натиснута кнопка ENTER (Треба звернути увагу в майбутньому, код кнопки може відрізнятись)
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == 16777220:
            if self.ui.search_input.hasFocus():
                self.ui.stackedWidget.setCurrentIndex(5)
                self.on_search_btn_clicked()

    # Function for changing page to user pag (відсутня, можливо і не з'виться)
    # def on_user_btn_clicked(self):
    #     self.ui.stackedWidget.setCurrentIndex(6)
    #     cur_user = user_module.User(login=f'{login_window.ui.login_input.text()}')
    #     user_form.ui.f_name_output.setText(''.join(cur_user.user_f_name().fetchone()))
    #     user_form.ui.l_name_output.setText(''.join(cur_user.user_l_name().fetchone()))
    #     user_form.ui.email_output.setText(''.join(cur_user.user_email().fetchone()))
    #     user_form.ui.login_label.setText(f'{login_window.ui.login_input.text()}')
    #     user_form.show()

    # Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    # functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


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
    # loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    # Для логін_вікна стилі в файлі login_window_ui
    # Login_form = QtWidgets.QWidget()
    # ui_login = Ui_LoginWindow()
    # ui_login.setupUi(Login_form)

    # loading style file, Example 2 (для менй вікна стилі в окремому файлі)
    style_file = QFile("UI/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    main_window = MainWindow()
    login_window = LoginWindow()
    login_window.show()
    # main_window.show()
    # if login_window.on_clicked_enter_button():
    user_form = UserForm()
    delete_user_form = DeleteUserForm()
    # delete_user_form.show()
        # user_form.show()
    # user_form = UserForm()
    # main_window.show()
    # user_form.show()

    sys.exit(app.exec_())
