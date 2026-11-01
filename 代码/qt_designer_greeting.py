"""Qt Designer 问候小程序：运行时直接加载可编辑的 .ui 文件。"""

import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton


class GreetingApp:
    def __init__(self) -> None:
        ui_path = Path(__file__).with_name("qt_designer_greeting.ui")
        ui_file = QFile(str(ui_path))
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"无法打开界面文件：{ui_path}")

        self.window = QUiLoader().load(ui_file)
        ui_file.close()
        if not isinstance(self.window, QMainWindow):
            raise RuntimeError("Qt Designer 界面加载失败")

        self.name_input = self.window.findChild(QLineEdit, "nameInput")
        self.greet_button = self.window.findChild(QPushButton, "greetButton")
        self.message_label = self.window.findChild(QLabel, "messageLabel")
        if not all((self.name_input, self.greet_button, self.message_label)):
            raise RuntimeError("界面控件名称与程序不一致")

        self.greet_button.clicked.connect(self.show_greeting)
        self.name_input.returnPressed.connect(self.show_greeting)

    def show_greeting(self) -> None:
        name = self.name_input.text().strip() or "同学"
        self.message_label.setText(f"你好，{name}！欢迎使用 Qt Designer。")

    def show(self) -> None:
        self.window.show()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    greeting_app = GreetingApp()
    greeting_app.show()
    sys.exit(application.exec())
