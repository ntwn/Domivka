import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QFile, QTextStream, QPoint, Qt, QAbstractTableModel
import operation_for_db
from algor_main_window import MainWindow
from UI.main_window_ui import Ui_MainWindow


class PersonTable(MainWindow):
    def __init__(self):
        super(PersonTable).__init__()
        self.initUI()
        self.ui.confirm_create_person_buttonBox.clicked.connect(self.create_new_person)

    def initUI(self):
        pass

    def create_list_person(self):
        current_unit = operation_for_db.SQLiteDBPerson(unit_number=self.find_current_unit_id())
        model = PersonTableView(current_unit.select_list_person().fetchall())
        self.ui.person_table_view.setModel(model)
        self.person_table_setting()

    def person_table_setting(self):
        # Отримання заголовка
        header_table = self.ui.person_table_view.horizontalHeader()
        header_table.setSectionResizeMode(QHeaderView.Stretch)

        # Шрифт
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        header_table.setFont(font)

    def create_new_person(self, button):
        if button.text() == '&Yes':
            print("Натиснуто кнопку OK")
        elif button.text() == 'Cancel':
            print("Натиснуто кнопку Cancel")

    def edit_person(self, button):
        if button.text() == '&Yes':
            print("Натиснуто кнопку OK")
        elif button.text() == 'Cancel':
            print("Натиснуто кнопку Cancel")

    def delete_person(self, button):
        if button.text() == '&Yes':
            print("Натиснуто кнопку OK")
        elif button.text() == 'Cancel':
            print("Натиснуто кнопку Cancel")


class PersonTableView(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 7

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ["Квартира", "Прізвище", "Ім'я", "По батькові", "Документ", "Площа", "Квитанція"][section]
            # else:
            #     return str(section)
