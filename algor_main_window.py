import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QFile, QTextStream, QPoint
from time import sleep
import algor_login_window
import operation_for_db

from UI.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.unit_button = None

        # Стартовий стан дадатку
        self.initial_state()

        # прозорість фону та приховування верхньої панелі вікна авторизацій
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # відсілковування кнопок на клавіатурі
        self.keyPressEvent = self.on_search_key_press_event

        # Для формування списку буддинків
        self.units_build = operation_for_db.SQLiteDBUnits()
        self.create_unit()

        self.ui.new_unit_btn.clicked.connect(self.on_clicked_unit)

        # Маніпуляції з вікном
        self.ui.maximized_btn.clicked.connect(self.on_maximized_btn_clicked)
        self.ui.normalize_btn.clicked.connect(self.on_normalize_btn_clicked)
        self.ui.normalize_btn.hide()

        self.ui.close_unit_btn.clicked.connect(self.initial_state)

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

    def find_unit(self):
        if self.units_build.select_units():
            self.ui.new_unit_btn.setMinimumSize(QtCore.QSize(16777215, 10))
            self.ui.new_unit_btn.setStyleSheet('font-size: 11px; margin: 0 9px;')
        for unit in self.units_build.select_units().fetchall():
            yield unit

    def create_unit(self):
        for unit in self.find_unit():
            unit_button = QPushButton(self)
            unit_button.setMinimumSize(QtCore.QSize(200, 70))
            unit_button.setMaximumSize(QtCore.QSize(200, 70))
            unit_button.setObjectName(f"build_{unit[0]}")
            unit_button.setText(f'{unit[1]}')
            self.ui.verticalLayout_8.addWidget(unit_button)
            unit_button.clicked.connect(lambda: self.on_clicked_unit(unit_button.text()))

    def on_clicked_unit(self, button_text):
        self.ui.main_btn_1.hide()
        self.ui.main_btn_2.hide()
        self.ui.set_unit_btn_1.show()
        self.ui.set_unit_btn_2.show()
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.main_btn_2.setChecked(False)
        self.ui.set_unit_btn_2.setChecked(True)
        self.ui.unit_name_label.setText(f'{button_text}')
        self.on_open_unit_btn()

    def initial_state(self):
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.main_btn_2.setChecked(True)
        self.ui.main_btn_1.show()
        self.ui.main_btn_2.show()
        self.ui.set_unit_btn_1.hide()
        self.ui.set_unit_btn_2.hide()
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

    # Функція дозволяє зробити активними 2 кнопки, що мають індекси 5 та 6 (в даному випадку)
    # def on_stackedWidget_currentChanged(self, index):
    #     btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
    #                 + self.ui.full_menu_widget.findChildren(QPushButton)
    #
    #     for btn in btn_list:
    #         if index in [5, 6]:
    #             btn.setAutoExclusive(False)
    #             btn.setChecked(False)
    #         else:
    #             btn.setAutoExclusive(True)

    # functions for changing menu page
    def on_main_btn_1_toggled(self, index):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_main_btn_2_toggled(self, index):
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

    def on_set_unit_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_set_unit_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
