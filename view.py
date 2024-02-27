from PyQt5.QtWidgets import QMainWindow, QCheckBox,\
                            QPushButton, QSystemTrayIcon,\
                            QMenu, QStyle, QAction
from PyQt5.QtGui import QIcon


class SettingsView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quick Access Utility")
        self.setWindowIcon(QIcon("images\\app_icon.ico"))
        self.setGeometry(100, 100, 400, 200)

        self.startup_checkbox = QCheckBox("Запускать приложение при запуске системы", self)
        self.startup_checkbox.setGeometry(10, 10, 350, 30)

        self.minimize_checkbox = QCheckBox("Запускать приложение свернутым", self)
        self.minimize_checkbox.setGeometry(10, 50, 350, 30)

        self.tray_checkbox = QCheckBox("Сворачивать приложение в трей", self)
        self.tray_checkbox.setGeometry(10, 90, 350, 30)

        self.save_button = QPushButton("Сохранить настройки", self)
        self.save_button.setGeometry(10, 130, 150, 30)

        # Иконка в трее
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("images\\app_icon.ico"))
        self.tray_icon.setToolTip("Quick Access Utility")

        # События трея
        show_action = QAction("Показать", self)
        hide_action = QAction("Скрыть", self)
        quit_action = QAction("Выйти", self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(exit)

        # Инициализация пунктов меню трея
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        """Переназначение функции закрытия окна для возможности сворачивания."""
        #if self.check_box.isChecked(): Добавить настройку сворачивания приложения в трей
        event.ignore()
        self.hide()
        # Добавить возможность отключения уведомления о сворачивании приложения
        '''
        if model.settings.tray_notification:
            self.tray_icon.showMessage(
                "Quick Access Utility",
                "Приложение свернуто в трей",
                QSystemTrayIcon.Information,
                1000)
        '''

    def show_message(self, message):
        # Реализация вывода сообщений пользователю
        pass
