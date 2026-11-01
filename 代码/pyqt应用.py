import sys  # 导入系统模块，为 PySide6 应用传递启动参数并返回退出状态码

from PySide6.QtCore import Slot  # 导入槽装饰器，用于标记按钮点击后的业务方法
from PySide6.QtWidgets import (  # 导入构建学生信息管理器所需的 PySide6 控件
    QApplication,  # 管理整个 PySide6 应用和事件循环
    QAbstractItemView,  # 配置表格的选择和编辑行为
    QFormLayout,  # 按“标签 + 输入控件”形式排列录入区域
    QHBoxLayout,  # 水平排列操作按钮
    QHeaderView,  # 设置表格表头的显示方式
    QLabel,  # 显示普通文字标题
    QLineEdit,  # 创建单行文本输入框
    QMessageBox,  # 弹出错误或提示对话框
    QPushButton,  # 创建可点击按钮
    QSpinBox,  # 创建带上下箭头的数字输入框
    QTableWidget,  # 创建表格控件
    QTableWidgetItem,  # 创建表格中的单元格内容
    QVBoxLayout,  # 垂直排列窗口中的各个区域
    QWidget,  # 作为主窗口的基础控件
)  # 结束控件导入列表


class StudentManager(QWidget):  # 定义演示数据录入、表格展示和删除功能的 PySide6 窗口类
    def __init__(self):  # 初始化窗口和全部界面控件
        super().__init__()  # 调用父类 QWidget 的初始化方法
        self.setWindowTitle("PySide6 学生信息管理器")  # 设置窗口标题并明确当前示例使用 PySide6
        self.resize(680, 450)  # 设置窗口初始宽度和高度

        self.name_edit = QLineEdit()  # 创建姓名输入框，用于录入学生姓名
        self.name_edit.setPlaceholderText("请输入姓名")  # 设置姓名输入框中的提示文字
        self.age_spin = QSpinBox()  # 创建年龄数字输入框，用于录入学生年龄
        self.age_spin.setRange(1, 120)  # 限制年龄只能在 1 到 120 之间
        self.age_spin.setValue(18)  # 将默认年龄设置为 18
        self.course_edit = QLineEdit()  # 创建课程输入框，用于录入所学课程
        self.course_edit.setPlaceholderText("例如：Python 程序设计")  # 设置课程输入框中的示例文字
        self.add_button = QPushButton("添加记录")  # 创建把录入数据加入表格的按钮
        self.delete_button = QPushButton("删除选中记录")  # 创建删除当前选中表格行的按钮

        form_layout = QFormLayout()  # 创建表单布局来整齐排列录入控件
        form_layout.addRow("姓名：", self.name_edit)  # 添加姓名标签和姓名输入框
        form_layout.addRow("年龄：", self.age_spin)  # 添加年龄标签和年龄输入框
        form_layout.addRow("课程：", self.course_edit)  # 添加课程标签和课程输入框

        button_layout = QHBoxLayout()  # 创建让两个操作按钮并排显示的水平布局
        button_layout.addWidget(self.add_button)  # 将添加记录按钮放入水平布局
        button_layout.addWidget(self.delete_button)  # 将删除记录按钮放入水平布局

        self.table = QTableWidget(0, 3)  # 创建初始为 0 行、3 列的学生信息表格
        self.table.setHorizontalHeaderLabels(["姓名", "年龄", "课程"])  # 设置三列表头对应的文字
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 让三列自动拉伸并填满表格宽度
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # 设置点击任意单元格时选中整行
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)  # 设置一次只允许选择一条记录
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 禁止直接双击修改表格单元格内容
        self.table.setAlternatingRowColors(True)  # 开启隔行换色以便阅读多条记录

        layout = QVBoxLayout()  # 创建按从上到下顺序摆放界面的主垂直布局
        layout.addWidget(QLabel("录入学生信息"))  # 添加录入区域标题标签
        layout.addLayout(form_layout)  # 将录入表单布局加入主布局
        layout.addLayout(button_layout)  # 将按钮布局加入主布局
        layout.addWidget(QLabel("学生信息表"))  # 添加表格区域标题标签
        layout.addWidget(self.table)  # 将学生信息表格加入主布局
        self.setLayout(layout)  # 将主垂直布局设置为窗口布局

        self.add_button.clicked.connect(self.add_student)  # 将添加按钮的点击信号连接到新增记录的方法
        self.delete_button.clicked.connect(self.delete_selected_student)  # 将删除按钮的点击信号连接到删除记录的方法

    @Slot()  # 声明下面的方法是一个不接收参数的 Qt 槽函数
    def add_student(self):  # 读取输入内容并新增一行学生记录
        name = self.name_edit.text().strip()  # 读取姓名输入框文字并去除首尾空格
        age = self.age_spin.value()  # 读取年龄数字输入框中的数值
        course = self.course_edit.text().strip()  # 读取课程输入框文字并去除首尾空格

        if not name or not course:  # 判断姓名或课程是否为空
            QMessageBox.warning(self, "输入有误", "姓名和课程不能为空。")  # 弹窗提示用户补全必填内容
            return  # 终止本次添加操作，避免向表格写入不完整数据

        row = self.table.rowCount()  # 获取当前表格行数，作为新记录所在的行号
        self.table.insertRow(row)  # 在表格末尾插入一个新行
        self.table.setItem(row, 0, QTableWidgetItem(name))  # 在第 1 列写入学生姓名
        self.table.setItem(row, 1, QTableWidgetItem(str(age)))  # 在第 2 列写入学生年龄
        self.table.setItem(row, 2, QTableWidgetItem(course))  # 在第 3 列写入学生课程
        self.name_edit.clear()  # 清空姓名输入框，方便继续录入下一位学生
        self.course_edit.clear()  # 清空课程输入框，方便继续录入下一门课程
        self.name_edit.setFocus()  # 将输入光标重新放回姓名输入框

    @Slot()  # 声明下面的方法是一个不接收参数的 Qt 槽函数
    def delete_selected_student(self):  # 删除表格中当前选中的学生记录
        selected_rows = self.table.selectionModel().selectedRows()  # 获取表格中当前选中的行索引列表

        if not selected_rows:  # 判断用户是否选中了任何一行
            QMessageBox.warning(self, "未选择记录", "请先在表格中选择要删除的一行。")  # 未选择时弹出提示信息
            return  # 终止删除操作，防止用户误以为操作已经成功

        for index in sorted(selected_rows, key=lambda item: item.row(), reverse=True):  # 按行号从后往前遍历选中行，避免删除时影响后续行号
            self.table.removeRow(index.row())  # 根据行号从表格中删除对应记录


if __name__ == "__main__":  # 仅在直接运行本文件时执行以下启动代码
    app = QApplication(sys.argv)  # 创建 PySide6 应用程序对象并接收命令行参数
    window = StudentManager()  # 创建学生信息管理器窗口实例
    window.show()  # 显示学生信息管理器主窗口
    sys.exit(app.exec())  # 启动事件循环，并在窗口关闭后返回退出状态码
