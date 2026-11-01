import sys  # 导入系统模块，用于传入命令行参数并返回程序退出状态码（sys模块负责与python解释器交互）

from PySide6.QtCore import Slot  # 导入槽装饰器，用于标记按钮点击后的处理函数
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget  # 导入 PySide6 应用、标签、按钮、布局和基础窗口控件


class FirstPySideWindow(QWidget):  # 定义一个继承 QWidget 的第一个 PySide6 窗口类
    def __init__(self):  # 初始化窗口及其中的界面控件
        super().__init__()  # 调用父类 QWidget 的初始化方法
        self.setWindowTitle("我的第一个 PySide6 程序")  # 设置窗口标题，说明当前示例使用 PySide6
        self.resize(360, 180)  # 设置窗口初始宽度和高度

        self.message_label = QLabel("欢迎学习 PySide6！")  # 创建用于显示提示文字的标签控件
        self.click_button = QPushButton("点击我")  # 创建可被用户点击的按钮控件

        layout = QVBoxLayout()  # 创建垂直布局，让控件自动从上到下排列
        layout.addWidget(self.message_label)  # 将提示标签加入垂直布局
        layout.addWidget(self.click_button)  # 将按钮加入垂直布局
        self.setLayout(layout)  # 将垂直布局设置为窗口的主布局

        self.click_button.clicked.connect(self.change_message)  # 将按钮的点击信号连接到文字更新槽函数

    @Slot()  # 声明下面的方法是一个不接收参数的 Qt 槽函数
    def change_message(self):  # 定义用户点击按钮后执行的交互逻辑
        self.message_label.setText("按钮已点击：PySide6 可以响应用户操作！")  # 更新标签文字以反馈按钮点击结果


if __name__ == "__main__":  # 仅在直接运行本文件时启动图形界面程序
    app = QApplication(sys.argv)  # 创建并初始化整个 PySide6 应用程序对象
    window = FirstPySideWindow()  # 创建第一个 PySide6 窗口对象
    window.show()  # 将窗口显示到屏幕上
    sys.exit(app.exec())  # 启动事件循环，并在窗口关闭后把退出状态返回给系统
