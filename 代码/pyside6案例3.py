import sys  # 导入系统模块，用于传入命令行参数并正常退出程序

from PySide6.QtCore import Slot  # 导入槽装饰器，用于标记按钮点击后的计算方法
from PySide6.QtWidgets import (  # 导入创建成绩计算器所需的 PySide6 控件
    QApplication,  # 管理整个 PySide6 应用及其事件循环
    QFormLayout,  # 按“标签 + 控件”的表单形式排列界面
    QLabel,  # 显示普通文本或计算结果
    QLineEdit,  # 让用户输入课程成绩和学分
    QMessageBox,  # 弹出输入错误等提示对话框
    QPushButton,  # 创建可点击的计算按钮
    QWidget,  # 作为计算器窗口的基础组件
)  # 结束控件导入列表


def calculate_weighted_average(scores, credits):  # 根据成绩和对应学分计算加权平均分
    total = sum(score * credit for score, credit in zip(scores, credits))  # 计算所有“成绩 × 学分”的加权总和
    return total / sum(credits)  # 用加权总分除以总学分并返回平均分


class WeightedAverageCalculator(QWidget):  # 定义成绩加权平均分计算器窗口
    def __init__(self):  # 初始化窗口及其中的全部控件
        super().__init__()  # 调用父类 QWidget 的初始化方法
        self.setWindowTitle("PySide6 成绩加权平均分计算器")  # 设置窗口标题并明确当前示例使用 PySide6
        self.resize(440, 230)  # 设置窗口初始宽度和高度

        self.score_edit = QLineEdit()  # 创建用于输入课程成绩的单行文本框
        self.score_edit.setPlaceholderText("例如：90, 85, 78")  # 显示课程成绩的正确输入格式提示
        self.credit_edit = QLineEdit()  # 创建用于输入课程学分的单行文本框
        self.credit_edit.setPlaceholderText("例如：3, 2, 4")  # 显示课程学分的正确输入格式提示
        self.calculate_button = QPushButton("计算平均分")  # 创建开始计算的按钮
        self.result_label = QLabel("等待计算")  # 创建用于显示计算状态和结果的标签

        layout = QFormLayout()  # 创建表单布局对象，使标签和输入控件对齐排列
        layout.addRow("课程成绩（逗号分隔）", self.score_edit)  # 将成绩标签和输入框加入表单布局
        layout.addRow("课程学分（逗号分隔）", self.credit_edit)  # 将学分标签和输入框加入表单布局
        layout.addRow(self.calculate_button)  # 将计算按钮单独加入表单布局的一行
        layout.addRow("结果", self.result_label)  # 将结果标签和结果显示区域加入表单布局
        self.setLayout(layout)  # 把表单布局设置为窗口的主布局

        self.calculate_button.clicked.connect(self.calculate_average)  # 将按钮点击信号连接到计算平均分的槽函数

    @Slot()  # 声明下面的方法是一个不接收参数的 Qt 槽函数
    def calculate_average(self):  # 读取输入、校验数据并显示加权平均分
        try:  # 尝试把用户输入转换为可参与计算的数据
            scores = [float(item.strip()) for item in self.score_edit.text().split(",") if item.strip()]  # 将逗号分隔的成绩转换为浮点数列表
            credits = [float(item.strip()) for item in self.credit_edit.text().split(",") if item.strip()]  # 将逗号分隔的学分转换为浮点数列表

            if not scores or not credits:  # 判断成绩或学分列表是否为空
                raise ValueError("请输入课程成绩和学分。")  # 输入为空时抛出可提示给用户的错误
            if len(scores) != len(credits):  # 判断成绩数量是否与学分数量相同
                raise ValueError("成绩数量必须与学分数量相同。")  # 数量不一致时抛出可提示给用户的错误
            if any(credit <= 0 for credit in credits):  # 判断是否存在零或负数学分
                raise ValueError("学分必须大于 0。")  # 学分不合法时抛出可提示给用户的错误

            average = calculate_weighted_average(scores, credits)  # 调用独立函数计算加权平均分
            self.result_label.setText(f"加权平均分：{average:.2f}")  # 将结果保留两位小数并显示在标签中
        except ValueError as error:  # 捕获输入转换或数据校验产生的错误
            QMessageBox.warning(self, "输入有误", str(error))  # 用弹窗提示用户需要修改的输入内容


if __name__ == "__main__":  # 仅在直接运行本文件时启动图形界面程序
    app = QApplication(sys.argv)  # 创建 PySide6 应用程序对象并接收命令行参数
    window = WeightedAverageCalculator()  # 创建成绩加权平均分计算器窗口对象
    window.show()  # 显示计算器窗口
    sys.exit(app.exec())  # 启动事件循环，并在退出时返回程序状态码
