


class SettingsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.startup_checkbox.setChecked(self.model.startup_enabled)
        self.view.minimize_checkbox.setChecked(self.model.startup_minimized)
        self.view.tray_checkbox.setChecked(self.model.tray_enabled)

        self.view.save_button.clicked.connect(self.save_settings)

    def save_settings(self):
        self.model.startup_enabled = self.view.startup_checkbox.isChecked()
        self.model.startup_minimized = self.view.minimize_checkbox.isChecked()
        self.model.tray_enabled = self.view.tray_checkbox.isChecked()

        self.model.save_settings()
        self.view.show_message("Настройки успешно сохранены...")
