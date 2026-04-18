#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 简洁界面示例
专注于界面设计和布局
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget,
    QComboBox, QCheckBox, QRadioButton, QGroupBox, QTabWidget,
    QProgressBar, QSlider, QSpinBox, QTableWidget, QTableWidgetItem, QSplitter,
    QMessageBox, QMenuBar, QToolBar, QStatusBar, QFrame
)
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QFont, QPalette, QColor, QAction


class SimpleUI(QMainWindow):
    """简洁界面示例"""
    
    def __init__(self):
        super().__init__()
        self.user_fields = {}
        self.settings_checkboxes = {}
        self.data_table = None
        self.progress_bar = None
        self.stats_labels = {}
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()
        
    def setup_ui(self):
        """设置UI界面"""
        # 设置窗口属性
        self.setWindowTitle("PySide6 简洁界面")
        self.setGeometry(100, 100, 1000, 700)
        
        # 应用样式
        self.apply_styles()
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # 标题区域
        title_frame = QFrame()
        title_frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        title_layout = QVBoxLayout(title_frame)
        
        title_label = QLabel("PySide6 界面设计示例")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50; padding: 10px;")
        title_layout.addWidget(title_label)
        
        subtitle_label = QLabel("专注于界面布局和控件展示")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #7f8c8d; padding: 5px;")
        title_layout.addWidget(subtitle_label)
        
        main_layout.addWidget(title_frame)
        
        # 内容区域
        content_splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(content_splitter, 1)  # 1 表示拉伸因子
        
        # 左侧面板
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # 用户信息组
        user_group = QGroupBox("用户信息")
        user_group.setFont(QFont("Arial", 10, QFont.Bold))
        user_layout = QVBoxLayout()
        
        # 表单字段
        fields = [
            ("用户名:", QLineEdit()),
            ("邮箱:", QLineEdit()),
            ("电话:", QLineEdit()),
            ("地址:", QLineEdit())
        ]
        
        for label_text, widget in fields:
            field_layout = QHBoxLayout()
            label = QLabel(label_text)
            label.setFixedWidth(60)
            widget.setPlaceholderText(f"请输入{label_text[:-1]}...")
            field_layout.addWidget(label)
            field_layout.addWidget(widget)
            user_layout.addLayout(field_layout)
            # 存储字段引用
            field_name = label_text[:-1]
            self.user_fields[field_name] = widget
        
        user_group.setLayout(user_layout)
        left_layout.addWidget(user_group)
        
        # 设置组
        settings_group = QGroupBox("设置选项")
        settings_layout = QVBoxLayout()
        
        # 复选框
        checkboxes = [
            ("启用通知", True),
            ("自动保存", False),
            ("记住密码", True),
            ("深色模式", False)
        ]
        
        for text, checked in checkboxes:
            checkbox = QCheckBox(text)
            checkbox.setChecked(checked)
            settings_layout.addWidget(checkbox)
            # 存储复选框引用
            self.settings_checkboxes[text] = checkbox
        
        settings_group.setLayout(settings_layout)
        left_layout.addWidget(settings_group)
        
        # 按钮组
        button_layout = QHBoxLayout()
        
        btn_save = QPushButton("保存")
        btn_save.setStyleSheet(self.get_button_style("#27ae60"))
        btn_save.clicked.connect(self.save_settings)
        
        btn_reset = QPushButton("重置")
        btn_reset.setStyleSheet(self.get_button_style("#e74c3c"))
        btn_reset.clicked.connect(self.reset_settings)
        
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_reset)
        
        left_layout.addLayout(button_layout)
        left_layout.addStretch()
        
        content_splitter.addWidget(left_panel)
        
        # 右侧面板
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # 数据展示组
        data_group = QGroupBox("数据展示")
        data_layout = QVBoxLayout()
        
        # 表格
        self.data_table = QTableWidget(4, 3)
        self.data_table.setHorizontalHeaderLabels(["项目", "状态", "进度"])
        
        table_data = [
            ["任务 1", "进行中", "75%"],
            ["任务 2", "已完成", "100%"],
            ["任务 3", "待开始", "0%"],
            ["任务 4", "进行中", "45%"]
        ]
        
        for row, row_data in enumerate(table_data):
            for col, cell_data in enumerate(row_data):
                self.data_table.setItem(row, col, QTableWidgetItem(cell_data))
        
        data_layout.addWidget(self.data_table)
        
        # 进度条
        progress_layout = QVBoxLayout()
        progress_layout.addWidget(QLabel("总体进度:"))
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(65)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 3px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)
        
        data_layout.addLayout(progress_layout)
        data_group.setLayout(data_layout)
        right_layout.addWidget(data_group)
        
        # 统计信息组
        stats_group = QGroupBox("统计信息")
        stats_layout = QVBoxLayout()
        
        stats = [
            ("用户数量", "1,234"),
            ("活跃任务", "45"),
            ("完成率", "78%"),
            ("响应时间", "2.3s")
        ]
        
        for label_text, value_text in stats:
            stat_layout = QHBoxLayout()
            label = QLabel(label_text)
            label.setStyleSheet("font-weight: bold;")
            value = QLabel(value_text)
            value.setStyleSheet("color: #2980b9; font-size: 14px;")
            value.setAlignment(Qt.AlignRight)
            
            stat_layout.addWidget(label)
            stat_layout.addWidget(value)
            stats_layout.addLayout(stat_layout)
            # 存储统计信息标签
            self.stats_labels[label_text] = value
        
        stats_group.setLayout(stats_layout)
        right_layout.addWidget(stats_group)
        
        # 操作按钮
        action_layout = QHBoxLayout()
        
        actions = [
            ("刷新", "#3498db"),
            ("导出", "#9b59b6"),
            ("打印", "#e67e22"),
            ("帮助", "#95a5a6")
        ]
        
        for text, color in actions:
            btn = QPushButton(text)
            btn.setStyleSheet(self.get_button_style(color))
            # 添加点击事件
            if text == "刷新":
                btn.clicked.connect(self.refresh_data)
            elif text == "导出":
                btn.clicked.connect(self.export_data)
            elif text == "打印":
                btn.clicked.connect(self.print_data)
            elif text == "帮助":
                btn.clicked.connect(self.show_help)
            action_layout.addWidget(btn)
        
        right_layout.addLayout(action_layout)
        right_layout.addStretch()
        
        content_splitter.addWidget(right_panel)
        
        # 设置分割器比例
        content_splitter.setSizes([350, 650])
        
    def apply_styles(self):
        """应用全局样式"""
        # 设置调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#ecf0f1"))
        palette.setColor(QPalette.WindowText, QColor("#2c3e50"))
        palette.setColor(QPalette.Base, QColor("#ffffff"))
        palette.setColor(QPalette.AlternateBase, QColor("#f5f5f5"))
        palette.setColor(QPalette.ToolTipBase, QColor("#2c3e50"))
        palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#2c3e50"))
        palette.setColor(QPalette.Button, QColor("#3498db"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#3498db"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        
        self.setPalette(palette)
        
    def get_button_style(self, color):
        """获取按钮样式"""
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.darken_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.darken_color(color, 40)};
            }}
        """
    
    def darken_color(self, hex_color, amount=20):
        """加深颜色"""
        # 简化实现，实际应用中可以使用更复杂的颜色处理
        return hex_color
    
    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        
        file_actions = [
            ("新建", "Ctrl+N"),
            ("打开", "Ctrl+O"),
            ("保存", "Ctrl+S"),
            ("另存为", "Ctrl+Shift+S"),
            ("退出", "Ctrl+Q")
        ]
        
        for text, shortcut in file_actions:
            action = QAction(text, self)
            if shortcut:
                action.setShortcut(shortcut)
            if text == "退出":
                action.triggered.connect(self.close)
            file_menu.addAction(action)
        
        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        
        edit_actions = ["撤销", "重做", "剪切", "复制", "粘贴"]
        
        for text in edit_actions:
            action = QAction(text, self)
            edit_menu.addAction(action)
        
        # 视图菜单
        view_menu = menubar.addMenu("视图")
        
        view_actions = ["放大", "缩小", "重置缩放", "全屏"]
        
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
        
        # 工具按钮
        tools = ["新建", "打开", "保存", "打印", "帮助"]
        
        for text in tools:
            action = QAction(text, self)
            toolbar.addAction(action)
        
        toolbar.addSeparator()
        
        # 分隔线后添加更多工具
        more_tools = ["剪切", "复制", "粘贴"]
        
        for text in more_tools:
            action = QAction(text, self)
            toolbar.addAction(action)
        
    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        
        # 状态消息
        self.status_message = QLabel("就绪")
        statusbar.addWidget(self.status_message)
        
        # 系统信息
        system_info = QLabel("© 2023 PySide6 UI Demo")
        statusbar.addPermanentWidget(system_info)
        
    def show_status(self, message):
        """显示状态消息"""
        self.status_message.setText(message)
        
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self,
            "关于 PySide6 简洁界面",
            "PySide6 简洁界面示例\n\n"
            "这是一个专注于界面设计和布局的示例程序。\n"
            "展示了现代化的UI设计、合理的布局和美观的控件样式。\n\n"
            "主要特点：\n"
            "• 清晰的布局结构\n"
            "• 现代化的配色方案\n"
            "• 完整的界面组件\n"
            "• 响应式设计\n\n"
            "版本: 1.0.0"
        )
    
    def save_settings(self):
        """保存设置"""
        # 收集用户信息
        user_info = {}
        for field_name, widget in self.user_fields.items():
            user_info[field_name] = widget.text()
        
        # 收集设置选项
        settings = {}
        for setting_name, checkbox in self.settings_checkboxes.items():
            settings[setting_name] = checkbox.isChecked()
        
        # 检查深色模式
        if settings.get("深色模式", False):
            self.apply_dark_mode()
        else:
            self.apply_light_mode()
        
        # 显示保存成功消息
        QMessageBox.information(self, "保存成功", "用户信息和设置已保存！")
        self.show_status("设置已保存")
    
    def reset_settings(self):
        """重置设置"""
        # 清空用户信息
        for widget in self.user_fields.values():
            widget.clear()
        
        # 重置设置选项到默认值
        default_settings = {
            "启用通知": True,
            "自动保存": False,
            "记住密码": True,
            "深色模式": False
        }
        
        for setting_name, default_value in default_settings.items():
            if setting_name in self.settings_checkboxes:
                self.settings_checkboxes[setting_name].setChecked(default_value)
        
        # 确保使用浅色模式
        self.apply_light_mode()
        
        # 显示重置成功消息
        QMessageBox.information(self, "重置成功", "所有设置已重置为默认值！")
        self.show_status("设置已重置")
    
    def apply_light_mode(self):
        """应用浅色模式"""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#ecf0f1"))
        palette.setColor(QPalette.WindowText, QColor("#2c3e50"))
        palette.setColor(QPalette.Base, QColor("#ffffff"))
        palette.setColor(QPalette.AlternateBase, QColor("#f5f5f5"))
        palette.setColor(QPalette.ToolTipBase, QColor("#2c3e50"))
        palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#2c3e50"))
        palette.setColor(QPalette.Button, QColor("#3498db"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#3498db"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        
        self.setPalette(palette)
        
        # 更新表格样式
        if self.data_table:
            self.data_table.setStyleSheet("""
                QTableWidget {
                    background-color: #ffffff;
                    color: #2c3e50;
                    gridline-color: #bdc3c7;
                }
                QHeaderView::section {
                    background-color: #3498db;
                    color: #ffffff;
                    padding: 8px;
                    border: 1px solid #bdc3c7;
                }
            """)
        
        # 更新进度条样式
        if self.progress_bar:
            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 2px solid #bdc3c7;
                    border-radius: 5px;
                    text-align: center;
                    background-color: #ffffff;
                    color: #2c3e50;
                }
                QProgressBar::chunk {
                    background-color: #3498db;
                    border-radius: 3px;
                }
            """)
    
    def apply_dark_mode(self):
        """应用深色模式"""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2c3e50"))
        palette.setColor(QPalette.WindowText, QColor("#ecf0f1"))
        palette.setColor(QPalette.Base, QColor("#34495e"))
        palette.setColor(QPalette.AlternateBase, QColor("#2c3e50"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ecf0f1"))
        palette.setColor(QPalette.ToolTipText, QColor("#2c3e50"))
        palette.setColor(QPalette.Text, QColor("#ecf0f1"))
        palette.setColor(QPalette.Button, QColor("#3498db"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#3498db"))
        palette.setColor(QPalette.HighlightedText, QColor("#2c3e50"))
        
        self.setPalette(palette)
        
        # 更新表格样式
        if self.data_table:
            self.data_table.setStyleSheet("""
                QTableWidget {
                    background-color: #34495e;
                    color: #ecf0f1;
                    gridline-color: #2c3e50;
                }
                QHeaderView::section {
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    padding: 8px;
                    border: 1px solid #34495e;
                }
            """)
        
        # 更新进度条样式
        if self.progress_bar:
            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 2px solid #34495e;
                    border-radius: 5px;
                    text-align: center;
                    background-color: #2c3e50;
                    color: #ecf0f1;
                }
                QProgressBar::chunk {
                    background-color: #3498db;
                    border-radius: 3px;
                }
            """)
    
    def refresh_data(self):
        """刷新数据"""
        # 模拟数据刷新
        import random
        
        # 更新表格数据
        statuses = ["进行中", "已完成", "待开始"]
        for row in range(self.data_table.rowCount()):
            # 随机更新状态
            status = random.choice(statuses)
            self.data_table.setItem(row, 1, QTableWidgetItem(status))
            
            # 根据状态更新进度
            if status == "已完成":
                progress = "100%"
            elif status == "待开始":
                progress = "0%"
            else:
                progress = f"{random.randint(1, 99)}%"
            self.data_table.setItem(row, 2, QTableWidgetItem(progress))
        
        # 更新进度条
        new_progress = random.randint(0, 100)
        self.progress_bar.setValue(new_progress)
        
        # 更新统计信息
        self.stats_labels["用户数量"].setText(f"{random.randint(1000, 2000):,}")
        self.stats_labels["活跃任务"].setText(f"{random.randint(30, 60)}")
        self.stats_labels["完成率"].setText(f"{random.randint(60, 95)}%")
        self.stats_labels["响应时间"].setText(f"{random.uniform(1.0, 3.0):.1f}s")
        
        # 显示刷新成功消息
        QMessageBox.information(self, "刷新成功", "数据已更新！")
        self.show_status("数据已刷新")
    
    def export_data(self):
        """导出数据"""
        # 模拟导出功能
        import json
        import os
        
        # 收集表格数据
        table_data = []
        for row in range(self.data_table.rowCount()):
            row_data = []
            for col in range(self.data_table.columnCount()):
                item = self.data_table.item(row, col)
                row_data.append(item.text() if item else "")
            table_data.append(row_data)
        
        # 准备导出数据
        export_data = {
            "table_data": table_data,
            "progress": self.progress_bar.value(),
            "statistics": {}
        }
        
        for label, widget in self.stats_labels.items():
            export_data["statistics"][label] = widget.text()
        
        # 保存到文件
        export_path = os.path.join(os.path.expanduser("~"), "export_data.json")
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        # 显示导出成功消息
        QMessageBox.information(self, "导出成功", f"数据已导出到: {export_path}")
        self.show_status("数据已导出")
    
    def print_data(self):
        """打印数据"""
        # 模拟打印功能
        QMessageBox.information(self, "打印", "数据已发送到打印机！")
        self.show_status("数据已打印")
    
    def show_help(self):
        """显示帮助"""
        QMessageBox.information(
            self,
            "帮助",
            "PySide6 简洁界面使用说明\n\n"
            "1. 用户信息：填写个人信息\n"
            "2. 设置选项：配置应用程序设置\n"
            "3. 数据展示：查看任务进度和统计信息\n"
            "4. 操作按钮：\n"
            "   - 刷新：更新数据\n"
            "   - 导出：导出数据到文件\n"
            "   - 打印：打印数据\n"
            "   - 帮助：显示此帮助信息\n\n"
            "点击保存按钮保存设置，点击重置按钮恢复默认设置。"
        )
        self.show_status("显示帮助信息")


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle("Fusion")
    
    # 设置应用程序字体
    font = QFont("Microsoft YaHei", 9)
    app.setFont(font)
    
    # 创建并显示主窗口
    window = SimpleUI()
    window.show()
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    main()