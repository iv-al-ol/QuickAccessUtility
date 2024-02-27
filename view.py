from PyQt5.QtWidgets import QMainWindow, QCheckBox,\
                            QPushButton, QSystemTrayIcon,\
                            QMenu, QStyle, QAction
from PyQt5.QtGui import QIcon


class SettingsView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quick Access Utility")
        self.setWindowIcon(QIcon('images\\app_icon.ico'))
        self.setGeometry(100, 100, 400, 200)

        self.startup_checkbox = QCheckBox("Запускать приложение при запуске системы", self)
        self.startup_checkbox.setGeometry(10, 10, 350, 30)

        self.minimize_checkbox = QCheckBox("Запускать приложение свернутым", self)
        self.minimize_checkbox.setGeometry(10, 50, 350, 30)

        self.tray_checkbox = QCheckBox("Сворачивать приложение в трей", self)
        self.tray_checkbox.setGeometry(10, 90, 350, 30)

        self.save_button = QPushButton("Сохранить настройки", self)
        self.save_button.setGeometry(10, 130, 150, 30)

        # Создание трея


        # Иконка в трее
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.tray_icon.setToolTip('Quick Access Utility')

        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        #quit_action.triggered.connect(self.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        '''
        # Контекстное меню трея
        self.tray_menu = QMenu()
        self.tray_menu.addAction("Открыть", self.show)
        self.tray_menu.addAction("Закрыть приложение", self.close)

        self.tray_icon.setContextMenu(self.tray_menu)
        '''

    def closeEvent(self, event):
        #if self.check_box.isChecked():
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000)

    def show_message(self, message):
        # Реализация вывода сообщений пользователю
        pass
