import os
import json


class SettingsModel:
    def __init__(self):
        self.startup_enabled = False
        self.startup_minimized = False
        self.tray_enabled = False
        self.set_settings_file()
        self.load_settings()

    def set_settings_file(self):
        """Определяет папку и файл настроек."""
        self.settings_folder = os.path.join(os.path.expanduser("~"),
                                             "Documents", 
                                             "QuickAccessUtility")
        self.settings_file = os.path.join(self.settings_folder, "settings.json")

    def save_settings(self):
        """Сохраняет настройки."""
        settings = {
            "startup_enabled": self.startup_enabled,
            "startup_minimized": self.startup_minimized,
            "tray_enabled": self.tray_enabled
        }

    def load_settings(self):
        """Загружает настройки."""
        pass
