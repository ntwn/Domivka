# def valid_email(email):
#     return re.match(EMAIL_REGEX, email) is not None
#
# EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+"
#
# email = "john.doe@example.com"
#
# if valid_email(email):
#     print("Email address is valid")
# else:
#     print("Email address is invalid")

#
# import email_validator
#
# email = "john.doe@gmail.com"
#
# # print(email_validator.validate_email(email))
# if email_validator.validate_email(email):
#     print("Email address is valid")
# else:
#     print("Email address is invalid")

# import sys
# import sqlite3
# from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QHeaderView, QVBoxLayout, QTableWidgetItem
#
#
#
# import sys
# import sqlite3
# from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout
# from PyQt5.QtCore import QAbstractTableModel, Qt

# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data
#
#     def rowCount(self, parent=None):
#         return len(self._data)
#
#     def columnCount(self, parent=None):
#         return len(self._data[0])
#
#     def data(self, index, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole:
#             return self._data[index.row()][index.column()]
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Формування таблиці з SQLite")
#         self.resize(800, 600)
#
#         # Створення QTableView
#         self.table = QTableView()
#
#         # Створення моделі даних
#         model = MyTableModel(self.get_data())
#         self.table.setModel(model)
#
#         # Додавання QTableView до QVBoxLayout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         self.setLayout(layout)
#
#     def get_data(self):
#         # Створення з'єднання з SQLite
#         connection = sqlite3.connect("data/database.db")
#         cursor = connection.cursor()
#
#         # Запит даних з таблиці
#         query = "SELECT first_name, last_name, father_name FROM person"
#         cursor.execute(query)
#
#         # Отримання даних
#         data = cursor.fetchall()
#
#         # Закриття з'єднання з SQLite
#         cursor.close()
#         connection.close()
#
#         return data
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     ex.show()
#     sys.exit(app.exec_())



#----------------------------------------------------------------
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Формування таблиці з SQLite")
#         self.resize(800, 600)
#
#         # Створення QTableWidget
#         self.table = QTableWidget()
#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(["Ім'я", "Вік", "Місто"])
#
#         # Заповнення таблиці даними з SQLite
#         self.populate_table()
#
#         # Додавання QTableWidget до QVBoxLayout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         self.setLayout(layout)
#
#     def populate_table(self):
#         # Створення з'єднання з SQLite
#         connection = sqlite3.connect("data/database.db")
#         cursor = connection.cursor()
#
#         # Запит даних з таблиці
#         query = "SELECT first_name, last_name, father_name FROM person"
#         cursor.execute(query)
#
#         # Заповнення рядків таблиці
#         for row_data in cursor.fetchall():
#             row = self.table.rowrowCount()
#             self.table.insertRow(row)
#             for column, data in enumerate(row_data):
#                 self.table.setItem(row, column, QTableWidgetItem(str(data)))
#
#         # Встановлення розміру стовпчиків
#         self.table.resizeColumnsToContents()
#
#         # Закриття з'єднання з SQLite
#         cursor.close()
#         connection.close()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     ex.show()
#     sys.exit(app.exec_())
