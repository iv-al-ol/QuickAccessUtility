from PyQt5.QtWidgets import QApplication
from model import SettingsModel
from view import SettingsView
from controller import SettingsController
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = SettingsModel()
    view = SettingsView()
    controller = SettingsController(model, view)

    view.show()

    sys.exit(app.exec_())
