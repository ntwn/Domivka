# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 729)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-radius: 5px;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setStyleSheet("#full_menu_widget {background-color: #286465;\n"
"        border-top-right-radius: 0;\n"
"        border-bottom-right-radius: 0;}\n"
"\n"
"#full_menu_widget QPushButton {\n"
"        border:none;\n"
"        border-radius: 3px;\n"
"        text-align: left;\n"
"        padding: 8px 0 8px 10px;\n"
"        background-color:#286465;\n"
"        color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"#full_menu_widget QPushButton:hover {\n"
"        background-color: rgba(86, 101, 115, 0.5);\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:checked {\n"
"        color: #fff;\n"
"        font: 12pt \"Gotham Pro\";\n"
"    }")
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setStyleSheet("#logo_label_2 {\n"
"        padding: 5px;\n"
"        color: #fff;\n"
"        background-color:#286465;\n"
"    }")
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setStyleSheet("#logo_label_3 {\n"
"        padding-right: 10px;\n"
"        color: #fff;\n"
"        background-color:#286465;\n"
"    }")
        self.logo_label_3.setTextFormat(QtCore.Qt.PlainText)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.main_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.main_btn_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.main_btn_2.setIcon(icon1)
        self.main_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.main_btn_2.setCheckable(True)
        self.main_btn_2.setAutoExclusive(True)
        self.main_btn_2.setObjectName("main_btn_2")
        self.verticalLayout_5.addWidget(self.main_btn_2)
        self.results_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.results_btn_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.results_btn_2.setIcon(icon2)
        self.results_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.results_btn_2.setCheckable(True)
        self.results_btn_2.setAutoExclusive(True)
        self.results_btn_2.setObjectName("results_btn_2")
        self.verticalLayout_5.addWidget(self.results_btn_2)
        self.archive_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.archive_btn_2.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.archive_btn_2.setIcon(icon3)
        self.archive_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.archive_btn_2.setCheckable(True)
        self.archive_btn_2.setAutoExclusive(True)
        self.archive_btn_2.setObjectName("archive_btn_2")
        self.verticalLayout_5.addWidget(self.archive_btn_2)
        self.co_owners_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.co_owners_btn_2.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.co_owners_btn_2.setIcon(icon4)
        self.co_owners_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.co_owners_btn_2.setCheckable(True)
        self.co_owners_btn_2.setAutoExclusive(True)
        self.co_owners_btn_2.setObjectName("co_owners_btn_2")
        self.verticalLayout_5.addWidget(self.co_owners_btn_2)
        self.counters_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.counters_btn_2.setFont(font)
        self.counters_btn_2.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.counters_btn_2.setIcon(icon5)
        self.counters_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.counters_btn_2.setCheckable(True)
        self.counters_btn_2.setAutoExclusive(True)
        self.counters_btn_2.setObjectName("counters_btn_2")
        self.verticalLayout_5.addWidget(self.counters_btn_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn_2.setFont(font)
        self.exit_btn_2.setStyleSheet("padding: 10px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_2.setIcon(icon6)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_2.addWidget(self.exit_btn_2)
        self.gridLayout_10.addWidget(self.full_menu_widget, 0, 1, 2, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setStyleSheet("#maximized_btn {margin-bottom: 10px;}\n"
"\n"
"#normalize_btn {margin-bottom: 10px;}\n"
"\n"
"#hide_btn {margin-bottom: 10px;}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_btn = QtWidgets.QPushButton(self.widget_4)
        self.change_btn.setStyleSheet("padding: 5px;\n"
"border: none;\n"
"width: 30px;\n"
"height: 30px;")
        self.change_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/menu-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon7)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout.addWidget(self.change_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.search_input = QtWidgets.QLineEdit(self.widget_4)
        self.search_input.setStyleSheet("#search_input {\n"
"        border: none;\n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"#search_input:focus {\n"
"        background-color: #70B9FE;\n"
"    }")
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget_4)
        self.search_btn.setStyleSheet("#search_btn {    border: none;\n"
"}")
        self.search_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.search_btn.setIcon(icon8)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.hide_btn = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.hide_btn.setFont(font)
        self.hide_btn.setObjectName("hide_btn")
        self.horizontalLayout.addWidget(self.hide_btn)
        self.normalize_btn = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalize_btn.sizePolicy().hasHeightForWidth())
        self.normalize_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(15)
        self.normalize_btn.setFont(font)
        self.normalize_btn.setStyleSheet("")
        self.normalize_btn.setObjectName("normalize_btn")
        self.horizontalLayout.addWidget(self.normalize_btn)
        self.maximized_btn = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(17)
        self.maximized_btn.setFont(font)
        self.maximized_btn.setObjectName("maximized_btn")
        self.horizontalLayout.addWidget(self.maximized_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget_4, 0, 2, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setStyleSheet("#widget_2 QPushButton:hover {\n"
"    background-color: #286465;\n"
"    color: #fff;\n"
"    }\n"
"\n"
"#widget_2 QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"    }\n"
"\n"
"#widget_2 QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #ffffff;\n"
"    background-color:#ededed;\n"
"    /* border:1px solid #dcdcdc;*/\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#777777;\n"
"    font: 75 12pt \"Century Gothic\";\n"
"    font-weight:bold;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 3px 0px #ffffff;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_9.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.open_unit_btn = QtWidgets.QPushButton(self.widget_2)
        self.open_unit_btn.setMinimumSize(QtCore.QSize(200, 70))
        self.open_unit_btn.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.open_unit_btn.setFont(font)
        self.open_unit_btn.setStyleSheet("")
        self.open_unit_btn.setObjectName("open_unit_btn")
        self.gridLayout_9.addWidget(self.open_unit_btn, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 1)
        self.new_unit_btn = QtWidgets.QPushButton(self.widget_2)
        self.new_unit_btn.setMinimumSize(QtCore.QSize(200, 70))
        self.new_unit_btn.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.new_unit_btn.setFont(font)
        self.new_unit_btn.setStyleSheet("")
        self.new_unit_btn.setObjectName("new_unit_btn")
        self.gridLayout_9.addWidget(self.new_unit_btn, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem4, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.results_label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.results_label.setFont(font)
        self.results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.results_label.setObjectName("results_label")
        self.verticalLayout_6.addWidget(self.results_label)
        self.tableView = QtWidgets.QTableView(self.widget_5)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_6.addWidget(self.tableView)
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.back_button_results = QtWidgets.QPushButton(self.widget)
        self.back_button_results.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.back_button_results.setFont(font)
        self.back_button_results.setObjectName("back_button_results")
        self.gridLayout_8.addWidget(self.back_button_results, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(556, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 1, 2, 1)
        self.verticalLayout_6.addWidget(self.widget)
        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.archive_label = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.archive_label.setFont(font)
        self.archive_label.setAlignment(QtCore.Qt.AlignCenter)
        self.archive_label.setObjectName("archive_label")
        self.gridLayout_4.addWidget(self.archive_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.co_owners_label = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.co_owners_label.setFont(font)
        self.co_owners_label.setAlignment(QtCore.Qt.AlignCenter)
        self.co_owners_label.setObjectName("co_owners_label")
        self.gridLayout_5.addWidget(self.co_owners_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.counters_label = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.counters_label.setFont(font)
        self.counters_label.setAlignment(QtCore.Qt.AlignCenter)
        self.counters_label.setObjectName("counters_label")
        self.gridLayout_6.addWidget(self.counters_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.search_label = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.search_label.setFont(font)
        self.search_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_label.setObjectName("search_label")
        self.gridLayout_7.addWidget(self.search_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.gridLayout_10.addWidget(self.widget_3, 1, 2, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("#icon_only_widget {background-color: #286465;\n"
"        width:50px;\n"
"        border-top-right-radius: 0;\n"
"        border-bottom-right-radius: 0;}\n"
"\n"
"#icon_only_widget QPushButton, QLabel {\n"
"        height:50px;\n"
"        border:none;\n"
"    }\n"
"\n"
"#icon_only_widget QPushButton {\n"
"     background-color:#286465;\n"
"}\n"
"\n"
"#icon_only_widget QPushButton:hover {background-color: rgba( 86, 101, 115, 0.5);}\n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setStyleSheet("padding: 5px;\n"
"background-color:#286465;")
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.verticalLayout_4.addWidget(self.logo_label_1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.main_btn_1.setStyleSheet("")
        self.main_btn_1.setText("")
        self.main_btn_1.setIcon(icon1)
        self.main_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.main_btn_1.setCheckable(True)
        self.main_btn_1.setAutoExclusive(True)
        self.main_btn_1.setObjectName("main_btn_1")
        self.verticalLayout_3.addWidget(self.main_btn_1)
        self.results_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.results_btn_1.setStyleSheet("")
        self.results_btn_1.setText("")
        self.results_btn_1.setIcon(icon2)
        self.results_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.results_btn_1.setCheckable(True)
        self.results_btn_1.setAutoExclusive(True)
        self.results_btn_1.setObjectName("results_btn_1")
        self.verticalLayout_3.addWidget(self.results_btn_1)
        self.archive_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.archive_btn_1.setStyleSheet("")
        self.archive_btn_1.setText("")
        self.archive_btn_1.setIcon(icon3)
        self.archive_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.archive_btn_1.setCheckable(True)
        self.archive_btn_1.setAutoExclusive(True)
        self.archive_btn_1.setObjectName("archive_btn_1")
        self.verticalLayout_3.addWidget(self.archive_btn_1)
        self.co_owners_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.co_owners_btn_1.setStyleSheet("")
        self.co_owners_btn_1.setText("")
        self.co_owners_btn_1.setIcon(icon4)
        self.co_owners_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.co_owners_btn_1.setCheckable(True)
        self.co_owners_btn_1.setAutoExclusive(True)
        self.co_owners_btn_1.setObjectName("co_owners_btn_1")
        self.verticalLayout_3.addWidget(self.co_owners_btn_1)
        self.counters_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.counters_btn_1.setStyleSheet("")
        self.counters_btn_1.setText("")
        self.counters_btn_1.setIcon(icon5)
        self.counters_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.counters_btn_1.setCheckable(True)
        self.counters_btn_1.setAutoExclusive(True)
        self.counters_btn_1.setObjectName("counters_btn_1")
        self.verticalLayout_3.addWidget(self.counters_btn_1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIcon(icon6)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_4.addWidget(self.exit_btn_1)
        self.gridLayout_10.addWidget(self.icon_only_widget, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.main_btn_1.toggled['bool'].connect(self.main_btn_2.setChecked) # type: ignore
        self.results_btn_1.toggled['bool'].connect(self.results_btn_2.setChecked) # type: ignore
        self.archive_btn_1.toggled['bool'].connect(self.archive_btn_2.setChecked) # type: ignore
        self.co_owners_btn_1.toggled['bool'].connect(self.co_owners_btn_2.setChecked) # type: ignore
        self.counters_btn_1.toggled['bool'].connect(self.counters_btn_2.setChecked) # type: ignore
        self.main_btn_2.toggled['bool'].connect(self.main_btn_1.setChecked) # type: ignore
        self.results_btn_2.toggled['bool'].connect(self.results_btn_1.setChecked) # type: ignore
        self.archive_btn_2.toggled['bool'].connect(self.archive_btn_1.setChecked) # type: ignore
        self.co_owners_btn_2.toggled['bool'].connect(self.co_owners_btn_1.setChecked) # type: ignore
        self.counters_btn_2.toggled['bool'].connect(self.counters_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.maximized_btn.clicked.connect(MainWindow.showMaximized) # type: ignore
        self.normalize_btn.clicked.connect(MainWindow.showNormal) # type: ignore
        self.hide_btn.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Домівка"))
        self.logo_label_3.setText(_translate("MainWindow", "Домівка"))
        self.main_btn_2.setText(_translate("MainWindow", "Головна"))
        self.results_btn_2.setText(_translate("MainWindow", "Результати"))
        self.archive_btn_2.setText(_translate("MainWindow", "Архів"))
        self.co_owners_btn_2.setText(_translate("MainWindow", "Співвласники"))
        self.counters_btn_2.setText(_translate("MainWindow", "Лічильники"))
        self.exit_btn_2.setText(_translate("MainWindow", "Закрити"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.hide_btn.setText(_translate("MainWindow", " __ "))
        self.normalize_btn.setText(_translate("MainWindow", ""))
        self.maximized_btn.setText(_translate("MainWindow", ""))
        self.open_unit_btn.setText(_translate("MainWindow", "ОСББ \"Варшавська 15 \""))
        self.new_unit_btn.setText(_translate("MainWindow", "Створити будинок"))
        self.results_label.setText(_translate("MainWindow", "Результати"))
        self.back_button_results.setText(_translate("MainWindow", "Закрити будинок"))
        self.archive_label.setText(_translate("MainWindow", "Архів"))
        self.co_owners_label.setText(_translate("MainWindow", "Співвласники"))
        self.counters_label.setText(_translate("MainWindow", "Лічильники"))
        self.search_label.setText(_translate("MainWindow", "Search Page"))
