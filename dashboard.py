#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 仪表板界面
现代化仪表板设计示例 - 舆情监控专用
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLabel, QFrame, QGridLayout, QStackedWidget,
    QTableWidget, QTableWidgetItem, QProgressBar, QLineEdit, QTextEdit,
    QComboBox, QCheckBox, QSpinBox, QGroupBox, QScrollArea,
    QMenuBar, QToolBar, QStatusBar, QMessageBox
)
from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtGui import QFont, QPalette, QColor, QAction, QIcon


class Dashboard(QMainWindow):
    """现代化仪表板界面 - 舆情监控专用"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()
        self.setup_timers()
        
    def setup_ui(self):
        """设置UI界面"""
        # 设置窗口属性
        self.setWindowTitle("智言空间 - 现代化仪表板")
        self.setGeometry(100, 100, 1400, 900)
        
        # 应用现代样式
        self.apply_modern_style()
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 顶部栏
        top_bar = self.create_top_bar()
        main_layout.addWidget(top_bar)
        
        # 主要内容区域
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setSpacing(20)
        
        # 左侧导航栏
        sidebar = self.create_sidebar()
        content_layout.addWidget(sidebar)
        
        # 右侧内容区域 - 使用堆叠窗口管理不同页面
        self.stacked_widget = QStackedWidget()
        
        # 创建各个页面
        self.dashboard_page = self.create_dashboard_page()
        self.user_management_page = self.create_user_management_page()
        self.data_report_page = self.create_data_report_page()
        self.system_settings_page = self.create_system_settings_page()
        self.security_center_page = self.create_security_center_page()
        self.document_center_page = self.create_document_center_page()
        self.help_support_page = self.create_help_support_page()
        
        # 添加页面到堆叠窗口
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.user_management_page)
        self.stacked_widget.addWidget(self.data_report_page)
        self.stacked_widget.addWidget(self.system_settings_page)
        self.stacked_widget.addWidget(self.security_center_page)
        self.stacked_widget.addWidget(self.document_center_page)
        self.stacked_widget.addWidget(self.help_support_page)
        
        content_layout.addWidget(self.stacked_widget, 1)  # 拉伸因子
        
        main_layout.addWidget(content_widget, 1)
        
    def create_top_bar(self):
        """创建顶部栏"""
        top_bar = QFrame()
        top_bar.setFrameShape(QFrame.NoFrame)
        top_bar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        
        layout = QHBoxLayout(top_bar)
        
        # 应用标题
        title_label = QLabel("📊 智言空间 - 网络舆情监控平台")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title_label)
        
        layout.addStretch()
        
        # 搜索框
        search_input = QLineEdit()
        search_input.setPlaceholderText("搜索舆情关键词...")
        search_input.setFixedWidth(300)
        search_input.setStyleSheet("""
            QLineEdit {
                background-color: #34495e;
                border: 1px solid #4a6572;
                border-radius: 4px;
                padding: 6px 12px;
                color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        layout.addWidget(search_input)
        
        # 用户信息
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)
        user_layout.setSpacing(10)
        
        user_icon = QLabel("👤")
        user_icon.setStyleSheet("font-size: 16px;")
        
        user_name = QLabel("管理员")
        user_name.setStyleSheet("color: white; font-weight: bold;")
        
        user_layout.addWidget(user_icon)
        user_layout.addWidget(user_name)
        
        layout.addWidget(user_widget)
        
        return top_bar
    
    def create_sidebar(self):
        """创建侧边导航栏"""
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setFrameShape(QFrame.StyledPanel)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setSpacing(5)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # 导航标题
        nav_title = QLabel("导航菜单")
        nav_title.setStyleSheet("""
            QLabel {
                color: #7f8c8d;
                font-size: 12px;
                font-weight: bold;
                padding: 5px 0;
            }
        """)
        layout.addWidget(nav_title)
        
        # 导航按钮
        nav_items = [
            ("📈 仪表板", 0),
            ("👥 用户管理", 1),
            ("📊 数据报表", 2),
            ("⚙️ 系统设置", 3),
            ("🛡️ 安全中心", 4),
            ("📚 文档中心", 5),
            ("❓ 帮助支持", 6)
        ]
        
        self.nav_buttons = []
        for text, index in nav_items:
            btn = QPushButton(text)
            btn.setFixedHeight(40)
            btn.setCheckable(True)
            btn.setChecked(index == 0)  # 默认选中第一个
            
            if index == 0:
                btn_style = """
                    QPushButton {
                        background-color: #3498db;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        text-align: left;
                        padding-left: 15px;
                        font-weight: bold;
                    }
                """
            else:
                btn_style = """
                    QPushButton {
                        background-color: transparent;
                        color: #2c3e50;
                        border: none;
                        border-radius: 6px;
                        text-align: left;
                        padding-left: 15px;
                    }
                    QPushButton:hover {
                        background-color: #f5f5f5;
                    }
                """
            
            btn.setStyleSheet(btn_style)
            btn.clicked.connect(lambda checked=False, idx=index: self.switch_page(idx))
            self.nav_buttons.append(btn)
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # 系统状态
        status_group = QGroupBox("系统状态")
        status_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
                font-weight: bold;
                color: #2c3e50;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        status_layout = QVBoxLayout()
        
        status_items = [
            ("CPU使用率", "42%"),
            ("内存使用", "68%"),
            ("网络状态", "正常"),
            ("存储空间", "1.2TB/2TB")
        ]
        
        for label, value in status_items:
            item_layout = QHBoxLayout()
            item_label = QLabel(label)
            item_label.setStyleSheet("color: #7f8c8d; font-size: 12px;")
            item_value = QLabel(value)
            item_value.setStyleSheet("color: #2c3e50; font-weight: bold;")
            
            item_layout.addWidget(item_label)
            item_layout.addWidget(item_value)
            status_layout.addLayout(item_layout)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        return sidebar
    
    def switch_page(self, index):
        """切换页面"""
        # 更新导航按钮状态
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
            if i == index:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #3498db;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        text-align: left;
                        padding-left: 15px;
                        font-weight: bold;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: #2c3e50;
                        border: none;
                        border-radius: 6px;
                        text-align: left;
                        padding-left: 15px;
                    }
                    QPushButton:hover {
                        background-color: #f5f5f5;
                    }
                """)
        
        # 切换页面
        self.stacked_widget.setCurrentIndex(index)
        
        # 更新状态栏
        page_names = ["仪表板", "用户管理", "数据报表", "系统设置", "安全中心", "文档中心", "帮助支持"]
        self.status_label.setText(f"当前页面: {page_names[index]}")
    
    def create_dashboard_page(self):
        """创建仪表板页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 仪表板卡片
        dashboard_cards = self.create_dashboard_cards()
        layout.addWidget(dashboard_cards)
        
        # 数据表格区域
        data_section = self.create_data_section()
        layout.addWidget(data_section, 1)  # 拉伸因子
        
        return page
    
    def create_dashboard_cards(self):
        """创建仪表板卡片"""
        cards_widget = QWidget()
        cards_layout = QGridLayout(cards_widget)
        cards_layout.setSpacing(15)
        
        # 定义卡片数据
        cards_data = [
            {
                "title": "舆情热度指数",
                "value": "78.5",
                "change": "+2.3%",
                "icon": "📈",
                "color": "#3498db"
            },
            {
                "title": "敏感信息检测",
                "value": "125",
                "change": "+15",
                "icon": "⚠️",
                "color": "#e74c3c"
            },
            {
                "title": "虚假信息识别",
                "value": "89",
                "change": "+8",
                "icon": "❌",
                "color": "#f39c12"
            },
            {
                "title": "情感分析",
                "value": "45%",
                "change": "正面",
                "icon": "😊",
                "color": "#2ecc71"
            },
            {
                "title": "风险预警",
                "value": "12",
                "change": "高风险",
                "icon": "🚨",
                "color": "#9b59b6"
            },
            {
                "title": "处理效率",
                "value": "98.5%",
                "change": "+1.2%",
                "icon": "⚡",
                "color": "#1abc9c"
            }
        ]
        
        # 创建卡片
        for i, card_data in enumerate(cards_data):
            card = self.create_card(**card_data)
            cards_layout.addWidget(card, i // 3, i % 3)
        
        return cards_widget
    
    def create_card(self, title, value, change, icon, color):
        """创建单个卡片"""
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        style_sheet = """
            QFrame {{
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }}
            QFrame:hover {{
                border-color: {0};
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
        """.format(color)
        card.setStyleSheet(style_sheet)
        
        layout = QVBoxLayout(card)
        
        # 卡片顶部
        top_layout = QHBoxLayout()
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet(f"font-size: 24px; color: {color};")
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #7f8c8d; font-size: 14px;")
        
        top_layout.addWidget(icon_label)
        top_layout.addWidget(title_label)
        top_layout.addStretch()
        
        layout.addLayout(top_layout)
        
        # 卡片数值
        value_label = QLabel(value)
        value_label.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            margin: 10px 0;
        """)
        layout.addWidget(value_label)
        
        # 卡片变化
        change_layout = QHBoxLayout()
        
        change_label = QLabel(change)
        if "+" in change:
            change_label.setStyleSheet("color: #2ecc71; font-weight: bold;")
        else:
            change_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        
        change_text = QLabel("相比昨日")
        change_text.setStyleSheet("color: #95a5a6; font-size: 12px;")
        
        change_layout.addWidget(change_label)
        change_layout.addWidget(change_text)
        change_layout.addStretch()
        
        layout.addLayout(change_layout)
        
        return card
    
    def create_user_management_page(self):
        """创建用户管理页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("👥 用户管理")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 搜索和操作栏
        search_bar = QWidget()
        search_layout = QHBoxLayout(search_bar)
        search_layout.setSpacing(10)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("搜索用户...")
        search_input.setFixedWidth(300)
        search_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        add_user_btn = QPushButton("➕ 新增用户")
        add_user_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        add_user_btn.clicked.connect(self.add_user)
        
        import_btn = QPushButton("📤 导入用户")
        import_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        import_btn.clicked.connect(self.import_users)
        
        export_btn = QPushButton("📥 导出用户")
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        export_btn.clicked.connect(self.export_users)
        
        search_layout.addWidget(search_input)
        search_layout.addStretch()
        search_layout.addWidget(add_user_btn)
        search_layout.addWidget(import_btn)
        search_layout.addWidget(export_btn)
        
        layout.addWidget(search_bar)
        
        # 用户表格
        self.user_table = QTableWidget(10, 7)
        self.user_table.setHorizontalHeaderLabels(["ID", "用户名", "邮箱", "角色", "状态", "注册时间", "操作"])
        
        # 设置表格样式
        self.user_table.setStyleSheet("""
            QTableWidget {
                border: none;
                alternate-background-color: #f9f9f9;
                selection-background-color: #3498db;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #f1f1f1;
                padding: 8px;
                border: none;
                font-weight: bold;
                color: #2c3e50;
            }
        """)
        
        # 填充示例数据
        self.sample_users = [
            ["001", "admin", "admin@example.com", "管理员", "活跃", "2023-01-01"],
            ["002", "user1", "user1@example.com", "普通用户", "活跃", "2023-01-02"],
            ["003", "user2", "user2@example.com", "普通用户", "禁用", "2023-01-03"],
            ["004", "user3", "user3@example.com", "普通用户", "活跃", "2023-01-04"],
            ["005", "user4", "user4@example.com", "普通用户", "活跃", "2023-01-05"],
            ["006", "user5", "user5@example.com", "普通用户", "禁用", "2023-01-06"],
            ["007", "user6", "user6@example.com", "普通用户", "活跃", "2023-01-07"],
            ["008", "user7", "user7@example.com", "普通用户", "活跃", "2023-01-08"],
            ["009", "user8", "user8@example.com", "普通用户", "活跃", "2023-01-09"],
            ["010", "user9", "user9@example.com", "普通用户", "禁用", "2023-01-10"]
        ]
        
        self.populate_user_table()
        
        # 设置表格属性
        self.user_table.setAlternatingRowColors(True)
        self.user_table.horizontalHeader().setStretchLastSection(True)
        self.user_table.verticalHeader().setVisible(False)
        self.user_table.setShowGrid(False)
        self.user_table.setSortingEnabled(True)
        
        layout.addWidget(self.user_table, 1)
        
        return page
    
    def populate_user_table(self):
        """填充用户表格"""
        self.user_table.setRowCount(len(self.sample_users))
        for row, user_data in enumerate(self.sample_users):
            for col, cell_data in enumerate(user_data):
                item = QTableWidgetItem(cell_data)
                if col == 4:  # 状态列
                    if cell_data == "活跃":
                        item.setForeground(QColor("#2ecc71"))
                    elif cell_data == "禁用":
                        item.setForeground(QColor("#e74c3c"))
                self.user_table.setItem(row, col, item)
            
            # 添加操作按钮
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setSpacing(5)
            action_layout.setContentsMargins(0, 0, 0, 0)
            
            edit_btn = QPushButton("编辑")
            edit_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 4px 8px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_user(r))
            
            delete_btn = QPushButton("删除")
            delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 4px 8px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
            """)
            delete_btn.clicked.connect(lambda checked, r=row: self.delete_user(r))
            
            action_layout.addWidget(edit_btn)
            action_layout.addWidget(delete_btn)
            action_layout.addStretch()
            
            self.user_table.setCellWidget(row, 6, action_widget)
    
    def add_user(self):
        """新增用户"""
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QDialogButtonBox
        
        dialog = QDialog(self)
        dialog.setWindowTitle("新增用户")
        dialog.setGeometry(400, 300, 400, 300)
        
        layout = QFormLayout(dialog)
        
        # 用户名
        username_input = QLineEdit()
        username_input.setPlaceholderText("请输入用户名")
        layout.addRow("用户名:", username_input)
        
        # 邮箱
        email_input = QLineEdit()
        email_input.setPlaceholderText("请输入邮箱")
        layout.addRow("邮箱:", email_input)
        
        # 角色
        role_combo = QComboBox()
        role_combo.addItems(["普通用户", "管理员"])
        layout.addRow("角色:", role_combo)
        
        # 状态
        status_combo = QComboBox()
        status_combo.addItems(["活跃", "禁用"])
        layout.addRow("状态:", status_combo)
        
        # 按钮
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)
        
        if dialog.exec() == QDialog.Accepted:
            # 生成新ID
            new_id = f"{len(self.sample_users) + 1:03d}"
            # 获取用户输入
            username = username_input.text()
            email = email_input.text()
            role = role_combo.currentText()
            status = status_combo.currentText()
            # 获取当前日期
            from datetime import datetime
            register_date = datetime.now().strftime("%Y-%m-%d")
            
            # 添加新用户
            self.sample_users.append([new_id, username, email, role, status, register_date])
            # 更新表格
            self.populate_user_table()
            # 显示成功消息
            QMessageBox.information(self, "成功", "用户添加成功！")
    
    def edit_user(self, row):
        """编辑用户"""
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QDialogButtonBox
        
        user_data = self.sample_users[row]
        
        dialog = QDialog(self)
        dialog.setWindowTitle("编辑用户")
        dialog.setGeometry(400, 300, 400, 300)
        
        layout = QFormLayout(dialog)
        
        # 用户名
        username_input = QLineEdit(user_data[1])
        layout.addRow("用户名:", username_input)
        
        # 邮箱
        email_input = QLineEdit(user_data[2])
        layout.addRow("邮箱:", email_input)
        
        # 角色
        role_combo = QComboBox()
        role_combo.addItems(["普通用户", "管理员"])
        role_combo.setCurrentText(user_data[3])
        layout.addRow("角色:", role_combo)
        
        # 状态
        status_combo = QComboBox()
        status_combo.addItems(["活跃", "禁用"])
        status_combo.setCurrentText(user_data[4])
        layout.addRow("状态:", status_combo)
        
        # 按钮
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)
        
        if dialog.exec() == QDialog.Accepted:
            # 更新用户数据
            self.sample_users[row][1] = username_input.text()
            self.sample_users[row][2] = email_input.text()
            self.sample_users[row][3] = role_combo.currentText()
            self.sample_users[row][4] = status_combo.currentText()
            # 更新表格
            self.populate_user_table()
            # 显示成功消息
            QMessageBox.information(self, "成功", "用户更新成功！")
    
    def delete_user(self, row):
        """删除用户"""
        reply = QMessageBox.question(self, "确认删除", "确定要删除这个用户吗？",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 删除用户
            del self.sample_users[row]
            # 更新表格
            self.populate_user_table()
            # 显示成功消息
            QMessageBox.information(self, "成功", "用户删除成功！")
    
    def import_users(self):
        """导入用户"""
        from PySide6.QtWidgets import QFileDialog
        
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "CSV Files (*.csv);;Text Files (*.txt)")
        
        if file_path:
            try:
                import csv
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)  # 跳过表头
                    for row in reader:
                        if len(row) >= 5:
                            # 生成新ID
                            new_id = f"{len(self.sample_users) + 1:03d}"
                            # 添加新用户
                            self.sample_users.append([new_id, row[0], row[1], row[2], row[3], row[4]])
                # 更新表格
                self.populate_user_table()
                # 显示成功消息
                QMessageBox.information(self, "成功", "用户导入成功！")
            except Exception as e:
                QMessageBox.error(self, "错误", f"导入失败: {str(e)}")
    
    def export_users(self):
        """导出用户"""
        from PySide6.QtWidgets import QFileDialog
        
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "users.csv", "CSV Files (*.csv)")
        
        if file_path:
            try:
                import csv
                with open(file_path, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["用户名", "邮箱", "角色", "状态", "注册时间"])
                    for user in self.sample_users:
                        writer.writerow(user[1:])
                # 显示成功消息
                QMessageBox.information(self, "成功", "用户导出成功！")
            except Exception as e:
                QMessageBox.error(self, "错误", f"导出失败: {str(e)}")
    
    def create_data_section(self):
        """创建数据表格区域"""
        section = QFrame()
        section.setFrameShape(QFrame.StyledPanel)
        section.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout(section)
        
        # 区域标题
        section_header = QHBoxLayout()
        
        section_title = QLabel("📋 舆情数据明细")
        section_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        
        section_header.addWidget(section_title)
        section_header.addStretch()
        
        # 筛选控件
        filter_layout = QHBoxLayout()
        filter_layout.setSpacing(10)
        
        period_combo = QComboBox()
        period_combo.addItems(["今日", "本周", "本月", "本季度", "本年"])
        period_combo.setFixedWidth(120)
        
        export_btn = QPushButton("导出数据")
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        filter_layout.addWidget(period_combo)
        filter_layout.addWidget(export_btn)
        filter_layout.addStretch()
        
        section_header.addLayout(filter_layout)
        layout.addLayout(section_header)
        
        # 数据表格
        table = QTableWidget(10, 6)
        table.setHorizontalHeaderLabels(["ID", "关键词", "热度", "情感", "风险等级", "处理状态"])
        
        # 设置表格样式
        table.setStyleSheet("""
            QTableWidget {
                border: none;
                alternate-background-color: #f9f9f9;
                selection-background-color: #3498db;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #f1f1f1;
                padding: 8px;
                border: none;
                font-weight: bold;
                color: #2c3e50;
            }
        """)
        
        # 填充示例数据
        sample_data = [
            ["1001", "疫情", "95", "负面", "高风险", "已处理"],
            ["1002", "经济", "88", "中性", "中风险", "处理中"],
            ["1003", "教育", "75", "正面", "低风险", "已处理"],
            ["1004", "科技", "92", "正面", "低风险", "已处理"],
            ["1005", "医疗", "85", "负面", "中风险", "处理中"],
            ["1006", "环境", "78", "中性", "低风险", "已处理"],
            ["1007", "就业", "82", "负面", "中风险", "处理中"],
            ["1008", "房价", "90", "负面", "高风险", "已处理"],
            ["1009", "交通", "70", "中性", "低风险", "已处理"],
            ["1010", "安全", "86", "正面", "低风险", "已处理"]
        ]
        
        for row, row_data in enumerate(sample_data):
            for col, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                if col == 3:  # 情感列
                    if cell_data == "正面":
                        item.setForeground(QColor("#2ecc71"))
                    elif cell_data == "负面":
                        item.setForeground(QColor("#e74c3c"))
                    else:
                        item.setForeground(QColor("#f39c12"))
                elif col == 4:  # 风险等级
                    if cell_data == "高风险":
                        item.setForeground(QColor("#e74c3c"))
                    elif cell_data == "中风险":
                        item.setForeground(QColor("#f39c12"))
                    else:
                        item.setForeground(QColor("#2ecc71"))
                elif col == 5:  # 处理状态
                    if cell_data == "已处理":
                        item.setForeground(QColor("#2ecc71"))
                    else:
                        item.setForeground(QColor("#f39c12"))
                table.setItem(row, col, item)
        
        # 设置表格属性
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        table.setSortingEnabled(True)
        
        layout.addWidget(table)
        
        return section
    
    def create_data_report_page(self):
        """创建数据报表页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("📊 数据报表")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 报表筛选栏
        filter_bar = QWidget()
        filter_layout = QHBoxLayout(filter_bar)
        filter_layout.setSpacing(10)
        
        self.period_combo = QComboBox()
        self.period_combo.addItems(["今日", "本周", "本月", "本季度", "本年", "自定义"])
        self.period_combo.setFixedWidth(120)
        
        self.report_type_combo = QComboBox()
        self.report_type_combo.addItems(["舆情热度报表", "情感分析报表", "风险预警报表", "处理效率报表"])
        self.report_type_combo.setFixedWidth(150)
        
        generate_btn = QPushButton("生成报表")
        generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        generate_btn.clicked.connect(self.generate_report)
        
        export_pdf_btn = QPushButton("导出PDF")
        export_pdf_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        export_pdf_btn.clicked.connect(self.export_pdf)
        
        export_excel_btn = QPushButton("导出Excel")
        export_excel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        export_excel_btn.clicked.connect(self.export_excel)
        
        filter_layout.addWidget(self.period_combo)
        filter_layout.addWidget(self.report_type_combo)
        filter_layout.addStretch()
        filter_layout.addWidget(generate_btn)
        filter_layout.addWidget(export_pdf_btn)
        filter_layout.addWidget(export_excel_btn)
        
        layout.addWidget(filter_bar)
        
        # 报表内容区域
        self.report_content = QFrame()
        self.report_content.setFrameShape(QFrame.StyledPanel)
        self.report_content.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        self.report_layout = QVBoxLayout(self.report_content)
        
        # 初始显示报表
        self.generate_report()
        
        layout.addWidget(self.report_content, 1)
        
        return page
    
    def generate_report(self):
        """生成报表"""
        # 清空当前报表内容
        while self.report_layout.count() > 0:
            item = self.report_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # 获取选择的时间范围和报表类型
        period = self.period_combo.currentText()
        report_type = self.report_type_combo.currentText()
        
        # 报表标题
        report_title = QLabel(f"{report_type} - {period}")
        report_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        self.report_layout.addWidget(report_title)
        
        # 报表摘要
        summary_frame = QFrame()
        summary_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 15px;
                margin-bottom: 20px;
            }
        """)
        summary_layout = QHBoxLayout(summary_frame)
        
        # 舆情热度报表摘要
        if report_type == "舆情热度报表":
            summary_items = [
                ("最高热度", "95.8", "#3498db"),
                ("平均热度", "78.5", "#2ecc71"),
                ("热点数量", "125", "#f39c12"),
                ("趋势变化", "+2.3%", "#9b59b6")
            ]
        # 情感分析报表摘要
        elif report_type == "情感分析报表":
            summary_items = [
                ("正面情感", "45%", "#3498db"),
                ("负面情感", "30%", "#e74c3c"),
                ("中性情感", "25%", "#f39c12"),
                ("情感趋势", "稳定", "#9b59b6")
            ]
        # 风险预警报表摘要
        elif report_type == "风险预警报表":
            summary_items = [
                ("高风险", "12", "#e74c3c"),
                ("中风险", "35", "#f39c12"),
                ("低风险", "78", "#2ecc71"),
                ("预警率", "4.7%", "#9b59b6")
            ]
        # 处理效率报表
        else:
            summary_items = [
                ("处理率", "98.5%", "#3498db"),
                ("平均处理时间", "2.3小时", "#2ecc71"),
                ("处理完成", "125", "#f39c12"),
                ("处理中", "15", "#9b59b6")
            ]
        
        for label, value, color in summary_items:
            item_frame = QWidget()
            item_layout = QVBoxLayout(item_frame)
            item_label = QLabel(label)
            item_label.setStyleSheet("color: #6c757d; font-size: 12px;")
            item_value = QLabel(value)
            item_value.setStyleSheet(f"color: {color}; font-size: 18px; font-weight: bold;")
            item_layout.addWidget(item_label)
            item_layout.addWidget(item_value)
            summary_layout.addWidget(item_frame)
        
        summary_layout.addStretch()
        self.report_layout.addWidget(summary_frame)
        
        # 图表区域
        chart_frame = QFrame()
        chart_frame.setFixedHeight(300)
        chart_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 15px;
                margin-bottom: 20px;
            }
        """)
        chart_layout = QVBoxLayout(chart_frame)
        
        chart_title = QLabel("📈 数据趋势图表")
        chart_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;")
        chart_layout.addWidget(chart_title)
        
        # 图表占位
        chart_placeholder = QFrame()
        chart_placeholder.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px dashed #dee2e6;
                border-radius: 6px;
            }
        """)
        
        chart_placeholder_label = QLabel("图表展示区域")
        chart_placeholder_label.setStyleSheet("font-size: 14px; color: #6c757d;")
        chart_placeholder_layout = QVBoxLayout(chart_placeholder)
        chart_placeholder_layout.addWidget(chart_placeholder_label)
        chart_placeholder_layout.setAlignment(Qt.AlignCenter)
        
        chart_layout.addWidget(chart_placeholder)
        self.report_layout.addWidget(chart_frame)
        
        # 数据表格
        if report_type == "舆情热度报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["关键词", "热度值", "趋势", "处理状态"])
            
            # 填充示例数据
            sample_report = [
                ["疫情", "95.8", "上升", "已处理"],
                ["经济", "88.5", "稳定", "处理中"],
                ["教育", "75.2", "下降", "已处理"],
                ["科技", "92.3", "上升", "已处理"],
                ["医疗", "85.7", "稳定", "处理中"],
                ["环境", "78.9", "下降", "已处理"],
                ["就业", "82.1", "上升", "处理中"],
                ["房价", "90.4", "稳定", "已处理"],
                ["交通", "70.5", "下降", "已处理"],
                ["安全", "86.3", "上升", "已处理"]
            ]
        elif report_type == "情感分析报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["关键词", "正面", "负面", "中性"])
            
            # 填充示例数据
            sample_report = [
                ["疫情", "35%", "55%", "10%"],
                ["经济", "40%", "30%", "30%"],
                ["教育", "60%", "20%", "20%"],
                ["科技", "75%", "15%", "10%"],
                ["医疗", "45%", "40%", "15%"],
                ["环境", "50%", "30%", "20%"],
                ["就业", "30%", "50%", "20%"],
                ["房价", "25%", "65%", "10%"],
                ["交通", "45%", "35%", "20%"],
                ["安全", "65%", "20%", "15%"]
            ]
        elif report_type == "风险预警报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["关键词", "风险等级", "预警时间", "处理状态"])
            
            # 填充示例数据
            sample_report = [
                ["疫情", "高风险", "2023-10-15", "已处理"],
                ["经济", "中风险", "2023-10-14", "处理中"],
                ["教育", "低风险", "2023-10-13", "已处理"],
                ["科技", "低风险", "2023-10-12", "已处理"],
                ["医疗", "中风险", "2023-10-11", "处理中"],
                ["环境", "低风险", "2023-10-10", "已处理"],
                ["就业", "中风险", "2023-10-09", "处理中"],
                ["房价", "高风险", "2023-10-08", "已处理"],
                ["交通", "低风险", "2023-10-07", "已处理"],
                ["安全", "低风险", "2023-10-06", "已处理"]
            ]
        else:  # 处理效率报表
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["关键词", "处理时间", "处理状态", "处理人员"])
            
            # 填充示例数据
            sample_report = [
                ["疫情", "1.5小时", "已处理", "管理员"],
                ["经济", "2.3小时", "处理中", "用户1"],
                ["教育", "1.2小时", "已处理", "用户2"],
                ["科技", "1.8小时", "已处理", "用户3"],
                ["医疗", "2.5小时", "处理中", "用户4"],
                ["环境", "1.0小时", "已处理", "用户5"],
                ["就业", "2.0小时", "处理中", "用户6"],
                ["房价", "1.7小时", "已处理", "用户7"],
                ["交通", "0.9小时", "已处理", "用户8"],
                ["安全", "1.3小时", "已处理", "用户9"]
            ]
        
        # 设置表格样式
        self.report_table.setStyleSheet("""
            QTableWidget {
                border: none;
                alternate-background-color: #f9f9f9;
                selection-background-color: #3498db;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #f1f1f1;
                padding: 8px;
                border: none;
                font-weight: bold;
                color: #2c3e50;
            }
        """)
        
        # 填充表格数据
        for row, row_data in enumerate(sample_report):
            for col, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                if report_type == "舆情热度报表" and col == 2:
                    if cell_data == "上升":
                        item.setForeground(QColor("#2ecc71"))
                    elif cell_data == "下降":
                        item.setForeground(QColor("#e74c3c"))
                    else:
                        item.setForeground(QColor("#f39c12"))
                elif report_type == "风险预警报表" and col == 1:
                    if cell_data == "高风险":
                        item.setForeground(QColor("#e74c3c"))
                    elif cell_data == "中风险":
                        item.setForeground(QColor("#f39c12"))
                    else:
                        item.setForeground(QColor("#2ecc71"))
                elif (report_type == "舆情热度报表" or report_type == "风险预警报表" or report_type == "处理效率报表") and col == 3:
                    if cell_data == "已处理":
                        item.setForeground(QColor("#2ecc71"))
                    else:
                        item.setForeground(QColor("#f39c12"))
                self.report_table.setItem(row, col, item)
        
        # 设置表格属性
        self.report_table.setAlternatingRowColors(True)
        self.report_table.horizontalHeader().setStretchLastSection(True)
        self.report_table.verticalHeader().setVisible(False)
        self.report_table.setShowGrid(False)
        
        self.report_layout.addWidget(self.report_table)
        
        # 显示生成成功消息
        if hasattr(self, 'status_label'):
            self.status_label.setText(f"报表生成成功: {report_type} - {period}")
            QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
    
    def export_pdf(self):
        """导出PDF"""
        from PySide6.QtWidgets import QFileDialog
        
        file_path, _ = QFileDialog.getSaveFileName(self, "保存PDF文件", "report.pdf", "PDF Files (*.pdf)")
        
        if file_path:
            try:
                # 模拟PDF导出
                import time
                time.sleep(1)  # 模拟导出过程
                QMessageBox.information(self, "成功", "PDF导出成功！")
                if hasattr(self, 'status_label'):
                    self.status_label.setText("PDF导出成功")
                    QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
            except Exception as e:
                QMessageBox.error(self, "错误", f"导出失败: {str(e)}")
    
    def export_excel(self):
        """导出Excel"""
        from PySide6.QtWidgets import QFileDialog
        
        file_path, _ = QFileDialog.getSaveFileName(self, "保存Excel文件", "report.xlsx", "Excel Files (*.xlsx)")
        
        if file_path:
            try:
                # 模拟Excel导出
                import time
                time.sleep(1)  # 模拟导出过程
                QMessageBox.information(self, "成功", "Excel导出成功！")
                if hasattr(self, 'status_label'):
                    self.status_label.setText("Excel导出成功")
                    QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
            except Exception as e:
                QMessageBox.error(self, "错误", f"导出失败: {str(e)}")
    
    def apply_modern_style(self):
        """应用现代化样式"""
        # 设置调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f8f9fa"))
        palette.setColor(QPalette.WindowText, QColor("#212529"))
        palette.setColor(QPalette.Base, QColor("#ffffff"))
        palette.setColor(QPalette.AlternateBase, QColor("#f8f9fa"))
        palette.setColor(QPalette.ToolTipBase, QColor("#212529"))
        palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#212529"))
        palette.setColor(QPalette.Button, QColor("#6c757d"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#007bff"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        
        self.setPalette(palette)
        
        # 设置全局样式表
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QPushButton {
                font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            }
            QLabel {
                font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            }
            QTableWidget {
                font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            }
        """)
    
    def create_system_settings_page(self):
        """创建系统设置页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 页面标题
        title = QLabel("⚙️ 系统设置")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        # 设置容器
        settings_container = QWidget()
        settings_layout = QVBoxLayout(settings_container)
        settings_layout.setSpacing(15)
        settings_layout.setContentsMargins(0, 0, 0, 20)
        
        # 基本设置
        basic_group = QGroupBox("基本设置")
        basic_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 0;
                padding: 15px;
                font-weight: bold;
                color: #2c3e50;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        basic_layout = QVBoxLayout()
        
        # 语言设置
        language_layout = QHBoxLayout()
        language_label = QLabel("语言:")
        language_label.setFixedWidth(100)
        language_combo = QComboBox()
        language_combo.addItems(["简体中文", "English"])
        language_layout.addWidget(language_label)
        language_layout.addWidget(language_combo)
        basic_layout.addLayout(language_layout)
        
        # 时区设置
        timezone_layout = QHBoxLayout()
        timezone_label = QLabel("时区:")
        timezone_label.setFixedWidth(100)
        timezone_combo = QComboBox()
        timezone_combo.addItems(["Asia/Shanghai", "America/New_York", "Europe/London"])
        timezone_layout.addWidget(timezone_label)
        timezone_layout.addWidget(timezone_combo)
        basic_layout.addLayout(timezone_layout)
        
        # 日期格式
        date_format_layout = QHBoxLayout()
        date_format_label = QLabel("日期格式:")
        date_format_label.setFixedWidth(100)
        date_format_combo = QComboBox()
        date_format_combo.addItems(["YYYY-MM-DD", "DD/MM/YYYY", "MM/DD/YYYY"])
        date_format_layout.addWidget(date_format_label)
        date_format_layout.addWidget(date_format_combo)
        basic_layout.addLayout(date_format_layout)
        
        basic_group.setLayout(basic_layout)
        settings_layout.addWidget(basic_group)
        
        # 通知设置
        notification_group = QGroupBox("通知设置")
        notification_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 15px;
                padding: 15px;
                font-weight: bold;
                color: #2c3e50;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        notification_layout = QVBoxLayout()
        
        # 邮件通知
        email_notification = QCheckBox("启用邮件通知")
        email_notification.setChecked(True)
        notification_layout.addWidget(email_notification)
        
        # 短信通知
        sms_notification = QCheckBox("启用短信通知")
        sms_notification.setChecked(False)
        notification_layout.addWidget(sms_notification)
        
        # 系统通知
        system_notification = QCheckBox("启用系统通知")
        system_notification.setChecked(True)
        notification_layout.addWidget(system_notification)
        
        notification_group.setLayout(notification_layout)
        settings_layout.addWidget(notification_group)
        
        # 保存按钮
        save_btn = QPushButton("保存设置")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        save_btn.clicked.connect(lambda: QMessageBox.information(self, "成功", "设置保存成功！"))
        
        settings_layout.addWidget(save_btn)
        
        scroll_area.setWidget(settings_container)
        layout.addWidget(scroll_area, 1)
        
        return page
    
    def create_security_center_page(self):
        """创建安全中心页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 页面标题
        title = QLabel("🛡️ 安全中心")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 安全状态
        security_status = QFrame()
        security_status.setStyleSheet("""
            QFrame {
                background-color: #d4edda;
                border: 1px solid #c3e6cb;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        status_layout = QHBoxLayout(security_status)
        status_icon = QLabel("✅")
        status_icon.setStyleSheet("font-size: 24px;")
        status_text = QLabel("系统安全状态良好，未检测到异常")
        status_text.setStyleSheet("color: #155724; font-weight: bold;")
        status_layout.addWidget(status_icon)
        status_layout.addWidget(status_text)
        status_layout.addStretch()
        
        layout.addWidget(security_status)
        
        # 滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        # 安全设置
        security_settings = QWidget()
        security_layout = QVBoxLayout(security_settings)
        security_layout.setSpacing(15)
        security_layout.setContentsMargins(0, 0, 0, 20)
        
        # 密码设置
        password_group = QGroupBox("密码设置")
        password_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 0;
                padding: 15px;
                font-weight: bold;
                color: #2c3e50;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        password_layout = QVBoxLayout()
        
        # 密码强度
        password_strength = QCheckBox("启用密码强度检查")
        password_strength.setChecked(True)
        password_layout.addWidget(password_strength)
        
        # 密码过期
        password_expiry = QCheckBox("启用密码过期")
        password_expiry.setChecked(True)
        password_layout.addWidget(password_expiry)
        
        # 登录尝试限制
        login_attempts = QCheckBox("启用登录尝试限制")
        login_attempts.setChecked(True)
        password_layout.addWidget(login_attempts)
        
        password_group.setLayout(password_layout)
        security_layout.addWidget(password_group)
        
        # 访问控制
        access_group = QGroupBox("访问控制")
        access_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 15px;
                padding: 15px;
                font-weight: bold;
                color: #2c3e50;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        access_layout = QVBoxLayout()
        
        # IP白名单
        ip_whitelist = QCheckBox("启用IP白名单")
        ip_whitelist.setChecked(False)
        access_layout.addWidget(ip_whitelist)
        
        # 两步验证
        two_factor = QCheckBox("启用两步验证")
        two_factor.setChecked(False)
        access_layout.addWidget(two_factor)
        
        # 会话超时
        session_timeout = QCheckBox("启用会话超时")
        session_timeout.setChecked(True)
        access_layout.addWidget(session_timeout)
        
        access_group.setLayout(access_layout)
        security_layout.addWidget(access_group)
        
        # 保存按钮
        save_security_btn = QPushButton("保存安全设置")
        save_security_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        save_security_btn.clicked.connect(lambda: QMessageBox.information(self, "成功", "安全设置保存成功！"))
        
        security_layout.addWidget(save_security_btn)
        
        scroll_area.setWidget(security_settings)
        layout.addWidget(scroll_area, 1)
        
        return page
    
    def create_document_center_page(self):
        """创建文档中心页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("📚 文档中心")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 文档搜索
        search_bar = QWidget()
        search_layout = QHBoxLayout(search_bar)
        
        search_input = QLineEdit()
        search_input.setPlaceholderText("搜索文档...")
        search_input.setFixedWidth(300)
        search_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        search_btn = QPushButton("搜索")
        search_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        upload_btn = QPushButton("上传文档")
        upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_btn)
        search_layout.addWidget(upload_btn)
        search_layout.addStretch()
        
        layout.addWidget(search_bar)
        
        # 文档分类
        categories = QFrame()
        categories.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        categories_layout = QVBoxLayout(categories)
        
        # 分类标题
        categories_title = QLabel("文档分类")
        categories_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        categories_layout.addWidget(categories_title)
        
        # 分类列表
        category_items = [
            ("用户指南", "12 个文档"),
            ("API 文档", "8 个文档"),
            ("系统文档", "5 个文档"),
            ("培训资料", "7 个文档"),
            ("常见问题", "15 个文档")
        ]
        
        for category, count in category_items:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.setSpacing(10)
            
            item_icon = QLabel("📄")
            item_icon.setStyleSheet("font-size: 16px;")
            
            item_label = QLabel(category)
            item_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
            
            item_count = QLabel(count)
            item_count.setStyleSheet("color: #7f8c8d;")
            
            item_layout.addWidget(item_icon)
            item_layout.addWidget(item_label)
            item_layout.addStretch()
            item_layout.addWidget(item_count)
            
            categories_layout.addWidget(item_widget)
        
        layout.addWidget(categories)
        
        # 最近文档
        recent_docs = QFrame()
        recent_docs.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        recent_layout = QVBoxLayout(recent_docs)
        
        # 最近文档标题
        recent_title = QLabel("最近文档")
        recent_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        recent_layout.addWidget(recent_title)
        
        # 最近文档列表
        recent_items = [
            ("用户操作手册.pdf", "2023-10-15", "2.5MB"),
            ("API 接口文档.md", "2023-10-14", "1.2MB"),
            ("系统架构设计.docx", "2023-10-13", "3.8MB"),
            ("培训课程资料.pptx", "2023-10-12", "5.6MB")
        ]
        
        for doc, date, size in recent_items:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.setSpacing(10)
            
            item_icon = QLabel("📁")
            item_icon.setStyleSheet("font-size: 16px;")
            
            item_info = QWidget()
            info_layout = QVBoxLayout(item_info)
            info_layout.setContentsMargins(0, 0, 0, 0)
            
            doc_label = QLabel(doc)
            doc_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
            
            doc_meta = QLabel(f"{date} • {size}")
            doc_meta.setStyleSheet("font-size: 12px; color: #7f8c8d;")
            
            info_layout.addWidget(doc_label)
            info_layout.addWidget(doc_meta)
            
            download_btn = QPushButton("下载")
            download_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 4px 8px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            
            item_layout.addWidget(item_icon)
            item_layout.addWidget(item_info)
            item_layout.addStretch()
            item_layout.addWidget(download_btn)
            
            recent_layout.addWidget(item_widget)
        
        layout.addWidget(recent_docs)
        
        return page
    
    def create_help_support_page(self):
        """创建帮助支持页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("❓ 帮助支持")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 常见问题
        faq_section = QFrame()
        faq_section.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        faq_layout = QVBoxLayout(faq_section)
        
        # 常见问题标题
        faq_title = QLabel("常见问题")
        faq_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        faq_layout.addWidget(faq_title)
        
        # 常见问题列表
        faq_items = [
            "如何添加新用户？",
            "如何生成数据报表？",
            "如何设置系统通知？",
            "如何上传文档？",
            "如何导出数据？",
            "如何重置密码？",
            "如何查看系统日志？",
            "如何配置安全设置？"
        ]
        
        for question in faq_items:
            faq_item = QPushButton(question)
            faq_item.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #2c3e50;
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 10px 15px;
                    text-align: left;
                    font-weight: bold;
                    margin-bottom: 8px;
                }
                QPushButton:hover {
                    background-color: #f5f5f5;
                }
            """)
            faq_item.clicked.connect(lambda checked, q=question: QMessageBox.information(self, "问题", f"这是关于 '{q}' 的答案。"))
            faq_layout.addWidget(faq_item)
        
        layout.addWidget(faq_section)
        
        # 联系支持
        support_section = QFrame()
        support_section.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        support_layout = QVBoxLayout(support_section)
        
        # 联系支持标题
        support_title = QLabel("联系支持")
        support_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        support_layout.addWidget(support_title)
        
        # 联系方式
        contact_info = QWidget()
        contact_layout = QVBoxLayout(contact_info)
        
        contact_items = [
            ("📧 邮箱", "support@example.com"),
            ("📞 电话", "400-123-4567"),
            ("💬 在线客服", "工作时间: 9:00-18:00"),
            ("🌐 帮助中心", "https://help.example.com")
        ]
        
        for icon, info in contact_items:
            contact_item = QLabel(f"{icon} {info}")
            contact_item.setStyleSheet("font-size: 14px; color: #2c3e50; margin-bottom: 8px;")
            contact_layout.addWidget(contact_item)
        
        support_layout.addWidget(contact_info)
        
        # 提交问题按钮
        submit_btn = QPushButton("提交问题")
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
                margin-top: 15px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        submit_btn.clicked.connect(self.submit_issue)
        
        support_layout.addWidget(submit_btn)
        
        layout.addWidget(support_section)
        
        return page
    
    def submit_issue(self):
        """提交问题"""
        from PySide6.QtWidgets import QDialog, QTextEdit, QPushButton, QVBoxLayout, QLabel
        
        dialog = QDialog(self)
        dialog.setWindowTitle("提交问题")
        dialog.setGeometry(400, 300, 500, 400)
        
        layout = QVBoxLayout(dialog)
        
        # 问题标题
        title_label = QLabel("问题标题:")
        title_input = QLineEdit()
        title_input.setPlaceholderText("请输入问题标题")
        layout.addWidget(title_label)
        layout.addWidget(title_input)
        
        # 问题描述
        desc_label = QLabel("问题描述:")
        desc_input = QTextEdit()
        desc_input.setPlaceholderText("请详细描述您遇到的问题...")
        desc_input.setFixedHeight(200)
        layout.addWidget(desc_label)
        layout.addWidget(desc_input)
        
        # 联系方式
        contact_label = QLabel("联系方式:")
        contact_input = QLineEdit()
        contact_input.setPlaceholderText("请留下您的邮箱或电话")
        layout.addWidget(contact_label)
        layout.addWidget(contact_input)
        
        # 提交按钮
        submit_btn = QPushButton("提交")
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
                margin-top: 15px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        submit_btn.clicked.connect(dialog.accept)
        layout.addWidget(submit_btn)
        
        if dialog.exec() == dialog.Accepted:
            QMessageBox.information(self, "成功", "问题提交成功！我们会尽快处理您的问题。")
    
    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        
        file_actions = [
            ("新建", "Ctrl+N"),
            ("打开", "Ctrl+O"),
            ("保存", "Ctrl+S"),
            ("导出", "Ctrl+E"),
            ("退出", "Ctrl+Q")
        ]
        
        for text, shortcut in file_actions:
            action = QAction(text, self)
            if shortcut:
                action.setShortcut(shortcut)
            if text == "退出":
                action.triggered.connect(self.close)
            file_menu.addAction(action)
        
        # 工具菜单
        tools_menu = menubar.addMenu("工具")
        
        tool_actions = [
            "数据导入",
            "数据导出",
            "系统备份",
            "系统恢复"
        ]
        
        for text in tool_actions:
            action = QAction(text, self)
            tools_menu.addAction(action)
        
        # 视图菜单
        view_menu = menubar.addMenu("视图")
        
        view_actions = [
            "刷新",
            "重置视图",
            "全屏"
        ]
        
        for text in view_actions:
            action = QAction(text, self)
            view_menu.addAction(action)
        
        # 帮助菜单
        help_menu = menubar.addMenu("帮助")
        
        help_action = QAction("关于", self)
        help_action.triggered.connect(self.show_about)
        help_menu.addAction(help_action)
    
    def setup_toolbar(self):
        """设置工具栏"""
        toolbar = QToolBar("工具栏")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        tools = ["新建", "打开", "保存", "分析", "帮助"]
        
        for text in tools:
            action = QAction(text, self)
            toolbar.addAction(action)
    
    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        
        # 状态标签
        self.status_label = QLabel("系统就绪")
        statusbar.addWidget(self.status_label)
        
        # 系统时间
        self.time_label = QLabel()
        statusbar.addPermanentWidget(self.time_label)
        
        # 版本信息
        version_label = QLabel("版本 1.0.0")
        statusbar.addPermanentWidget(version_label)
    
    def setup_timers(self):
        """设置定时器"""
        # 系统时间更新定时器
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)  # 每秒更新一次
        
        # 初始化时间
        self.update_time()
    
    def update_time(self):
        """更新系统时间"""
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.time_label.setText(current_time)
    
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(self, "关于", "智言空间 - 网络舆情监控平台\n版本: 1.0.0\n\n基于 PySide6 开发的现代化仪表板系统\n用于网络舆情监控和分析")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())