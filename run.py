#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 界面启动器
选择运行不同的界面示例
"""

import sys
import subprocess
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFrame, QTextEdit, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor


class Launcher(QMainWindow):
    """界面启动器"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        """设置UI界面"""
        # 设置窗口属性
        self.setWindowTitle("PySide6 界面启动器")
        self.setGeometry(100, 100, 600, 500)
        
        # 应用样式
        self.apply_styles()
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # 标题
        title_label = QLabel("PySide6 界面示例启动器")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50; padding: 10px;")
        main_layout.addWidget(title_label)
        
        # 描述
        desc_label = QLabel("选择要运行的 PySide6 界面示例")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("color: #7f8c8d; font-size: 14px; padding: 5px;")
        main_layout.addWidget(desc_label)
        
        # 分隔线
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #bdc3c7;")
        main_layout.addWidget(separator)
        
        # 界面选择区域
        selection_widget = QWidget()
        selection_layout = QVBoxLayout(selection_widget)
        selection_layout.setSpacing(15)
        
        # 界面选项
        interfaces = [
            {
                "name": "完整功能界面",
                "file": "main.py",
                "description": "展示 PySide6 所有主要控件的完整示例，包含4个标签页和各种交互功能。",
                "color": "#3498db"
            },
            {
                "name": "简洁界面",
                "file": "simple_ui.py", 
                "description": "专注于界面设计和布局的简洁示例，现代化的配色方案和清晰的布局结构。",
                "color": "#2ecc71"
            },
            {
                "name": "现代化仪表板",
                "file": "dashboard.py",
                "description": "数据可视化和管理界面，卡片式布局设计，适合数据分析和管理类应用。",
                "color": "#9b59b6"
            }
        ]
        
        self.interface_buttons = []
        
        for interface in interfaces:
            # 创建界面选项卡片
            card = self.create_interface_card(interface)
            selection_layout.addWidget(card)
        
        main_layout.addWidget(selection_widget)
        
        # 按钮区域
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        
        # 安装依赖按钮
        install_btn = QPushButton("安装依赖")
        install_btn.setFixedHeight(40)
        install_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        install_btn.clicked.connect(self.install_dependencies)
        
        # 退出按钮
        exit_btn = QPushButton("退出")
        exit_btn.setFixedHeight(40)
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        exit_btn.clicked.connect(self.close)
        
        button_layout.addWidget(install_btn)
        button_layout.addStretch()
        button_layout.addWidget(exit_btn)
        
        main_layout.addWidget(button_widget)
        
        # 状态信息
        self.status_label = QLabel("就绪")
        self.status_label.setStyleSheet("""
            QLabel {
                padding: 10px;
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 4px;
                color: #6c757d;
            }
        """)
        main_layout.addWidget(self.status_label)
        
    def create_interface_card(self, interface):
        """创建界面选择卡片"""
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 2px solid {interface['color']}20;
                border-radius: 8px;
                padding: 15px;
            }}
            QFrame:hover {{
                border: 2px solid {interface['color']};
                background-color: {interface['color']}08;
            }}
        """)
        
        layout = QVBoxLayout(card)
        
        # 标题和运行按钮
        header_layout = QHBoxLayout()
        
        title_label = QLabel(interface["name"])
        title_label.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {interface['color']};")
        
        run_btn = QPushButton("运行")
        run_btn.setFixedWidth(80)
        run_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {interface['color']};
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {self.darken_color(interface['color'])};
            }}
        """)
        run_btn.clicked.connect(lambda checked, f=interface["file"]: self.run_interface(f))
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(run_btn)
        
        layout.addLayout(header_layout)
        
        # 文件信息
        file_label = QLabel(f"文件: {interface['file']}")
        file_label.setStyleSheet("color: #7f8c8d; font-size: 12px; margin-top: 5px;")
        layout.addWidget(file_label)
        
        # 描述
        desc_text = QLabel(interface["description"])
        desc_text.setWordWrap(True)
        desc_text.setStyleSheet("color: #495057; margin-top: 10px; line-height: 1.4;")
        layout.addWidget(desc_text)
        
        return card
    
    def darken_color(self, hex_color, amount=20):
        """加深颜色（简化实现）"""
        return hex_color
    
    def apply_styles(self):
        """应用样式"""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f8f9fa"))
        palette.setColor(QPalette.WindowText, QColor("#212529"))
        
        self.setPalette(palette)
        
    def run_interface(self, filename):
        """运行界面文件"""
        self.status_label.setText(f"正在启动 {filename}...")
        
        try:
            if os.path.exists(filename):
                # 在新进程中运行界面
                if sys.platform == "win32":
                    subprocess.Popen([sys.executable, filename], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    subprocess.Popen([sys.executable, filename])
                
                self.status_label.setText(f"已启动 {filename}")
                
                # 询问是否关闭启动器
                reply = QMessageBox.question(
                    self,
                    "启动成功",
                    f"{filename} 已启动。是否关闭启动器？",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                
                if reply == QMessageBox.Yes:
                    self.close()
            else:
                QMessageBox.warning(
                    self,
                    "文件不存在",
                    f"找不到文件: {filename}\n请确保文件在当前目录中。"
                )
                self.status_label.setText(f"文件不存在: {filename}")
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "启动失败",
                f"启动 {filename} 时出错:\n{str(e)}"
            )
            self.status_label.setText(f"启动失败: {filename}")
    
    def install_dependencies(self):
        """安装依赖"""
        self.status_label.setText("正在安装依赖...")
        
        try:
            if os.path.exists("requirements.txt"):
                # 安装依赖
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8'
                )
                
                if result.returncode == 0:
                    QMessageBox.information(
                        self,
                        "安装成功",
                        "依赖安装完成！"
                    )
                    self.status_label.setText("依赖安装完成")
                else:
                    QMessageBox.warning(
                        self,
                        "安装失败",
                        f"依赖安装失败:\n{result.stderr}"
                    )
                    self.status_label.setText("依赖安装失败")
            else:
                QMessageBox.warning(
                    self,
                    "文件不存在",
                    "找不到 requirements.txt 文件"
                )
                self.status_label.setText("找不到 requirements.txt")
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "安装出错",
                f"安装依赖时出错:\n{str(e)}"
            )
            self.status_label.setText("安装过程出错")


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle("Fusion")
    
    # 设置应用程序字体
    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)
    
    # 创建并显示启动器
    launcher = Launcher()
    launcher.show()
    
    # 运行应用程序
    sys.exit(app.exec())


if __name__ == "__main__":
    main()