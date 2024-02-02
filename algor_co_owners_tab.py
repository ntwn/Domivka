import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QMainWindow, QTableWidgetItem
import operation_for_db
import algor_main_window

class PersonTable(QWidget):
    def __init__(self, id_unit=1):
        super().__init__()
        self.initUI()
        self.id_unit = id_unit

    def initUI(self):
        self.setWindowTitle("Формування таблиці з SQLite")
        self.resize(800, 600)

        # Створення QTableWidget
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Ім'я", "Вік", "Місто"])

        # Заповнення таблиці даними з SQLite
        self.create_list_person()

        # Додавання QTableWidget до QVBoxLayout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def create_list_person(self):

        current_unit = operation_for_db.SQLiteDBPerson(unit_number=algor_main_window.MainWindow.find_current_unit_id(self.id_unit))

        for row_data in current_unit.select_list_person().fetchall():
            row = self.ui.person_table_view.rowCount()
            self.ui.person_table_view.insertRow(row)
            for column, data in enumerate(row_data):
                self.ui.person_table_view.setItem(row, column, QTableWidgetItem(str(data)))

        # Встановлення розміру стовпчиків
        self.table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PersonTable()
    ex.show()
    sys.exit(app.exec_())