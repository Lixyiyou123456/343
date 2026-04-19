#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
网络舆情智能处理平台
简洁版界面 - 轻量化快速使用
"""

import sys
import json
import os
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget,
    QComboBox, QCheckBox, QRadioButton, QGroupBox, QTabWidget,
    QProgressBar, QSlider, QSpinBox, QTableWidget, QTableWidgetItem, QSplitter,
    QMessageBox, QMenuBar, QToolBar, QStatusBar, QFrame, QTextBrowser
)
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QFont, QPalette, QColor, QAction


class SimplePublicOpinionUI(QMainWindow):
    """简洁版舆情分析界面"""

    def __init__(self):
        super().__init__()
        self.analysis_count = 0
        self.risk_count = 0
        self.sensitive_count = 0
        self.total_time = 0.0
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()

    def setup_ui(self):
        """设置UI界面"""
        self.setWindowTitle("网络舆情智能处理平台 - 简洁版")
        self.setGeometry(100, 100, 1000, 700)

        self.apply_styles()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)

        # 标题区域
        title_frame = QFrame()
        title_frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        title_layout = QVBoxLayout(title_frame)

        title_label = QLabel("网络舆情智能处理平台")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50; padding: 10px;")
        title_layout.addWidget(title_label)

        subtitle_label = QLabel("轻量化 · 快速分析 · 实时预警")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #7f8c8d; padding: 5px;")
        title_layout.addWidget(subtitle_label)

        main_layout.addWidget(title_frame)

        # 内容区域
        content_splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(content_splitter, 1)

        # 左侧面板
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # 快速分析组
        analysis_group = QGroupBox("快速分析")
        analysis_group.setFont(QFont("Arial", 10, QFont.Bold))
        analysis_layout = QVBoxLayout()

        # 分析模式选择
        analysis_layout.addWidget(QLabel("选择分析模式:"))
        self.analysis_mode = QComboBox()
        self.analysis_mode.addItems(["情感分析", "敏感词检测", "虚假信息检测"])
        analysis_layout.addWidget(self.analysis_mode)

        # 文本输入
        analysis_layout.addWidget(QLabel("输入文本:"))
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("请输入需要分析的文本...")
        analysis_layout.addWidget(self.text_input)

        # 一键分析按钮
        btn_analyze = QPushButton("开始分析")
        btn_analyze.setStyleSheet(self.get_button_style("#27ae60"))
        btn_analyze.clicked.connect(self.start_analysis)
        analysis_layout.addWidget(btn_analyze)

        analysis_group.setLayout(analysis_layout)
        left_layout.addWidget(analysis_group)

        # 高级设置组
        settings_group = QGroupBox("高级设置")
        settings_layout = QVBoxLayout()

        self.enable_warning = QCheckBox("实时风险预警")
        self.enable_warning.setChecked(True)

        self.enable_auto_save = QCheckBox("结果自动保存")

        self.enable_detail = QCheckBox("详细分析模式")
        self.enable_detail.setChecked(True)

        self.enable_dark = QCheckBox("深色模式")
        self.enable_dark.setChecked(True)

        settings_layout.addWidget(self.enable_warning)
        settings_layout.addWidget(self.enable_auto_save)
        settings_layout.addWidget(self.enable_detail)
        settings_layout.addWidget(self.enable_dark)

        # 连接信号
        self.enable_warning.stateChanged.connect(lambda: print("实时风险预警:", self.enable_warning.isChecked()))
        self.enable_auto_save.stateChanged.connect(lambda: print("结果自动保存:", self.enable_auto_save.isChecked()))
        self.enable_detail.stateChanged.connect(lambda: print("详细分析模式:", self.enable_detail.isChecked()))
        self.enable_dark.stateChanged.connect(self.toggle_dark_mode)

        settings_group.setLayout(settings_layout)
        left_layout.addWidget(settings_group)

        # 操作按钮
        button_layout = QHBoxLayout()

        btn_save = QPushButton("保存结果")
        btn_save.setStyleSheet(self.get_button_style("#3498db"))
        btn_save.clicked.connect(self.save_result)

        btn_clear = QPushButton("清空")
        btn_clear.setStyleSheet(self.get_button_style("#e74c3c"))
        btn_clear.clicked.connect(self.clear_all)

        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_clear)

        left_layout.addLayout(button_layout)
        left_layout.addStretch()

        content_splitter.addWidget(left_panel)

        # 右侧面板
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # 结果显示组
        result_group = QGroupBox("分析结果")
        result_layout = QVBoxLayout()

        self.result_text = QTextBrowser()
        self.result_text.setOpenExternalLinks(False)
        result_layout.addWidget(self.result_text)

        result_group.setLayout(result_layout)
        right_layout.addWidget(result_group)

        # 数据统计面板
        stats_group = QGroupBox("数据统计")
        stats_layout = QVBoxLayout()

        self.analysis_count_label = QLabel("总分析次数: 0")
        self.risk_count_label = QLabel("风险信息条数: 0")
        self.sensitive_count_label = QLabel("敏感词总数: 0")
        self.avg_time_label = QLabel("平均分析耗时: 0.0s")

        stats_layout.addWidget(self.analysis_count_label)
        stats_layout.addWidget(self.risk_count_label)
        stats_layout.addWidget(self.sensitive_count_label)
        stats_layout.addWidget(self.avg_time_label)

        stats_group.setLayout(stats_layout)
        right_layout.addWidget(stats_group)

        # 快捷操作
        action_layout = QHBoxLayout()

        btn_refresh = QPushButton("刷新统计")
        btn_refresh.setStyleSheet(self.get_button_style("#3498db"))
        btn_refresh.clicked.connect(self.refresh_stats)

        btn_export = QPushButton("导出JSON")
        btn_export.setStyleSheet(self.get_button_style("#9b59b6"))
        btn_export.clicked.connect(self.export_json)

        btn_help = QPushButton("帮助")
        btn_help.setStyleSheet(self.get_button_style("#95a5a6"))
        btn_help.clicked.connect(self.show_help)

        action_layout.addWidget(btn_refresh)
        action_layout.addWidget(btn_export)
        action_layout.addWidget(btn_help)

        right_layout.addLayout(action_layout)
        right_layout.addStretch()

        content_splitter.addWidget(right_panel)
        content_splitter.setSizes([400, 600])

    def apply_styles(self):
        """应用全局样式"""
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
        return hex_color

    def toggle_dark_mode(self):
        """切换深色模式"""
        if self.enable_dark.isChecked():
            # 应用深色模式
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
            palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
            self.setPalette(palette)
        else:
            # 应用浅色模式
            self.apply_styles()

    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()

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
            elif text == "保存":
                action.triggered.connect(self.save_result)
            elif text == "导出":
                action.triggered.connect(self.export_json)
            file_menu.addAction(action)

        analyze_menu = menubar.addMenu("分析")

        analyze_actions = ["情感分析", "敏感词检测", "虚假信息检测", "批量分析"]

        for text in analyze_actions:
            action = QAction(text, self)
            analyze_menu.addAction(action)

        view_menu = menubar.addMenu("视图")

        view_actions = ["刷新", "重置视图", "全屏"]

        for text in view_actions:
            action = QAction(text, self)
            view_menu.addAction(action)

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
            if text == "分析":
                action.triggered.connect(self.start_analysis)
            toolbar.addAction(action)

    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        self.status_message = QLabel("就绪")
        statusbar.addWidget(self.status_message)

        system_info = QLabel("© 2024 网络舆情智能处理平台 v1.0")
        statusbar.addPermanentWidget(system_info)

    def show_status(self, message):
        """显示状态消息"""
        self.status_message.setText(message)

    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self,
            "关于 网络舆情智能处理平台",
            "网络舆情智能处理平台 v1.0\n\n"
            "轻量化舆情分析系统\n\n"
            "核心功能：\n"
            "• 情感分析\n"
            "• 敏感词检测\n"
            "• 虚假信息识别\n"
            "• 实时预警\n\n"
            "轻量化设计，快速易用。"
        )

    def start_analysis(self):
        """开始分析"""
        import time
        start_time = time.time()

        text = self.text_input.toPlainText()
        if not text:
            QMessageBox.warning(self, "提示", "请输入需要分析的文本")
            return

        analysis_mode = self.analysis_mode.currentText()
        self.show_status(f"正在进行{analysis_mode}...")

        time.sleep(0.5)

        if analysis_mode == "情感分析":
            result = self.analyze_sentiment(text)
        elif analysis_mode == "敏感词检测":
            result = self.detect_sensitive(text)
        else:
            result = self.detect_false_info(text)

        self.result_text.setText(result)

        elapsed_time = time.time() - start_time
        self.total_time += elapsed_time
        self.analysis_count += 1

        self.update_stats()

        self.show_status(f"{analysis_mode}完成，耗时{elapsed_time:.2f}秒")

        if self.enable_warning.isChecked():
            if "敏感词" in result or "虚假" in result or "风险" in result or "可疑" in result:
                QMessageBox.warning(self, "风险预警", "检测到潜在风险信息，请及时处理！")
                self.risk_count += 1

        if self.enable_auto_save.isChecked():
            self.auto_save_result(result)

    def analyze_sentiment(self, text):
        """情感分析"""
        positive_words = ["好", "棒", "优秀", "赞", "满意", "开心", "高兴", "美好", "精彩", "完美", "喜欢", "爱"]
        negative_words = ["坏", "差", "糟糕", "失望", "生气", "愤怒", "难过", "伤心", "痛苦", "不满", "讨厌", "恨", "可怕", "恐怖", "恶心"]
        suspicious_words = ["假", "谣言", "骗局", "谎言", "虚假", "捏造", "欺骗"]

        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)
        suspicious_count = sum(1 for word in suspicious_words if word in text)

        if suspicious_count > 0:
            sentiment = "可疑"
            confidence = min(100, suspicious_count * 25)
        elif positive_count > negative_count:
            sentiment = "正面"
            confidence = min(100, positive_count * 20)
        elif negative_count > positive_count:
            sentiment = "负面"
            confidence = min(100, negative_count * 20)
        else:
            sentiment = "中性"
            confidence = 50

        result = f"{'='*50}\n"
        result += "情感分析报告\n"
        result += f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        result += f"{'='*50}\n\n"
        result += f"情感倾向: {sentiment}\n"
        result += f"置信度: {confidence}%\n"
        result += f"正面词数: {positive_count}\n"
        result += f"负面词数: {negative_count}\n"
        result += f"可疑词数: {suspicious_count}\n\n"

        if self.enable_detail.isChecked():
            result += f"详细分析:\n"
            if positive_count > 0:
                result += f"  检测到正面情感表达\n"
            if negative_count > 0:
                result += f"  检测到负面情感表达\n"
            if suspicious_count > 0:
                result += f"  警告：检测到可疑表达\n"

        return result

    def detect_sensitive(self, text):
        """敏感词检测"""
        sensitive_words = {
            "政治敏感": ["敏感词"],
            "违规违法": ["违法", "暴力", "赌博", "毒品", "色情", "低俗"],
            "不良言论": ["谣言", "诽谤", "侮辱", "傻逼", "煞笔", "傻b", "sb", "傻瓜", "白痴", "笨蛋", "蠢货", "垃圾", "滚蛋", "妈的", "操你", "fuck", "shit", "bitch", "你妈", "妈蛋", "草泥马", "fuck you", "操你妈", "王八蛋", "狗屎", "脑残", "智障", "贱人", "婊子", "畜生", "禽兽", "没脑子", "脑子进水", "脑子有病"]
        }

        detected = []
        for category, words in sensitive_words.items():
            for word in words:
                if word in text:
                    detected.append({"word": word, "category": category})
                    self.sensitive_count += 1

        result = f"{'='*50}\n"
        result += "敏感词检测报告\n"
        result += f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        result += f"{'='*50}\n\n"

        if detected:
            result += f"检测到 {len(detected)} 个敏感词:\n\n"
            stats = {}
            for item in detected:
                cat = item["category"]
                stats[cat] = stats.get(cat, 0) + 1

            for cat, cnt in stats.items():
                result += f"【{cat}】: {cnt} 个\n"

            result += "\n详细列表:\n"
            for i, item in enumerate(detected, 1):
                result += f"  {i}. {item['word']}\n"
        else:
            result += "未检测到敏感词\n"

        return result

    def detect_false_info(self, text):
        """虚假信息检测"""
        false_patterns = {
            "新冠疫苗有效": {"type": "谣言", "source": "世界卫生组织", "info": "疫苗对预防重症有效"},
            "气候变化是骗局": {"type": "谣言", "source": "联合国气候变化框架公约", "info": "气候变化是科学事实"},
            "5G会传播病毒": {"type": "谣言", "source": "世界卫生组织", "info": "5G与病毒无关"},
            "疫苗有害": {"type": "误导", "source": "国家卫健委", "info": "疫苗经过严格审批"},
            "喝酒能杀死病毒": {"type": "谣言", "source": "世界卫生组织", "info": "饮酒无法杀死病毒"}
        }

        detected = []
        for pattern, info in false_patterns.items():
            if pattern in text:
                detected.append({"keyword": pattern, **info})

        result = f"{'='*50}\n"
        result += "虚假信息检测报告\n"
        result += f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        result += f"{'='*50}\n\n"

        if detected:
            result += "检测到可疑信息:\n\n"
            for item in detected:
                result += f"关键词: {item['keyword']}\n"
                result += f"类型: {item['type']}\n"
                result += f"权威来源: {item['source']}\n"
                result += f"事实说明: {item['info']}\n\n"
                self.risk_count += 1
        else:
            result += "未检测到虚假信息\n"
            result += "可信度评估: 高\n\n"

        result += "溯源建议:\n"
        if detected:
            result += "建议通过权威信源（WHO、国家卫健委等）核实信息真实性\n"
        else:
            result += "信息暂时可信，但建议持续关注\n"

        return result

    def update_stats(self):
        """更新统计信息"""
        self.analysis_count_label.setText(f"总分析次数: {self.analysis_count}")
        self.risk_count_label.setText(f"风险信息条数: {self.risk_count}")
        self.sensitive_count_label.setText(f"敏感词总数: {self.sensitive_count}")

        if self.analysis_count > 0:
            avg_time = self.total_time / self.analysis_count
            self.avg_time_label.setText(f"平均分析耗时: {avg_time:.2f}s")

    def save_result(self):
        """保存结果"""
        result = self.result_text.toPlainText()
        if not result:
            QMessageBox.warning(self, "提示", "没有可保存的结果")
            return

        save_path = os.path.join(os.path.expanduser("~"), f"analysis_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(result)
            QMessageBox.information(self, "保存成功", f"结果已保存到:\n{save_path}")
            self.show_status("结果已保存")
        except Exception as e:
            QMessageBox.error(self, "保存失败", f"保存失败:\n{str(e)}")

    def auto_save_result(self, result):
        """自动保存结果"""
        try:
            save_path = os.path.join(os.path.expanduser("~"), f"auto_save_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(result)
            self.show_status("结果已自动保存")
        except:
            pass

    def clear_all(self):
        """清空所有内容"""
        self.text_input.clear()
        self.result_text.clear()
        self.show_status("已清空")

    def refresh_stats(self):
        """刷新统计信息"""
        self.show_status("统计信息已刷新")

    def export_json(self):
        """导出JSON"""
        if not self.result_text.toPlainText():
            QMessageBox.warning(self, "提示", "没有可导出的结果")
            return

        export_data = {
            "analysis_mode": self.analysis_mode.currentText(),
            "input_text": self.text_input.toPlainText(),
            "result": self.result_text.toPlainText(),
            "statistics": {
                "analysis_count": self.analysis_count,
                "risk_count": self.risk_count,
                "sensitive_count": self.sensitive_count,
                "avg_time": self.total_time / self.analysis_count if self.analysis_count > 0 else 0
            },
            "timestamp": datetime.now().isoformat()
        }

        export_path = os.path.join(os.path.expanduser("~"), f"export_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        try:
            with open(export_path, "w", encoding="utf-8") as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "导出成功", f"数据已导出到:\n{export_path}")
            self.show_status("数据已导出为JSON")
        except Exception as e:
            QMessageBox.error(self, "导出失败", f"导出失败:\n{str(e)}")

    def show_help(self):
        """显示帮助"""
        QMessageBox.information(
            self,
            "使用帮助",
            "网络舆情智能处理平台 - 简洁版\n\n"
            "【快速开始】\n"
            "1. 选择分析模式（情感分析/敏感词检测/虚假信息检测）\n"
            "2. 输入或粘贴需要分析的文本\n"
            "3. 点击「开始分析」获取结果\n\n"
            "【高级设置】\n"
            "• 实时风险预警：检测到风险时自动弹窗提醒\n"
            "• 结果自动保存：分析完成后自动保存结果\n"
            "• 详细分析模式：显示更详细的分析内容\n"
            "• 深色模式：切换界面颜色主题\n\n"
            "【快捷操作】\n"
            "• 保存结果：保存为TXT文件\n"
            "• 清空：清空输入和结果\n"
            "• 刷新统计：更新统计数据\n"
            "• 导出JSON：导出完整数据为JSON格式"
        )
        self.show_status("显示帮助信息")


def main():
    """主函数"""
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    font = QFont("Microsoft YaHei", 9)
    app.setFont(font)

    window = SimplePublicOpinionUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
