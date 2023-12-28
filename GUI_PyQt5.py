""" ******** package import ************"""
import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import *
from PyQt5.Qt import QIcon


def run_base_widgets():
    """Create a blank window"""
    window = QWidget()
    """Set window title"""
    window.setWindowTitle("计时器")
    """Set window size"""
    window.resize(600, 400)
    """Move window position to screen center"""
    center_point = QDesktopWidget().availableGeometry().center()
    rect = window.frameGeometry().getRect()
    width, height = rect[-2], rect[-1]
    x = center_point.x() - (width // 2)
    y = center_point.y() - (height // 2)
    window.move(x, y)
    """Swt app logo"""
    window.setWindowIcon(QIcon("R-C (2).jpg"))
    """Add 'label' controller and """
    Label = QLabel("账号：", window)
    """Move label position"""
    Label.setGeometry(100, 100, 50, 30)
    """Add button"""
    Button1 = QPushButton("按 钮")
    Button1.setGeometry(155, 200, 80, 30)
    Button1.setParent(window)
    """Add single row input rectangle"""
    edit = QLineEdit(window)
    """Add default show text"""
    edit.setPlaceholderText("输入账号")
    edit.setGeometry(155, 100, 200, 30)
    """Show window"""
    window.show()
    """Come in main loop and permit soft exit"""
    # sys.exit(app.exec_())
    app.exec_()


class run_Qt_layout(QWidget):
    """
    Widgets can be suitable window change
    Father class must be Widget
    """

    def __init__(self):
        super().__init__()
        # self.init_ui_box_layout()
        # self.init_ui_nine_layout()
        self.layout = None
        self.init_ui_stacked_layout()

    def init_ui_box_layout(self):
        # self.resize(300, 300)
        self.setWindowTitle("盒子布局")
        layout = QVBoxLayout()  # 最外层垂直布局
        layout_v = QVBoxLayout()  # 内部垂直布局
        layout_h = QHBoxLayout()  # 内部水平布局
        # --------------------------------- #
        box_1 = QGroupBox("垂直")
        btn1 = QRadioButton("选项1")
        btn2 = QRadioButton("选项2")
        btn3 = QRadioButton("选项3")
        # layout.addStretch()  # set stretch single
        layout_v.addWidget(btn1, stretch=1)
        layout_v.addWidget(btn2)
        layout_v.addWidget(btn3)
        box_1.setLayout(layout_v)
        # --------------------------------- #
        box_2 = QGroupBox("水平")
        btn4 = QPushButton("按钮4")
        btn5 = QPushButton("按钮5")
        layout_h.addWidget(btn4, stretch=1)
        layout_h.addWidget(btn5, stretch=1)
        box_2.setLayout(layout_h)

        layout.addWidget(box_1)
        layout.addLayout(layout_h)
        self.setLayout(layout)

    def init_ui_nine_layout(self):
        """Identy with Box_Layout"""
        self.setWindowTitle("九宫格布局")
        data = {
            0: ['7', '8', '9', 'x'],
            1: ['4', '5', '6', '-'],
            2: ['1', '2', '3', '+'],
            3: ['/', '0', '.', '=']}
        layout_v = QVBoxLayout()
        grid = QGridLayout()
        ############################################
        edit = QLineEdit()
        edit.setPlaceholderText("输入内容")
        ############################################
        for line_num, line_data in data.items():
            for col_num, num in enumerate(line_data):
                btn = QPushButton(num)
                grid.addWidget(btn, line_num, col_num)
        ############################################
        layout_v.addWidget(edit)
        layout_v.addLayout(grid)
        self.setLayout(layout_v)

    def init_ui_stacked_layout(self):
        # self.setFixedSize(300, 300)
        self.layout = QStackedLayout()
        layout_v = QVBoxLayout()
        Win = QWidget()  # 放置抽屉布局控件
        Win.setFixedSize(300, 200)
        ##################################
        win1 = QWidget(Win)
        win1.setFixedSize(100, 20)
        win1.setStyleSheet("background-color:blue;")
        QLabel("按钮1显示内容", win1)
        win2 = QWidget(Win)
        win2.setFixedSize(100, 20)
        QLabel("按钮2显示内容", win2)
        win2.setStyleSheet("background-color:yellow;")
        ##################################
        self.layout.addWidget(win1)  # 抽屉1
        self.layout.addWidget(win2)  # 抽屉2
        ###################################
        Win.setLayout(self.layout)  # 抽屉布局设置
        Win.setStyleSheet("background-color:white;")
        ###################################
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        # 函数方法不加括号，表示触发时才调用
        btn1.clicked.connect(self.btn1_events)
        btn2.clicked.connect(self.btn2_events)
        ##################################
        layout_v.addWidget(Win)
        layout_v.addWidget(btn1)
        layout_v.addWidget(btn2)

        self.setLayout(layout_v)

    def btn1_events(self):
        self.layout.setCurrentIndex(0)

    def btn2_events(self):
        self.layout.setCurrentIndex(1)


class run_Window(QMainWindow):
    """Allow user add select sheet at window head"""
    # 声明信号，且只能放在类内，不能放在方法内
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        ##############################
        self.resize(300, 300)
        self.scoll = QScrollArea(self)  # 滚动器
        self.scoll.setGeometry(10, 50, 290, 120)
        self.scoll.setStyleSheet("background-color:white;")
        ##############################
        self.label = QLabel()
        self.label.setWordWrap(True)  # 自动换行
        self.label.setAlignment(Qt.AlignTop)
        self.label.setStyleSheet("background-color:white;")
        ################################
        self.msg_h = []
        self.init_ui()

    def init_ui(self):
        menu = self.menuBar()  # 获得菜单栏
        # menu.setNativeMenuBar(False)  # Mac 系统开发
        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")
        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("复制")
        edit_menu.addAction("剪切")
        edit_menu.addAction("粘贴")
        #######################################
        btn = QPushButton("请点击", self)
        btn.clicked.connect(self.click_events)
        ######################################
        self.my_signal.connect(self.slot)  # 信号绑定
        #####################################
        self.scoll.setWidget(self.label)
        layout_ = QVBoxLayout()
        layout_.addWidget(self.scoll)
        self.layout.addWidget(btn)
        self.layout.addLayout(layout_)
        #####################################
        self.setLayout(self.layout)

    def slot(self, massage):
        self.msg_h.append(massage)
        self.label.repaint()  # 更新内容
        self.label.setText("<br/>".join(self.msg_h))
        self.label.resize(250, self.label.frameSize().height() + 15)

    def click_events(self):
        for i, id in enumerate(['192.168.1.%d' % x for x in range(1, 256)]):
            m = "模拟，正在检查 %s ..." % id
            if i % 5 == 0:
                self.my_signal.emit(m + "危险")


class run_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 400)


if __name__ == "__main__":
    """Create a application instance"""
    app = QApplication(sys.argv)  # Tell system to run procedure
    print(sys.argv)
    win = run_Qt_layout()
    win.show()
    app.exec()
    # run_base_widgets()
