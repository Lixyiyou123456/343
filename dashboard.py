#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 仪表板界面
现代化仪表板设计示例
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
    """现代化仪表板界面"""
    
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
        self.setWindowTitle("现代化仪表板")
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
        title_label = QLabel("📊 数据分析仪表板")
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
        search_input.setPlaceholderText("搜索...")
        search_input.setFixedWidth(200)
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
            btn.clicked.connect(lambda checked, idx=index: self.switch_page(idx))
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
                "title": "总用户数",
                "value": "2,847",
                "change": "+12.5%",
                "icon": "👥",
                "color": "#3498db"
            },
            {
                "title": "活跃用户",
                "value": "1,892",
                "change": "+8.3%",
                "icon": "🔥",
                "color": "#e74c3c"
            },
            {
                "title": "订单数量",
                "value": "5,623",
                "change": "+15.2%",
                "icon": "📦",
                "color": "#2ecc71"
            },
            {
                "title": "总收入",
                "value": "$42,580",
                "change": "+18.7%",
                "icon": "💰",
                "color": "#f39c12"
            },
            {
                "title": "转化率",
                "value": "3.8%",
                "change": "+0.4%",
                "icon": "📈",
                "color": "#9b59b6"
            },
            {
                "title": "满意度",
                "value": "4.6/5.0",
                "change": "+0.2",
                "icon": "⭐",
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
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }}
            QFrame:hover {{
                border-color: {color};
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
        """)
        
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
        
        change_text = QLabel("相比上月")
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
        
        section_title = QLabel("📋 数据明细")
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
        table.setHorizontalHeaderLabels(["ID", "用户", "产品", "金额", "日期", "状态"])
        
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
            ["1001", "张三", "产品A", "$125.00", "2023-10-15", "已完成"],
            ["1002", "李四", "产品B", "$89.50", "2023-10-14", "进行中"],
            ["1003", "王五", "产品C", "$245.00", "2023-10-13", "已完成"],
            ["1004", "赵六", "产品A", "$125.00", "2023-10-12", "已取消"],
            ["1005", "钱七", "产品B", "$89.50", "2023-10-11", "已完成"],
            ["1006", "孙八", "产品D", "$320.00", "2023-10-10", "进行中"],
            ["1007", "周九", "产品A", "$125.00", "2023-10-09", "已完成"],
            ["1008", "吴十", "产品C", "$245.00", "2023-10-08", "已完成"],
            ["1009", "郑十一", "产品B", "$89.50", "2023-10-07", "进行中"],
            ["1010", "王十二", "产品D", "$320.00", "2023-10-06", "已完成"]
        ]
        
        for row, row_data in enumerate(sample_data):
            for col, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                if col == 5:  # 状态列
                    if cell_data == "已完成":
                        item.setForeground(QColor("#2ecc71"))
                    elif cell_data == "进行中":
                        item.setForeground(QColor("#f39c12"))
                    elif cell_data == "已取消":
                        item.setForeground(QColor("#e74c3c"))
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
        self.report_type_combo.addItems(["销售报表", "用户报表", "订单报表", "库存报表"])
        self.report_type_combo.setFixedWidth(120)
        
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
        
        # 销售报表摘要
        if report_type == "销售报表":
            summary_items = [
                ("总销售额", "$125,480", "#3498db"),
                ("订单数量", "1,245", "#2ecc71"),
                ("平均客单价", "$100.8", "#f39c12"),
                ("转化率", "4.2%", "#9b59b6")
            ]
        # 用户报表摘要
        elif report_type == "用户报表":
            summary_items = [
                ("总用户数", "2,847", "#3498db"),
                ("新增用户", "156", "#2ecc71"),
                ("活跃用户", "1,892", "#f39c12"),
                ("留存率", "66.5%", "#9b59b6")
            ]
        # 订单报表摘要
        elif report_type == "订单报表":
            summary_items = [
                ("总订单数", "5,623", "#3498db"),
                ("已完成", "4,892", "#2ecc71"),
                ("进行中", "543", "#f39c12"),
                ("已取消", "188", "#9b59b6")
            ]
        # 库存报表
        else:
            summary_items = [
                ("总库存", "12,543", "#3498db"),
                ("库存预警", "128", "#e74c3c"),
                ("库存周转率", "3.2", "#f39c12"),
                ("平均库存", "8,756", "#9b59b6")
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
        if report_type == "销售报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["日期", "销售额", "订单数", "转化率"])
            
            # 填充示例数据
            sample_report = [
                ["2023-10-01", "$12,500", "120", "3.8%"],
                ["2023-10-02", "$13,200", "125", "4.1%"],
                ["2023-10-03", "$11,800", "115", "3.6%"],
                ["2023-10-04", "$14,500", "135", "4.3%"],
                ["2023-10-05", "$12,900", "122", "3.9%"],
                ["2023-10-06", "$13,800", "128", "4.0%"],
                ["2023-10-07", "$15,200", "140", "4.5%"],
                ["2023-10-08", "$14,100", "132", "4.2%"],
                ["2023-10-09", "$12,700", "120", "3.8%"],
                ["2023-10-10", "$13,500", "125", "4.0%"]
            ]
        elif report_type == "用户报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["日期", "新增用户", "活跃用户", "留存率"])
            
            # 填充示例数据
            sample_report = [
                ["2023-10-01", "15", "1,245", "68.5%"],
                ["2023-10-02", "18", "1,260", "69.2%"],
                ["2023-10-03", "12", "1,230", "67.8%"],
                ["2023-10-04", "20", "1,275", "70.1%"],
                ["2023-10-05", "16", "1,255", "69.5%"],
                ["2023-10-06", "14", "1,240", "68.8%"],
                ["2023-10-07", "22", "1,280", "70.5%"],
                ["2023-10-08", "17", "1,265", "69.8%"],
                ["2023-10-09", "13", "1,235", "68.2%"],
                ["2023-10-10", "19", "1,270", "70.0%"]
            ]
        elif report_type == "订单报表":
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["日期", "订单数", "已完成", "已取消"])
            
            # 填充示例数据
            sample_report = [
                ["2023-10-01", "120", "105", "5"],
                ["2023-10-02", "125", "110", "4"],
                ["2023-10-03", "115", "100", "6"],
                ["2023-10-04", "135", "120", "5"],
                ["2023-10-05", "122", "108", "4"],
                ["2023-10-06", "128", "115", "3"],
                ["2023-10-07", "140", "125", "5"],
                ["2023-10-08", "132", "118", "4"],
                ["2023-10-09", "120", "105", "5"],
                ["2023-10-10", "125", "110", "4"]
            ]
        else:  # 库存报表
            self.report_table = QTableWidget(10, 4)
            self.report_table.setHorizontalHeaderLabels(["产品", "库存数量", "库存状态", "最后更新"])
            
            # 填充示例数据
            sample_report = [
                ["产品A", "1,250", "正常", "2023-10-10"],
                ["产品B", "850", "正常", "2023-10-10"],
                ["产品C", "120", "预警", "2023-10-09"],
                ["产品D", "3,200", "正常", "2023-10-10"],
                ["产品E", "95", "预警", "2023-10-08"],
                ["产品F", "2,100", "正常", "2023-10-10"],
                ["产品G", "75", "预警", "2023-10-07"],
                ["产品H", "1,500", "正常", "2023-10-10"],
                ["产品I", "210", "正常", "2023-10-09"],
                ["产品J", "150", "预警", "2023-10-08"]
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
                if report_type == "库存报表" and col == 2:
                    if cell_data == "预警":
                        item.setForeground(QColor("#e74c3c"))
                    else:
                        item.setForeground(QColor("#2ecc71"))
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
        
        # 页面标题
        title = QLabel("⚙️ 系统设置")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 设置容器
        settings_container = QFrame()
        settings_container.setFrameShape(QFrame.StyledPanel)
        settings_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        settings_layout = QVBoxLayout(settings_container)
        
        # 基本设置
        basic_group = QGroupBox("基本设置")
        basic_group.setStyleSheet("""
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
        
        notification_layout = QVBoxLayout()
        
        # 启用通知
        enable_notification = QCheckBox("启用通知")
        enable_notification.setChecked(True)
        notification_layout.addWidget(enable_notification)
        
        # 邮件通知
        email_notification = QCheckBox("邮件通知")
        email_notification.setChecked(True)
        notification_layout.addWidget(email_notification)
        
        # 短信通知
        sms_notification = QCheckBox("短信通知")
        sms_notification.setChecked(False)
        notification_layout.addWidget(sms_notification)
        
        notification_group.setLayout(notification_layout)
        settings_layout.addWidget(notification_group)
        
        # 存储设置
        storage_group = QGroupBox("存储设置")
        storage_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 15px;
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
        
        storage_layout = QVBoxLayout()
        
        # 数据存储路径
        storage_path_layout = QHBoxLayout()
        storage_path_label = QLabel("数据存储路径:")
        storage_path_label.setFixedWidth(120)
        storage_path_input = QLineEdit()
        storage_path_input.setText("C:/ProgramData/MyApp")
        storage_path_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 6px 12px;
            }
        """)
        browse_btn = QPushButton("浏览")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        storage_path_layout.addWidget(storage_path_label)
        storage_path_layout.addWidget(storage_path_input)
        storage_path_layout.addWidget(browse_btn)
        storage_layout.addLayout(storage_path_layout)
        
        # 自动备份
        auto_backup = QCheckBox("启用自动备份")
        auto_backup.setChecked(True)
        storage_layout.addWidget(auto_backup)
        
        # 备份频率
        backup_frequency_layout = QHBoxLayout()
        backup_frequency_label = QLabel("备份频率:")
        backup_frequency_label.setFixedWidth(120)
        backup_frequency_combo = QComboBox()
        backup_frequency_combo.addItems(["每天", "每周", "每月"])
        backup_frequency_layout.addWidget(backup_frequency_label)
        backup_frequency_layout.addWidget(backup_frequency_combo)
        storage_layout.addLayout(backup_frequency_layout)
        
        storage_group.setLayout(storage_layout)
        settings_layout.addWidget(storage_group)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        save_btn = QPushButton("保存设置")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        reset_btn = QPushButton("重置默认")
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(reset_btn)
        button_layout.addWidget(cancel_btn)
        
        settings_layout.addLayout(button_layout)
        
        layout.addWidget(settings_container, 1)
        
        return page
    
    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        
        new_action = QAction("新建项目", self)
        file_menu.addAction(new_action)
        
        import_action = QAction("导入数据", self)
        file_menu.addAction(import_action)
        
        export_action = QAction("导出报表", self)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 视图菜单
        view_menu = menubar.addMenu("视图")
        
        refresh_action = QAction("刷新数据", self)
        view_menu.addAction(refresh_action)
        
        fullscreen_action = QAction("全屏模式", self)
        view_menu.addAction(fullscreen_action)
        
        # 帮助菜单
        help_menu = menubar.addMenu("帮助")
        
        docs_action = QAction("使用文档", self)
        help_menu.addAction(docs_action)
        
        about_action = QAction("关于", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_toolbar(self):
        """设置工具栏"""
        toolbar = QToolBar("快速操作")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # 添加工具按钮
        actions = [
            ("刷新", "🔄"),
            ("新增", "➕"),
            ("编辑", "✏️"),
            ("删除", "🗑️"),
            ("打印", "🖨️"),
            ("设置", "⚙️")
        ]
        
        for text, icon in actions:
            btn = QPushButton(f"{icon} {text}")
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #495057;
                    border: 1px solid #dee2e6;
                    border-radius: 6px;
                    padding: 8px 12px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #f8f9fa;
                    border-color: #adb5bd;
                }
            """)
            toolbar.addWidget(btn)
    
    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        
        # 状态消息
        self.status_label = QLabel("系统就绪")
        statusbar.addWidget(self.status_label)
        
        # 系统时间
        self.time_label = QLabel()
        statusbar.addPermanentWidget(self.time_label)
        
        # 版本信息
        version_label = QLabel("v1.0.0")
        statusbar.addPermanentWidget(version_label)
    
    def setup_timers(self):
        """设置定时器"""
        # 更新时间
        self.update_time()
        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)  # 每秒更新一次
        
        # 模拟数据更新
        self.data_timer = QTimer()
        self.data_timer.timeout.connect(self.simulate_data_update)
        self.data_timer.start(5000)  # 每5秒模拟数据更新
    
    def update_time(self):
        """更新时间显示"""
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.time_label.setText(f"🕒 {current_time}")
    
    def simulate_data_update(self):
        """模拟数据更新"""
        # 在实际应用中，这里会从数据库或API获取最新数据
        self.status_label.setText("数据已更新")
        
        # 2秒后恢复状态
        QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
    
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self,
            "关于数据分析仪表板",
            "现代化数据分析仪表板\n\n"
            "这是一个使用 PySide6 开发的现代化仪表板界面示例。\n"
            "展示了现代化的UI设计、数据可视化和管理功能。\n\n"
            "主要功能：\n"
            "• 实时数据监控\n"
            "• 数据可视化展示\n"
            "• 用户行为分析\n"
            "• 系统状态监控\n\n"
            "版本: 1.0.0\n"
            "© 2023 数据分析团队"
        )
    
    def create_security_center_page(self):
        """创建安全中心页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("🛡️ 安全中心")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 安全状态卡片
        status_card = QFrame()
        status_card.setFrameShape(QFrame.StyledPanel)
        status_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        status_layout = QVBoxLayout(status_card)
        
        status_title = QLabel("安全状态")
        status_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        status_layout.addWidget(status_title)
        
        status_items = [
            ("系统安全", "安全", "#2ecc71"),
            ("账户安全", "安全", "#2ecc71"),
            ("网络安全", "安全", "#2ecc71"),
            ("数据安全", "安全", "#2ecc71"),
            ("防火墙", "已启用", "#2ecc71"),
            ("病毒防护", "已启用", "#2ecc71")
        ]
        
        for label, value, color in status_items:
            item_layout = QHBoxLayout()
            item_label = QLabel(label)
            item_label.setStyleSheet("color: #7f8c8d; font-size: 14px;")
            item_value = QLabel(value)
            item_value.setStyleSheet(f"color: {color}; font-weight: bold;")
            
            item_layout.addWidget(item_label)
            item_layout.addStretch()
            item_layout.addWidget(item_value)
            status_layout.addLayout(item_layout)
        
        layout.addWidget(status_card)
        
        # 安全设置
        security_settings = QFrame()
        security_settings.setFrameShape(QFrame.StyledPanel)
        security_settings.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        settings_layout = QVBoxLayout(security_settings)
        
        settings_title = QLabel("安全设置")
        settings_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        settings_layout.addWidget(settings_title)
        
        # 密码策略
        password_policy = QGroupBox("密码策略")
        password_policy.setStyleSheet("""
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
        
        password_layout = QVBoxLayout()
        
        # 密码长度
        password_length_layout = QHBoxLayout()
        password_length_label = QLabel("密码最小长度:")
        password_length_label.setFixedWidth(120)
        password_length_spin = QSpinBox()
        password_length_spin.setMinimum(6)
        password_length_spin.setMaximum(20)
        password_length_spin.setValue(8)
        password_length_layout.addWidget(password_length_label)
        password_length_layout.addWidget(password_length_spin)
        password_layout.addLayout(password_length_layout)
        
        # 密码复杂度
        password_complexity = QCheckBox("要求包含大小写字母、数字和特殊字符")
        password_complexity.setChecked(True)
        password_layout.addWidget(password_complexity)
        
        # 密码过期
        password_expiry_layout = QHBoxLayout()
        password_expiry_label = QLabel("密码过期时间:")
        password_expiry_label.setFixedWidth(120)
        password_expiry_combo = QComboBox()
        password_expiry_combo.addItems(["30天", "60天", "90天", "180天", "365天"])
        password_expiry_combo.setCurrentIndex(2)  # 默认90天
        password_expiry_layout.addWidget(password_expiry_label)
        password_expiry_layout.addWidget(password_expiry_combo)
        password_layout.addLayout(password_expiry_layout)
        
        password_policy.setLayout(password_layout)
        settings_layout.addWidget(password_policy)
        
        # 登录安全
        login_security = QGroupBox("登录安全")
        login_security.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                margin-top: 15px;
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
        
        login_layout = QVBoxLayout()
        
        # 登录失败限制
        login_attempts_layout = QHBoxLayout()
        login_attempts_label = QLabel("登录失败限制:")
        login_attempts_label.setFixedWidth(120)
        login_attempts_spin = QSpinBox()
        login_attempts_spin.setMinimum(1)
        login_attempts_spin.setMaximum(10)
        login_attempts_spin.setValue(5)
        login_attempts_layout.addWidget(login_attempts_label)
        login_attempts_layout.addWidget(login_attempts_spin)
        login_layout.addLayout(login_attempts_layout)
        
        # 登录超时
        login_timeout_layout = QHBoxLayout()
        login_timeout_label = QLabel("登录超时:")
        login_timeout_label.setFixedWidth(120)
        login_timeout_combo = QComboBox()
        login_timeout_combo.addItems(["15分钟", "30分钟", "1小时", "2小时", "4小时"])
        login_timeout_combo.setCurrentIndex(2)  # 默认1小时
        login_timeout_layout.addWidget(login_timeout_label)
        login_timeout_layout.addWidget(login_timeout_combo)
        login_layout.addLayout(login_timeout_layout)
        
        # 双因素认证
        two_factor_auth = QCheckBox("启用双因素认证")
        two_factor_auth.setChecked(False)
        login_layout.addWidget(two_factor_auth)
        
        login_security.setLayout(login_layout)
        settings_layout.addWidget(login_security)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        apply_btn = QPushButton("应用设置")
        apply_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(cancel_btn)
        
        settings_layout.addLayout(button_layout)
        
        layout.addWidget(security_settings, 1)
        
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
        search_layout.setSpacing(10)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索文档...")
        self.search_input.setStyleSheet("""
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
        search_btn.clicked.connect(self.search_documents)
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_btn)
        search_layout.addStretch()
        
        layout.addWidget(search_bar)
        
        # 文档分类
        categories = QFrame()
        categories.setFrameShape(QFrame.StyledPanel)
        categories.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        categories_layout = QVBoxLayout(categories)
        
        categories_title = QLabel("文档分类")
        categories_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        categories_layout.addWidget(categories_title)
        
        # 文档数据
        self.documents = {
            "使用指南": [
                {"title": "系统入门", "desc": "了解系统的基本功能和操作", "content": "系统入门文档内容..."},
                {"title": "用户注册", "desc": "如何注册和激活账号", "content": "用户注册文档内容..."},
                {"title": "登录系统", "desc": "如何登录和退出系统", "content": "登录系统文档内容..."},
                {"title": "个人设置", "desc": "如何修改个人信息和密码", "content": "个人设置文档内容..."}
            ],
            "管理员手册": [
                {"title": "系统配置", "desc": "系统参数配置和管理", "content": "系统配置文档内容..."},
                {"title": "用户管理", "desc": "如何管理系统用户", "content": "用户管理文档内容..."},
                {"title": "权限设置", "desc": "如何设置用户权限", "content": "权限设置文档内容..."},
                {"title": "系统监控", "desc": "系统运行状态监控", "content": "系统监控文档内容..."}
            ],
            "API文档": [
                {"title": "API概述", "desc": "API接口总体说明", "content": "API概述文档内容..."},
                {"title": "认证接口", "desc": "用户认证相关接口", "content": "认证接口文档内容..."},
                {"title": "数据接口", "desc": "数据操作相关接口", "content": "数据接口文档内容..."},
                {"title": "错误处理", "desc": "API错误码和处理方法", "content": "错误处理文档内容..."}
            ],
            "故障排除": [
                {"title": "常见问题", "desc": "系统常见问题及解决方案", "content": "常见问题文档内容..."},
                {"title": "错误提示", "desc": "系统错误提示及解决方法", "content": "错误提示文档内容..."},
                {"title": "性能优化", "desc": "系统性能优化建议", "content": "性能优化文档内容..."},
                {"title": "故障恢复", "desc": "系统故障恢复流程", "content": "故障恢复文档内容..."}
            ],
            "更新日志": [
                {"title": "v1.0.0", "desc": "系统初始版本", "content": "v1.0.0更新日志..."},
                {"title": "v1.0.1", "desc": "bug修复和性能优化", "content": "v1.0.1更新日志..."},
                {"title": "v1.0.2", "desc": "新增功能和界面优化", "content": "v1.0.2更新日志..."},
                {"title": "v1.1.0", "desc": "重大功能更新", "content": "v1.1.0更新日志..."}
            ],
            "最佳实践": [
                {"title": "系统使用技巧", "desc": "系统使用的实用技巧", "content": "系统使用技巧文档内容..."},
                {"title": "数据管理", "desc": "数据管理的最佳实践", "content": "数据管理文档内容..."},
                {"title": "安全防护", "desc": "系统安全防护建议", "content": "安全防护文档内容..."},
                {"title": "工作流程", "desc": "推荐的工作流程", "content": "工作流程文档内容..."}
            ]
        }
        
        doc_categories = [
            ("📖 使用指南", "了解系统的基本使用方法"),
            ("🛠️ 管理员手册", "系统管理和配置指南"),
            ("📚 API文档", "开发接口和集成指南"),
            ("🔧 故障排除", "常见问题和解决方案"),
            ("📝 更新日志", "系统更新和版本说明"),
            ("💡 最佳实践", "使用系统的最佳方法")
        ]
        
        for full_title, desc in doc_categories:
            icon = full_title.split(' ')[0]
            title = full_title.split(' ')[1]
            doc_item = QFrame()
            doc_item.setStyleSheet("""
                QFrame {
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 10px;
                }
                QFrame:hover {
                    background-color: #e9ecef;
                }
            """)
            
            doc_layout = QVBoxLayout(doc_item)
            
            doc_title = QLabel(f"{icon} {title}")
            doc_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 5px;")
            doc_desc = QLabel(desc)
            doc_desc.setStyleSheet("color: #6c757d; font-size: 14px;")
            
            doc_layout.addWidget(doc_title)
            doc_layout.addWidget(doc_desc)
            
            # 添加点击事件
            doc_item.mousePressEvent = lambda event, t=title: self.show_documents(t)
            
            categories_layout.addWidget(doc_item)
        
        # 文档列表区域
        self.doc_list_frame = QFrame()
        self.doc_list_frame.setFrameShape(QFrame.StyledPanel)
        self.doc_list_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
                margin-top: 15px;
            }
        """)
        
        self.doc_list_layout = QVBoxLayout(self.doc_list_frame)
        
        self.doc_list_title = QLabel("文档列表")
        self.doc_list_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        self.doc_list_layout.addWidget(self.doc_list_title)
        
        # 默认显示使用指南文档
        self.show_documents("使用指南")
        
        layout.addWidget(categories)
        layout.addWidget(self.doc_list_frame)
        
        return page
    
    def show_documents(self, category):
        """显示指定分类的文档列表"""
        # 清空当前文档列表
        while self.doc_list_layout.count() > 1:  # 保留标题
            item = self.doc_list_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
        
        # 更新标题
        self.doc_list_title.setText(f"{category}文档")
        
        # 添加文档列表
        if category in self.documents:
            for doc in self.documents[category]:
                doc_item = QFrame()
                doc_item.setStyleSheet("""
                    QFrame {
                        background-color: #f8f9fa;
                        border-radius: 8px;
                        padding: 15px;
                        margin-bottom: 10px;
                    }
                    QFrame:hover {
                        background-color: #e9ecef;
                    }
                """)
                
                doc_layout = QVBoxLayout(doc_item)
                
                doc_title = QLabel(doc["title"])
                doc_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50; margin-bottom: 5px;")
                doc_desc = QLabel(doc["desc"])
                doc_desc.setStyleSheet("color: #6c757d; font-size: 12px;")
                
                doc_layout.addWidget(doc_title)
                doc_layout.addWidget(doc_desc)
                
                # 添加点击事件
                doc_item.mousePressEvent = lambda event, d=doc: self.show_document_content(d)
                
                self.doc_list_layout.addWidget(doc_item)
        
        # 显示成功消息
        if hasattr(self, 'status_label'):
            self.status_label.setText(f"显示{category}文档")
            QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
    
    def show_document_content(self, doc):
        """显示文档内容"""
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QDialogButtonBox
        
        dialog = QDialog(self)
        dialog.setWindowTitle(doc["title"])
        dialog.setGeometry(400, 200, 800, 600)
        
        layout = QVBoxLayout(dialog)
        
        # 文档内容
        content_edit = QTextEdit()
        content_edit.setPlainText(doc["content"])
        content_edit.setReadOnly(True)
        content_edit.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 15px;
                font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
                font-size: 14px;
                line-height: 1.5;
            }
        """)
        layout.addWidget(content_edit)
        
        # 按钮
        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(dialog.accept)
        layout.addWidget(buttons)
        
        dialog.exec()
    
    def search_documents(self):
        """搜索文档"""
        keyword = self.search_input.text().strip()
        
        if not keyword:
            QMessageBox.warning(self, "提示", "请输入搜索关键词")
            return
        
        # 清空当前文档列表
        while self.doc_list_layout.count() > 1:  # 保留标题
            item = self.doc_list_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()
        
        # 更新标题
        self.doc_list_title.setText(f"搜索结果: {keyword}")
        
        # 搜索文档
        results = []
        for category, docs in self.documents.items():
            for doc in docs:
                if keyword.lower() in doc["title"].lower() or keyword.lower() in doc["desc"].lower() or keyword.lower() in doc["content"].lower():
                    results.append((category, doc))
        
        # 显示搜索结果
        if results:
            for category, doc in results:
                doc_item = QFrame()
                doc_item.setStyleSheet("""
                    QFrame {
                        background-color: #f8f9fa;
                        border-radius: 8px;
                        padding: 15px;
                        margin-bottom: 10px;
                    }
                    QFrame:hover {
                        background-color: #e9ecef;
                    }
                """)
                
                doc_layout = QVBoxLayout(doc_item)
                
                doc_title = QLabel(f"{category} - {doc['title']}")
                doc_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50; margin-bottom: 5px;")
                doc_desc = QLabel(doc["desc"])
                doc_desc.setStyleSheet("color: #6c757d; font-size: 12px;")
                
                doc_layout.addWidget(doc_title)
                doc_layout.addWidget(doc_desc)
                
                # 添加点击事件
                doc_item.mousePressEvent = lambda event, d=doc: self.show_document_content(d)
                
                self.doc_list_layout.addWidget(doc_item)
        else:
            # 没有找到结果
            no_result = QLabel("未找到相关文档")
            no_result.setStyleSheet("font-size: 14px; color: #6c757d; text-align: center; padding: 20px;")
            self.doc_list_layout.addWidget(no_result)
        
        # 显示成功消息
        if hasattr(self, 'status_label'):
            self.status_label.setText(f"搜索完成，找到 {len(results)} 个结果")
            QTimer.singleShot(2000, lambda: self.status_label.setText("系统就绪"))
    
    def create_help_support_page(self):
        """创建帮助支持页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(15)
        
        # 页面标题
        title = QLabel("❓ 帮助支持")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)
        
        # 帮助卡片
        help_card = QFrame()
        help_card.setFrameShape(QFrame.StyledPanel)
        help_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        help_layout = QVBoxLayout(help_card)
        
        help_title = QLabel("获取帮助")
        help_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        help_layout.addWidget(help_title)
        
        help_options = [
            ("📞 联系客服", "工作时间: 周一至周五 9:00-18:00", "400-123-4567"),
            ("📧 发送邮件", "support@example.com", "点击发送邮件"),
            ("💬 在线聊天", "实时客服支持", "立即聊天"),
            ("📅 预约支持", "安排一对一支持会话", "预约时间")
        ]
        
        for icon, title, action in help_options:
            option_frame = QFrame()
            option_frame.setStyleSheet("""
                QFrame {
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 10px;
                }
                QFrame:hover {
                    background-color: #e9ecef;
                }
            """)
            
            option_layout = QVBoxLayout(option_frame)
            
            option_title = QLabel(f"{icon} {title}")
            option_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50; margin-bottom: 5px;")
            option_action = QLabel(action)
            option_action.setStyleSheet("color: #3498db; font-size: 14px; text-decoration: underline;")
            
            option_layout.addWidget(option_title)
            option_layout.addWidget(option_action)
            
            help_layout.addWidget(option_frame)
        
        layout.addWidget(help_card)
        
        # 常见问题
        faq_card = QFrame()
        faq_card.setFrameShape(QFrame.StyledPanel)
        faq_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)
        
        faq_layout = QVBoxLayout(faq_card)
        
        faq_title = QLabel("常见问题")
        faq_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 15px;")
        faq_layout.addWidget(faq_title)
        
        faq_items = [
            "如何重置密码？",
            "如何添加新用户？",
            "如何导出数据报表？",
            "如何修改系统设置？",
            "如何启用双因素认证？",
            "如何备份数据？"
        ]
        
        for question in faq_items:
            faq_item = QPushButton(question)
            faq_item.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                    color: #2c3e50;
                    border: none;
                    border-radius: 6px;
                    padding: 12px 16px;
                    text-align: left;
                    font-size: 14px;
                    margin-bottom: 8px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                }
            """)
            faq_layout.addWidget(faq_item)
        
        layout.addWidget(faq_card, 1)
        
        return page


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle("Fusion")
    
    # 设置应用程序字体
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    # 创建并显示主窗口
    window = Dashboard()
    window.show()
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    main()