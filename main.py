#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 界面示例
一个简单的桌面应用程序界面
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget,
    QComboBox, QCheckBox, QRadioButton, QGroupBox, QTabWidget,
    QProgressBar, QSlider, QSpinBox, QDoubleSpinBox, QDateEdit,
    QTimeEdit, QDateTimeEdit, QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QSplitter,
    QMessageBox, QFileDialog, QMenuBar, QToolBar, QStatusBar
)
from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtGui import QIcon, QFont, QPalette, QColor, QAction


class MainWindow(QMainWindow):
    """主窗口类"""
    
    def __init__(self):
        super().__init__()
        self.status_label = None
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()
        
    def setup_ui(self):
        """设置UI界面"""
        # 设置窗口属性
        self.setWindowTitle("PySide6 界面示例")
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 创建标签页
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # 标签页1: 基本控件
        tab1 = QWidget()
        self.setup_tab1(tab1)
        tab_widget.addTab(tab1, "基本控件")
        
        # 标签页2: 输入控件
        tab2 = QWidget()
        self.setup_tab2(tab2)
        tab_widget.addTab(tab2, "输入控件")
        
        # 标签页3: 表格和列表
        tab3 = QWidget()
        self.setup_tab3(tab3)
        tab_widget.addTab(tab3, "表格和列表")
        
        # 标签页4: 高级控件
        tab4 = QWidget()
        self.setup_tab4(tab4)
        tab_widget.addTab(tab4, "高级控件")
        
        # 标签页5: 数据库操作
        tab5 = QWidget()
        self.setup_tab5(tab5)
        tab_widget.addTab(tab5, "数据库操作")
        
    def setup_tab1(self, tab):
        """设置标签页1: 基本控件"""
        layout = QVBoxLayout(tab)
        
        # 标题
        title_label = QLabel("PySide6 基本控件展示")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 水平分割器
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        
        # 左侧区域
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # 按钮组
        button_group = QGroupBox("按钮控件")
        button_layout = QVBoxLayout()
        
        # 普通按钮
        btn_normal = QPushButton("普通按钮")
        btn_normal.clicked.connect(lambda: self.show_message("普通按钮被点击"))
        button_layout.addWidget(btn_normal)
        
        # 带图标的按钮
        btn_icon = QPushButton("带图标的按钮")
        # 添加图标（使用内置图标）
        btn_icon.clicked.connect(lambda: self.show_message("带图标的按钮被点击"))
        button_layout.addWidget(btn_icon)
        
        # 禁用按钮
        btn_disabled = QPushButton("禁用按钮")
        btn_disabled.setEnabled(False)
        button_layout.addWidget(btn_disabled)
        
        button_group.setLayout(button_layout)
        left_layout.addWidget(button_group)
        
        # 选择控件组
        select_group = QGroupBox("选择控件")
        select_layout = QVBoxLayout()
        
        # 复选框
        checkbox1 = QCheckBox("选项 1")
        checkbox1.clicked.connect(lambda state: self.show_message(f"选项 1 {'已选中' if state else '已取消'}"))
        checkbox2 = QCheckBox("选项 2")
        checkbox2.setChecked(True)
        checkbox2.clicked.connect(lambda state: self.show_message(f"选项 2 {'已选中' if state else '已取消'}"))
        checkbox3 = QCheckBox("选项 3")
        checkbox3.clicked.connect(lambda state: self.show_message(f"选项 3 {'已选中' if state else '已取消'}"))
        select_layout.addWidget(checkbox1)
        select_layout.addWidget(checkbox2)
        select_layout.addWidget(checkbox3)
        
        # 单选框
        radio1 = QRadioButton("单选 1")
        radio1.clicked.connect(lambda state: self.show_message("选择了单选 1"))
        radio2 = QRadioButton("单选 2")
        radio2.setChecked(True)
        radio2.clicked.connect(lambda state: self.show_message("选择了单选 2"))
        radio3 = QRadioButton("单选 3")
        radio3.clicked.connect(lambda state: self.show_message("选择了单选 3"))
        select_layout.addWidget(radio1)
        select_layout.addWidget(radio2)
        select_layout.addWidget(radio3)
        
        select_group.setLayout(select_layout)
        left_layout.addWidget(select_group)
        
        left_layout.addStretch()
        splitter.addWidget(left_widget)
        
        # 右侧区域
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # 进度条组
        progress_group = QGroupBox("进度指示器")
        progress_layout = QVBoxLayout()
        
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(50)
        progress_layout.addWidget(self.progress_bar)
        
        # 滑块
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(self.progress_bar.setValue)
        progress_layout.addWidget(QLabel("滑块:"))
        progress_layout.addWidget(slider)
        
        progress_group.setLayout(progress_layout)
        right_layout.addWidget(progress_group)
        
        # 文本显示组
        text_group = QGroupBox("文本显示")
        text_layout = QVBoxLayout()
        
        # 标签
        label = QLabel("这是一个标签文本")
        text_layout.addWidget(label)
        
        # 多行文本
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("在这里输入多行文本...")
        text_edit.setPlainText("欢迎使用 PySide6 界面示例程序！\n这是一个多行文本编辑区域。")
        text_edit.textChanged.connect(lambda: self.show_message("文本内容已更改"))
        text_layout.addWidget(text_edit)
        
        text_group.setLayout(text_layout)
        right_layout.addWidget(text_group)
        
        right_layout.addStretch()
        splitter.addWidget(right_widget)
        
        # 设置分割器初始比例
        splitter.setSizes([400, 600])
        
    def setup_tab2(self, tab):
        """设置标签页2: 输入控件"""
        layout = QVBoxLayout(tab)
        
        # 标题
        title_label = QLabel("输入控件展示")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 表单布局
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)
        
        # 单行文本输入
        line_edit_group = QGroupBox("文本输入")
        line_edit_layout = QVBoxLayout()
        
        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText("请输入用户名...")
        self.line_edit1.textChanged.connect(lambda text: self.show_message(f"用户名: {text}"))
        line_edit_layout.addWidget(QLabel("用户名:"))
        line_edit_layout.addWidget(self.line_edit1)
        
        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText("请输入密码...")
        self.line_edit2.setEchoMode(QLineEdit.Password)
        self.line_edit2.textChanged.connect(lambda text: self.show_message("密码已输入"))
        line_edit_layout.addWidget(QLabel("密码:"))
        line_edit_layout.addWidget(self.line_edit2)
        
        line_edit_group.setLayout(line_edit_layout)
        form_layout.addWidget(line_edit_group)
        
        # 数字输入
        number_group = QGroupBox("数字输入")
        number_layout = QVBoxLayout()
        
        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)
        self.spin_box.setValue(25)
        self.spin_box.valueChanged.connect(lambda value: self.show_message(f"整数输入: {value}"))
        number_layout.addWidget(QLabel("整数输入:"))
        number_layout.addWidget(self.spin_box)
        
        self.double_spin_box = QDoubleSpinBox()
        self.double_spin_box.setRange(0.0, 100.0)
        self.double_spin_box.setValue(50.5)
        self.double_spin_box.setSingleStep(0.5)
        self.double_spin_box.valueChanged.connect(lambda value: self.show_message(f"小数输入: {value}"))
        number_layout.addWidget(QLabel("小数输入:"))
        number_layout.addWidget(self.double_spin_box)
        
        number_group.setLayout(number_layout)
        form_layout.addWidget(number_group)
        
        # 日期时间输入
        datetime_group = QGroupBox("日期时间输入")
        datetime_layout = QVBoxLayout()
        
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDateTime.currentDateTime().date())
        self.date_edit.dateChanged.connect(lambda date: self.show_message(f"日期: {date.toString()}"))
        datetime_layout.addWidget(QLabel("日期:"))
        datetime_layout.addWidget(self.date_edit)
        
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QDateTime.currentDateTime().time())
        self.time_edit.timeChanged.connect(lambda time: self.show_message(f"时间: {time.toString()}"))
        datetime_layout.addWidget(QLabel("时间:"))
        datetime_layout.addWidget(self.time_edit)
        
        self.datetime_edit = QDateTimeEdit()
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.datetime_edit.dateTimeChanged.connect(lambda datetime: self.show_message(f"日期时间: {datetime.toString()}"))
        datetime_layout.addWidget(QLabel("日期时间:"))
        datetime_layout.addWidget(self.datetime_edit)
        
        datetime_group.setLayout(datetime_layout)
        form_layout.addWidget(datetime_group)
        
        # 下拉选择
        combo_group = QGroupBox("下拉选择")
        combo_layout = QVBoxLayout()
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(["选项 1", "选项 2", "选项 3", "选项 4", "选项 5"])
        self.combo_box.currentIndexChanged.connect(lambda index: self.show_message(f"选择了: {self.combo_box.itemText(index)}"))
        combo_layout.addWidget(QLabel("选择项:"))
        combo_layout.addWidget(self.combo_box)
        
        combo_group.setLayout(combo_layout)
        form_layout.addWidget(combo_group)
        
        # 添加保存按钮
        save_button = QPushButton("保存输入数据")
        save_button.setStyleSheet("font-weight: bold; padding: 10px;")
        save_button.clicked.connect(self.save_input_data)
        form_layout.addWidget(save_button)
        
        form_layout.addStretch()
        layout.addWidget(form_widget)
        
    def setup_tab3(self, tab):
        """设置标签页3: 表格和列表"""
        layout = QVBoxLayout(tab)
        
        # 标题
        title_label = QLabel("表格和列表控件")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 水平分割器
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        
        # 左侧: 列表控件
        list_widget = QWidget()
        list_layout = QVBoxLayout(list_widget)
        
        list_group = QGroupBox("列表控件")
        list_inner_layout = QVBoxLayout()
        
        # 列表
        self.list_widget = QListWidget()
        self.list_widget.addItems(["项目 1", "项目 2", "项目 3", "项目 4", "项目 5"])
        self.list_widget.itemSelectionChanged.connect(lambda: self.show_message(f"选中了: {self.list_widget.currentItem().text() if self.list_widget.currentItem() else '无'}"))
        list_inner_layout.addWidget(self.list_widget)
        
        # 列表操作按钮
        list_btn_layout = QHBoxLayout()
        btn_add = QPushButton("添加项目")
        btn_add.clicked.connect(self.add_list_item)
        btn_remove = QPushButton("删除选中")
        btn_remove.clicked.connect(self.remove_list_item)
        btn_export_list = QPushButton("导出列表")
        btn_export_list.clicked.connect(self.export_list)
        list_btn_layout.addWidget(btn_add)
        list_btn_layout.addWidget(btn_remove)
        list_btn_layout.addWidget(btn_export_list)
        list_inner_layout.addLayout(list_btn_layout)
        
        list_group.setLayout(list_inner_layout)
        list_layout.addWidget(list_group)
        list_layout.addStretch()
        splitter.addWidget(list_widget)
        
        # 右侧: 表格控件
        table_widget = QWidget()
        table_layout = QVBoxLayout(table_widget)
        
        table_group = QGroupBox("表格控件")
        table_inner_layout = QVBoxLayout()
        
        # 表格
        self.table_widget = QTableWidget(5, 4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "姓名", "年龄", "城市"])
        # 设置表格可编辑
        self.table_widget.setEditTriggers(QTableWidget.DoubleClicked)
        # 添加单元格点击事件
        self.table_widget.cellClicked.connect(lambda row, col: self.show_message(f"点击了单元格: 行{row+1}, 列{col+1}"))
        # 添加单元格内容变化事件
        self.table_widget.cellChanged.connect(lambda row, col: self.show_message(f"单元格内容已更改: 行{row+1}, 列{col+1}"))
        
        # 填充示例数据
        data = [
            ["001", "张三", "25", "北京"],
            ["002", "李四", "30", "上海"],
            ["003", "王五", "28", "广州"],
            ["004", "赵六", "35", "深圳"],
            ["005", "钱七", "22", "杭州"]
        ]
        
        for row, row_data in enumerate(data):
            for col, cell_data in enumerate(row_data):
                self.table_widget.setItem(row, col, QTableWidgetItem(cell_data))
        
        table_inner_layout.addWidget(self.table_widget)
        
        # 表格操作按钮
        table_btn_layout = QHBoxLayout()
        btn_refresh = QPushButton("刷新表格")
        btn_refresh.clicked.connect(self.refresh_table)
        btn_clear = QPushButton("清空表格")
        btn_clear.clicked.connect(self.clear_table)
        btn_export = QPushButton("导出数据")
        btn_export.clicked.connect(self.save_file)
        table_btn_layout.addWidget(btn_refresh)
        table_btn_layout.addWidget(btn_clear)
        table_btn_layout.addWidget(btn_export)
        table_inner_layout.addLayout(table_btn_layout)
        
        table_group.setLayout(table_inner_layout)
        table_layout.addWidget(table_group)
        table_layout.addStretch()
        splitter.addWidget(table_widget)
        
        # 设置分割器比例
        splitter.setSizes([300, 700])
        
    def setup_tab4(self, tab):
        """设置标签页4: 高级控件"""
        layout = QVBoxLayout(tab)
        
        # 标题
        title_label = QLabel("高级控件和功能")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 树形控件
        tree_group = QGroupBox("树形结构")
        tree_layout = QVBoxLayout()
        
        tree_widget = QTreeWidget()
        tree_widget.setHeaderLabels(["项目", "类型", "大小"])
        # 添加节点点击事件
        tree_widget.itemClicked.connect(lambda item, column: self.show_message(f"点击了: {item.text(0)}"))
        
        # 添加根节点
        root = QTreeWidgetItem(tree_widget)
        root.setText(0, "根目录")
        
        # 添加子节点
        for i in range(3):
            child = QTreeWidgetItem(root)
            child.setText(0, f"文件夹 {i+1}")
            child.setText(1, "文件夹")
            child.setText(2, "--")
            
            # 添加孙子节点
            for j in range(2):
                grandchild = QTreeWidgetItem(child)
                grandchild.setText(0, f"文件 {j+1}.txt")
                grandchild.setText(1, "文本文件")
                grandchild.setText(2, f"{j+1}KB")
        
        # 默认展开根节点
        tree_widget.expandItem(root)
        
        tree_layout.addWidget(tree_widget)
        tree_group.setLayout(tree_layout)
        layout.addWidget(tree_group)
        
        # 功能按钮组
        function_group = QGroupBox("功能演示")
        function_layout = QHBoxLayout()
        
        # 各种功能按钮
        btn_message = QPushButton("显示消息框")
        btn_message.clicked.connect(self.show_message_box)
        
        btn_file = QPushButton("选择文件")
        btn_file.clicked.connect(self.select_file)
        
        btn_color = QPushButton("更改背景色")
        btn_color.clicked.connect(self.change_background)
        
        btn_timer = QPushButton("启动计时器")
        btn_timer.clicked.connect(self.start_timer)
        
        function_layout.addWidget(btn_message)
        function_layout.addWidget(btn_file)
        function_layout.addWidget(btn_color)
        function_layout.addWidget(btn_timer)
        
        function_group.setLayout(function_layout)
        layout.addWidget(function_group)
        
        # 状态显示
        self.status_label = QLabel("就绪")
        self.status_label.setStyleSheet("padding: 10px; background-color: #f0f0f0; border: 1px solid #ccc;")
        layout.addWidget(self.status_label)
        
        layout.addStretch()
        
    def setup_tab5(self, tab):
        """设置标签页5: 数据库操作"""
        layout = QVBoxLayout(tab)
        
        # 标题
        title_label = QLabel("数据库操作")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 水平分割器
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        
        # 左侧区域 - 数据库设置
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # 数据集选择
        dataset_group = QGroupBox("数据集设置")
        dataset_layout = QVBoxLayout()
        
        # 数据集类型
        dataset_layout.addWidget(QLabel("数据集类型:"))
        self.dataset_combo = QComboBox()
        self.dataset_combo.addItems(["Market-1501", "DukeMTMC"])
        dataset_layout.addWidget(self.dataset_combo)
        
        # 数据路径
        dataset_layout.addWidget(QLabel("数据路径:"))
        path_layout = QHBoxLayout()
        self.data_path_edit = QLineEdit()
        self.data_path_edit.setPlaceholderText("请输入数据路径...")
        path_layout.addWidget(self.data_path_edit)
        btn_browse = QPushButton("浏览")
        btn_browse.clicked.connect(self.browse_data_path)
        path_layout.addWidget(btn_browse)
        dataset_layout.addLayout(path_layout)
        
        dataset_group.setLayout(dataset_layout)
        left_layout.addWidget(dataset_group)
        
        # 操作按钮组
        action_group = QGroupBox("操作")
        action_layout = QVBoxLayout()
        
        btn_load_data = QPushButton("加载数据")
        btn_load_data.clicked.connect(self.load_dataset)
        action_layout.addWidget(btn_load_data)
        
        btn_preprocess = QPushButton("预处理数据")
        btn_preprocess.clicked.connect(self.preprocess_data)
        action_layout.addWidget(btn_preprocess)
        
        btn_train = QPushButton("训练模型")
        btn_train.clicked.connect(self.train_model)
        action_layout.addWidget(btn_train)
        
        action_group.setLayout(action_layout)
        left_layout.addWidget(action_group)
        
        left_layout.addStretch()
        splitter.addWidget(left_widget)
        
        # 右侧区域 - 数据预览
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # 数据信息
        info_group = QGroupBox("数据信息")
        info_layout = QVBoxLayout()
        
        self.data_info_text = QTextEdit()
        self.data_info_text.setReadOnly(True)
        self.data_info_text.setPlaceholderText("数据信息将显示在这里...")
        info_layout.addWidget(self.data_info_text)
        
        info_group.setLayout(info_layout)
        right_layout.addWidget(info_group)
        
        # 图片预览
        preview_group = QGroupBox("图片预览")
        preview_layout = QVBoxLayout()
        
        self.preview_label = QLabel("图片预览")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setMinimumHeight(200)
        self.preview_label.setStyleSheet("border: 1px solid #ccc;")
        preview_layout.addWidget(self.preview_label)
        
        preview_group.setLayout(preview_layout)
        right_layout.addWidget(preview_group)
        
        # 进度条
        progress_group = QGroupBox("进度")
        progress_layout = QVBoxLayout()
        
        self.db_progress_bar = QProgressBar()
        self.db_progress_bar.setVisible(False)
        progress_layout.addWidget(self.db_progress_bar)
        
        progress_group.setLayout(progress_layout)
        right_layout.addWidget(progress_group)
        
        right_layout.addStretch()
        splitter.addWidget(right_widget)
        
        # 设置分割器初始比例
        splitter.setSizes([400, 600])
        
    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        
        new_action = QAction("新建", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(lambda: self.show_message("新建文件"))
        file_menu.addAction(new_action)
        
        open_action = QAction("打开", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.select_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        save_action = QAction("保存", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("退出", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        
        cut_action = QAction("剪切", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(lambda: self.show_message("剪切"))
        edit_menu.addAction(cut_action)
        
        copy_action = QAction("复制", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(lambda: self.show_message("复制"))
        edit_menu.addAction(copy_action)
        
        paste_action = QAction("粘贴", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(lambda: self.show_message("粘贴"))
        edit_menu.addAction(paste_action)
        
        # 视图菜单
        view_menu = menubar.addMenu("视图")
        
        zoom_in_action = QAction("放大", self)
        zoom_in_action.setShortcut("Ctrl++")
        zoom_in_action.triggered.connect(lambda: self.show_message("放大视图"))
        view_menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction("缩小", self)
        zoom_out_action.setShortcut("Ctrl+-")
        zoom_out_action.triggered.connect(lambda: self.show_message("缩小视图"))
        view_menu.addAction(zoom_out_action)
        
        # 帮助菜单
        help_menu = menubar.addMenu("帮助")
        
        about_action = QAction("关于", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def setup_toolbar(self):
        """设置工具栏"""
        toolbar = QToolBar("主工具栏")
        self.addToolBar(toolbar)
        
        # 添加工具按钮
        new_action = QAction("新建", self)
        new_action.triggered.connect(lambda: self.show_message("新建文件"))
        toolbar.addAction(new_action)
        
        open_action = QAction("打开", self)
        open_action.triggered.connect(self.select_file)
        toolbar.addAction(open_action)
        
        save_action = QAction("保存", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        cut_action = QAction("剪切", self)
        cut_action.triggered.connect(lambda: self.show_message("剪切"))
        toolbar.addAction(cut_action)
        
        copy_action = QAction("复制", self)
        copy_action.triggered.connect(lambda: self.show_message("复制"))
        toolbar.addAction(copy_action)
        
        paste_action = QAction("粘贴", self)
        paste_action.triggered.connect(lambda: self.show_message("粘贴"))
        toolbar.addAction(paste_action)
        
    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        
        # 状态标签
        self.status_label = QLabel("就绪")
        statusbar.addWidget(self.status_label)
        
        # 时间标签
        self.time_label = QLabel()
        statusbar.addPermanentWidget(self.time_label)
        
        # 更新时间
        self.update_time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒更新一次
        
    def update_time(self):
        """更新时间显示"""
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.time_label.setText(current_time)
        
    # 槽函数
    def show_message(self, text):
        """显示消息"""
        if self.status_label:
            self.status_label.setText(text)
        
    def add_list_item(self):
        """添加列表项目"""
        item_count = self.list_widget.count()
        self.list_widget.addItem(f"项目 {item_count + 1}")
        self.show_message(f"已添加项目 {item_count + 1}")
        
    def remove_list_item(self):
        """删除选中的列表项目"""
        current_item = self.list_widget.currentItem()
        if current_item:
            row = self.list_widget.row(current_item)
            self.list_widget.takeItem(row)
            self.show_message(f"已删除项目 {row + 1}")
            
    def refresh_table(self):
        """刷新表格"""
        # 重新填充示例数据
        data = [
            ["001", "张三", "25", "北京"],
            ["002", "李四", "30", "上海"],
            ["003", "王五", "28", "广州"],
            ["004", "赵六", "35", "深圳"],
            ["005", "钱七", "22", "杭州"]
        ]
        
        for row, row_data in enumerate(data):
            for col, cell_data in enumerate(row_data):
                self.table_widget.setItem(row, col, QTableWidgetItem(cell_data))
        
        self.show_message("表格已刷新")
        
    def clear_table(self):
        """清空表格"""
        self.table_widget.clearContents()
        self.show_message("表格已清空")
        
    def show_message_box(self):
        """显示消息框"""
        QMessageBox.information(
            self,
            "信息",
            "这是一个信息消息框！\nPySide6 提供了丰富的对话框功能。"
        )
        self.show_message("显示了消息框")
        
    def select_file(self):
        """选择文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "所有文件 (*.*);;文本文件 (*.txt);;Python文件 (*.py);;CSV文件 (*.csv)"
        )
        if file_path:
            self.show_message(f"已选择文件: {file_path}")
            # 如果是CSV文件，尝试加载到表格
            if file_path.endswith('.csv'):
                self.load_csv_file(file_path)
    
    def load_csv_file(self, file_path):
        """加载CSV文件到表格"""
        try:
            import csv
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                data = list(reader)
                if data:
                    # 清空表格
                    self.table_widget.clearContents()
                    # 设置表格大小
                    rows = len(data) - 1  # 第一行是标题
                    cols = len(data[0])
                    self.table_widget.setRowCount(rows)
                    self.table_widget.setColumnCount(cols)
                    # 设置表头
                    headers = data[0]
                    self.table_widget.setHorizontalHeaderLabels(headers)
                    # 填充数据
                    for row in range(rows):
                        for col in range(cols):
                            self.table_widget.setItem(row, col, QTableWidgetItem(data[row+1][col]))
                    self.show_message(f"已从 {file_path} 加载数据")
        except Exception as e:
            self.show_message(f"加载文件失败: {str(e)}")
    
    def save_file(self):
        """保存文件"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存文件",
            "",
            "CSV文件 (*.csv);;文本文件 (*.txt);;所有文件 (*.*)"
        )
        if file_path:
            # 如果是CSV文件，保存表格数据
            if file_path.endswith('.csv'):
                self.save_csv_file(file_path)
            else:
                self.show_message(f"已保存文件: {file_path}")
    
    def save_csv_file(self, file_path):
        """保存表格数据到CSV文件"""
        try:
            import csv
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # 写入表头
                headers = []
                for col in range(self.table_widget.columnCount()):
                    header = self.table_widget.horizontalHeaderItem(col)
                    headers.append(header.text() if header else f"列{col+1}")
                writer.writerow(headers)
                # 写入数据
                for row in range(self.table_widget.rowCount()):
                    row_data = []
                    for col in range(self.table_widget.columnCount()):
                        item = self.table_widget.item(row, col)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)
                self.show_message(f"数据已保存到 {file_path}")
        except Exception as e:
            self.show_message(f"保存文件失败: {str(e)}")
            
    def change_background(self):
        """更改背景色"""
        # 模拟颜色选择功能
        import random
        colors = ["#ecf0f1", "#3498db", "#2ecc71", "#e74c3c", "#f39c12"]
        random_color = random.choice(colors)
        
        # 设置窗口背景色
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(random_color))
        self.setPalette(palette)
        
        self.show_message(f"背景色已更改为: {random_color}")
        
    def start_timer(self):
        """启动计时器"""
        # 创建一个临时的计时器窗口
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
        
        timer_dialog = QDialog(self)
        timer_dialog.setWindowTitle("计时器")
        timer_dialog.setGeometry(200, 200, 300, 200)
        
        layout = QVBoxLayout()
        
        self.timer_label = QLabel("00:00:00", timer_dialog)
        self.timer_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_label)
        
        self.timer_seconds = 0
        
        def update_timer():
            self.timer_seconds += 1
            hours = self.timer_seconds // 3600
            minutes = (self.timer_seconds % 3600) // 60
            seconds = self.timer_seconds % 60
            self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        
        self.timer = QTimer()
        self.timer.timeout.connect(update_timer)
        self.timer.start(1000)
        
        stop_button = QPushButton("停止", timer_dialog)
        stop_button.clicked.connect(lambda: self.timer.stop())
        layout.addWidget(stop_button)
        
        timer_dialog.setLayout(layout)
        timer_dialog.exec()
        
        self.show_message("计时器已启动")
        
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self,
            "关于 PySide6 界面示例",
            "PySide6 界面示例程序\n\n"
            "这是一个展示 PySide6 各种控件的示例界面。\n"
            "包含了按钮、输入框、表格、列表、菜单栏、工具栏等常用控件。\n\n"
            "版本: 1.0.0\n"
            "使用 PySide6 开发"
        )
    
    def save_input_data(self):
        """保存输入数据"""
        # 收集输入数据
        input_data = {
            "用户名": self.line_edit1.text() if hasattr(self, 'line_edit1') else "",
            "密码": self.line_edit2.text() if hasattr(self, 'line_edit2') else "",
            "整数输入": self.spin_box.value() if hasattr(self, 'spin_box') else 0,
            "小数输入": self.double_spin_box.value() if hasattr(self, 'double_spin_box') else 0.0,
            "日期": self.date_edit.date().toString() if hasattr(self, 'date_edit') else "",
            "时间": self.time_edit.time().toString() if hasattr(self, 'time_edit') else "",
            "日期时间": self.datetime_edit.dateTime().toString() if hasattr(self, 'datetime_edit') else "",
            "下拉选择": self.combo_box.currentText() if hasattr(self, 'combo_box') else ""
        }
        
        # 保存到文件
        import json
        import os
        
        save_path = os.path.join(os.path.expanduser("~"), "input_data.json")
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(input_data, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "保存成功", f"输入数据已保存到: {save_path}")
            self.show_message("输入数据已保存")
        except Exception as e:
            QMessageBox.error(self, "保存失败", f"保存数据时出错: {str(e)}")
            self.show_message(f"保存失败: {str(e)}")
    
    def export_list(self):
        """导出列表数据"""
        # 收集列表数据
        list_items = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            list_items.append(item.text() if item else "")
        
        # 保存到文件
        import json
        import os
        
        save_path = os.path.join(os.path.expanduser("~"), "list_data.json")
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(list_items, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "导出成功", f"列表数据已导出到: {save_path}")
            self.show_message("列表数据已导出")
        except Exception as e:
            QMessageBox.error(self, "导出失败", f"导出数据时出错: {str(e)}")
            self.show_message(f"导出失败: {str(e)}")
    
    # 数据库操作方法
    def browse_data_path(self):
        """浏览数据路径"""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "选择数据目录",
            ""
        )
        if dir_path:
            self.data_path_edit.setText(dir_path)
            self.show_message(f"已选择数据路径: {dir_path}")
    
    def load_dataset(self):
        """加载数据集"""
        data_path = self.data_path_edit.text()
        dataset_type = self.dataset_combo.currentText()
        
        if not data_path:
            QMessageBox.warning(self, "警告", "请先选择数据路径")
            return
        
        self.show_message("正在加载数据集...")
        self.db_progress_bar.setVisible(True)
        self.db_progress_bar.setValue(0)
        
        try:
            # 模拟加载过程
            import time
            for i in range(101):
                time.sleep(0.02)
                self.db_progress_bar.setValue(i)
            
            # 检查数据路径
            import os
            if dataset_type == "Market-1501":
                attr_path = os.path.join(data_path, "Market-1501", "attribute", "market_attribute.mat")
                img_dir = os.path.join(data_path, "Market-1501", "bounding_box_train")
            else:
                attr_path = os.path.join(data_path, "DukeMTMC", "attribute", "duke_attribute.mat")
                img_dir = os.path.join(data_path, "DukeMTMC", "bounding_box_train")
            
            # 检查文件是否存在
            attr_exists = os.path.exists(attr_path)
            img_dir_exists = os.path.exists(img_dir)
            
            # 获取图片数量
            img_count = 0
            if img_dir_exists:
                img_count = len([f for f in os.listdir(img_dir) if f.endswith('.jpg')])
            
            # 显示数据信息
            info = f"数据集: {dataset_type}\n"
            info += f"数据路径: {data_path}\n"
            info += f"属性文件存在: {'是' if attr_exists else '否'}\n"
            info += f"图片目录存在: {'是' if img_dir_exists else '否'}\n"
            info += f"图片数量: {img_count}\n"
            
            self.data_info_text.setText(info)
            self.show_message("数据集加载完成")
            
            # 预览第一张图片
            if img_dir_exists and img_count > 0:
                import glob
                img_files = glob.glob(os.path.join(img_dir, "*.jpg"))
                if img_files:
                    from PySide6.QtGui import QPixmap
                    pixmap = QPixmap(img_files[0])
                    scaled_pixmap = pixmap.scaled(self.preview_label.width(), self.preview_label.height(), 
                                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.preview_label.setPixmap(scaled_pixmap)
        except Exception as e:
            QMessageBox.error(self, "错误", f"加载数据集失败: {str(e)}")
            self.show_message(f"加载数据集失败: {str(e)}")
        finally:
            self.db_progress_bar.setVisible(False)
    
    def preprocess_data(self):
        """预处理数据"""
        data_path = self.data_path_edit.text()
        if not data_path:
            QMessageBox.warning(self, "警告", "请先选择数据路径")
            return
        
        self.show_message("正在预处理数据...")
        self.db_progress_bar.setVisible(True)
        self.db_progress_bar.setValue(0)
        
        try:
            # 模拟预处理过程
            import time
            for i in range(101):
                time.sleep(0.02)
                self.db_progress_bar.setValue(i)
            
            self.show_message("数据预处理完成")
            QMessageBox.information(self, "成功", "数据预处理完成")
        except Exception as e:
            QMessageBox.error(self, "错误", f"预处理数据失败: {str(e)}")
            self.show_message(f"预处理数据失败: {str(e)}")
        finally:
            self.db_progress_bar.setVisible(False)
    
    def train_model(self):
        """训练模型"""
        data_path = self.data_path_edit.text()
        dataset_type = self.dataset_combo.currentText()
        
        if not data_path:
            QMessageBox.warning(self, "警告", "请先选择数据路径")
            return
        
        self.show_message("正在训练模型...")
        self.db_progress_bar.setVisible(True)
        self.db_progress_bar.setValue(0)
        
        try:
            # 模拟训练过程
            import time
            for i in range(101):
                time.sleep(0.05)
                self.db_progress_bar.setValue(i)
            
            # 保存模型
            import os
            save_dir = os.path.join(data_path, "checkpoints")
            os.makedirs(save_dir, exist_ok=True)
            model_path = os.path.join(save_dir, f"{dataset_type.lower()}_resnet50.pth")
            
            # 模拟保存模型
            with open(model_path, 'w') as f:
                f.write("model weights")
            
            self.show_message("模型训练完成")
            QMessageBox.information(self, "成功", f"模型已保存到: {model_path}")
        except Exception as e:
            QMessageBox.error(self, "错误", f"训练模型失败: {str(e)}")
            self.show_message(f"训练模型失败: {str(e)}")
        finally:
            self.db_progress_bar.setVisible(False)


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle("Fusion")
    
    # 创建并显示主窗口
    window = MainWindow()
    window.show()
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    main()