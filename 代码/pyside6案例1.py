import sys  # 导入系统模块，用于接收命令行参数和返回程序退出状态码

from PySide6.QtCore import Slot  # 导入槽装饰器，用于标记按钮触发的处理方法
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget  # 导入 PySide6 应用、主窗口、标签、按钮、布局和容器控件


class MainWindowDemo(QMainWindow):  # 定义一个使用 QMainWindow 的 PySide6 主窗口示例类
    def __init__(self):  # 初始化主窗口及其中央界面
        super().__init__()  # 调用父类 QMainWindow 的初始化方法
        self.setWindowTitle("PySide6 主窗口示例")  # 设置主窗口标题
        self.resize(420, 240)  # 设置主窗口初始宽度和高度

        central_widget = QWidget()  # 创建主窗口必须承载内容的中央容器控件
        self.setCentralWidget(central_widget)  # 将中央容器设置为主窗口的中心区域

        self.tip_label = QLabel("这是一个由 QMainWindow 管理的 PySide6 窗口。")  # 创建说明主窗口结构的标签控件
        self.status_button = QPushButton("更新状态栏")  # 创建用于触发状态栏变化的按钮控件

        layout = QVBoxLayout()  # 创建垂直布局，使中央控件自动上下排列
        layout.addWidget(self.tip_label)  # 将说明标签加入垂直布局
        layout.addWidget(self.status_button)  # 将状态栏按钮加入垂直布局
        central_widget.setLayout(layout)  # 将布局设置为中央容器的主布局

        self.statusBar().showMessage("程序已启动")  # 在主窗口自带的状态栏显示初始状态信息
        self.status_button.clicked.connect(self.update_status)  # 将按钮点击信号连接到更新状态栏的槽函数

    @Slot()  # 声明下面的方法是一个不接收参数的 Qt 槽函数
    def update_status(self):  # 定义更新窗口状态栏的交互方法
        self.statusBar().showMessage("按钮已点击，状态栏已更新。")  # 在状态栏显示用户操作后的反馈文字


if __name__ == "__main__":  # 仅在直接运行本文件时启动图形界面程序
    app = QApplication(sys.argv)  # 创建 PySide6 应用程序对象并接收命令行参数
    window = MainWindowDemo()  # 创建主窗口示例对象
    window.show()  # 显示主窗口
    sys.exit(app.exec())  # 启动事件循环，并在关闭窗口后正常退出程序
