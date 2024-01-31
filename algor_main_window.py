import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QFile, QTextStream, QPoint
from time import sleep
import algor_login_window

from UI.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.main_btn_2.setChecked(True)

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # відсілковування кнопок на клавіатурі
        self.keyPressEvent = self.on_search_key_press_event

        self.ui.maximized_btn.clicked.connect(self.on_maximized_btn_clicked)
        self.ui.normalize_btn.clicked.connect(self.on_normalize_btn_clicked)
        self.ui.normalize_btn.hide()
        self.initial_state()

        self.ui.back_button_results.clicked.connect(self.initial_state)
        self.ui.open_unit_btn.clicked.connect(self.on_open_unit_btn)


    # роблю вікно переміщуваним, бо self.setWindowFlags(QtCore.Qt.FramelessWindowHint) забирає таку можливість
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    # обробка кнопок (розгорнути/згорнути)
    def on_maximized_btn_clicked(self):
        self.ui.normalize_btn.show()
        self.ui.maximized_btn.hide()

    def on_normalize_btn_clicked(self):
        self.ui.normalize_btn.hide()
        self.ui.maximized_btn.show()


    def initial_state(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.main_btn_2.setChecked(True)
        self.ui.results_btn_1.hide()
        self.ui.results_btn_2.hide()
        self.ui.archive_btn_1.hide()
        self.ui.archive_btn_2.hide()
        self.ui.co_owners_btn_1.hide()
        self.ui.co_owners_btn_2.hide()
        self.ui.counters_btn_1.hide()
        self.ui.counters_btn_2.hide()

    def on_open_unit_btn(self):
        self.ui.results_btn_1.show()
        self.ui.results_btn_2.show()
        self.ui.archive_btn_1.show()
        self.ui.archive_btn_2.show()
        self.ui.co_owners_btn_1.show()
        self.ui.co_owners_btn_2.show()
        self.ui.counters_btn_1.show()
        self.ui.counters_btn_2.show()

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
    def on_main_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_main_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_results_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_results_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_archive_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_archive_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_co_owners_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_co_owners_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_counters_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_counters_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
