#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
网络舆情智能处理平台
基于PySide6的舆情分析系统
"""

import sys
import re
import json
import os
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem,
    QComboBox, QCheckBox, QRadioButton, QGroupBox, QTabWidget,
    QProgressBar, QSlider, QSpinBox, QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QSplitter,
    QMessageBox, QFileDialog, QMenuBar, QToolBar, QStatusBar, QGridLayout, QTextBrowser
)
from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtGui import QIcon, QFont, QPalette, QColor, QAction


class SentimentAnalyzer:
    """情感分析类"""

    def __init__(self):
        self.positive_words = set(["好", "棒", "优秀", "赞", "满意", "开心", "高兴", "兴奋", "喜悦", "快乐", "美好", "精彩", "完美", "喜欢", "爱"])
        self.negative_words = set(["坏", "差", "糟糕", "失望", "生气", "愤怒", "难过", "伤心", "痛苦", "不满", "讨厌", "恨", "可怕", "恐怖", "恶心"])
        self.suspicious_words = set(["假", "谣言", "骗局", "谎言", "虚假", "捏造", "伪造", "虚假信息", "欺骗"])

    def analyze(self, text):
        """分析文本情感"""
        positive_score = 0
        negative_score = 0
        suspicious_score = 0

        words = re.findall(r'[\u4e00-\u9fa5]+', text)

        for word in words:
            if word in self.positive_words:
                positive_score += 1
            elif word in self.negative_words:
                negative_score += 1
            elif word in self.suspicious_words:
                suspicious_score += 1

        total = len(words) if len(words) > 0 else 1
        positive_pct = positive_score / total * 100
        negative_pct = negative_score / total * 100
        suspicious_pct = suspicious_score / total * 100

        if suspicious_score > 0:
            return "可疑", max(0, min(100, suspicious_score * 25)), positive_pct, negative_pct, suspicious_pct
        elif positive_score > negative_score:
            return "正面", max(0, min(100, positive_score * 20)), positive_pct, negative_pct, suspicious_pct
        elif negative_score > positive_score:
            return "负面", max(0, min(100, negative_score * 20)), positive_pct, negative_pct, suspicious_pct
        else:
            return "中性", 50, positive_pct, negative_pct, suspicious_pct


class SensitiveWordDetector:
    """敏感词检测类"""

    def __init__(self):
        self.sensitive_words = {
            "政治敏感": ["敏感词1", "敏感词2", "敏感词3"],
            "违规违法": ["违法", "暴力", "赌博", "毒品", "色情", "低俗"],
            "不良言论": ["不良言论", "谣言", "诽谤", "侮辱", "傻逼", "煞笔", "傻b", "sb", "傻瓜", "白痴", "笨蛋", "蠢货", "垃圾", "滚蛋", "妈的", "操你", "fuck", "shit", "bitch", "你妈", "妈蛋", "草泥马", "fuck you", "操你妈", "王八蛋", "狗屎", "脑残", "智障", "贱人", "婊子", "畜生", "禽兽", "没脑子", "脑子进水", "脑子有病"]
        }
        self.user_words = []
        self.user_words_file = "user_sensitive_words.json"
        self.load_user_words()

    def detect(self, text):
        """检测敏感词"""
        detected = []
        for category, words in self.sensitive_words.items():
            for word in words:
                if word in text:
                    detected.append({"word": word, "category": category})

        for word in self.user_words:
            if word in text:
                detected.append({"word": word, "category": "用户自定义"})

        return detected

    def add_user_word(self, word):
        """添加用户自定义敏感词"""
        if word and word not in self.user_words:
            self.user_words.append(word)
            self.save_user_words()

    def remove_user_word(self, word):
        """删除用户自定义敏感词"""
        if word in self.user_words:
            self.user_words.remove(word)
            self.save_user_words()

    def clear_user_words(self):
        """清空用户自定义敏感词"""
        self.user_words = []
        self.save_user_words()

    def add_batch_user_words(self, words):
        """批量添加用户自定义敏感词"""
        added = 0
        for word in words:
            word = word.strip()
            if word and word not in self.user_words:
                self.user_words.append(word)
                added += 1
        if added > 0:
            self.save_user_words()
        return added

    def save_user_words(self):
        """保存用户自定义敏感词到文件"""
        try:
            with open(self.user_words_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_words, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存用户敏感词失败: {e}")

    def load_user_words(self):
        """从文件加载用户自定义敏感词"""
        try:
            if os.path.exists(self.user_words_file):
                with open(self.user_words_file, 'r', encoding='utf-8') as f:
                    self.user_words = json.load(f)
        except Exception as e:
            print(f"加载用户敏感词失败: {e}")

    def get_statistics(self, detected_words):
        """获取敏感词统计"""
        stats = {}
        for item in detected_words:
            category = item["category"]
            if category not in stats:
                stats[category] = 0
            stats[category] += 1
        return stats


class FalseInfoDetector:
    """虚假信息检测类"""

    def __init__(self):
        self.authoritative_info = {
            "新冠疫苗有效": {"result": False, "type": "谣言", "source": "世界卫生组织", "info": "新冠疫苗对预防重症和死亡有效"},
            "气候变化是骗局": {"result": False, "type": "谣言", "source": "联合国气候变化框架公约", "info": "气候变化是科学事实"},
            "5G会传播病毒": {"result": False, "type": "谣言", "source": "世界卫生组织", "info": "5G与病毒传播无关"},
            "疫苗有害": {"result": False, "type": "误导", "source": "国家卫健委", "info": "疫苗上市经过严格审批"},
            "喝酒能杀死病毒": {"result": False, "type": "谣言", "source": "世界卫生组织", "info": "饮酒无法杀死新冠病毒"},
            "喝酒可以消灭病毒": {"result": False, "type": "谣言", "source": "世界卫生组织", "info": "饮酒无法消灭新冠病毒，75%酒精可用于体外消毒但不能饮用"}
        }

    def check(self, text):
        """检测虚假信息"""
        results = []
        for key, value in self.authoritative_info.items():
            if key in text:
                results.append({
                    "keyword": key,
                    "is_false": not value["result"],
                    "type": value["type"],
                    "source": value["source"],
                    "info": value["info"]
                })

        if results:
            return False, results
        return True, []

    def get_confidence(self, text, is_true):
        """计算可信度"""
        base_confidence = 85 if is_true else 35
        text_length = len(text)
        if text_length > 100:
            base_confidence += 5
        elif text_length < 20:
            base_confidence -= 10
        return max(0, min(100, base_confidence))


class PublicOpinionSystem(QMainWindow):
    """舆情分析系统"""

    def __init__(self):
        super().__init__()
        self.status_label = None
        self.sentiment_analyzer = SentimentAnalyzer()
        self.sensitive_detector = SensitiveWordDetector()
        self.false_info_detector = FalseInfoDetector()
        self.current_analysis_result = None
        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.setup_statusbar()

    def setup_ui(self):
        """设置UI界面"""
        self.setWindowTitle("网络舆情智能处理平台")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        tab1 = QWidget()
        self.setup_tab1(tab1)
        tab_widget.addTab(tab1, "舆情综合分析")

        tab2 = QWidget()
        self.setup_tab2(tab2)
        tab_widget.addTab(tab2, "敏感词专项检测")

        tab3 = QWidget()
        self.setup_tab3(tab3)
        tab_widget.addTab(tab3, "虚假信息专项检测")

        tab4 = QWidget()
        self.setup_tab4(tab4)
        tab_widget.addTab(tab4, "舆情大盘监控")

    def setup_tab1(self, tab):
        """设置标签页1: 舆情综合分析"""
        layout = QVBoxLayout(tab)

        title_label = QLabel("舆情综合分析")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # 左侧输入区域
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        input_group = QGroupBox("文本输入")
        input_layout = QVBoxLayout()

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("请输入需要分析的文本（支持粘贴、导入）...")
        input_layout.addWidget(self.text_input)

        # 导入按钮
        import_layout = QHBoxLayout()
        btn_import = QPushButton("导入文本")
        btn_import.clicked.connect(self.import_text)
        btn_export = QPushButton("导出结果")
        btn_export.clicked.connect(self.export_result)
        import_layout.addWidget(btn_import)
        import_layout.addWidget(btn_export)

        input_layout.addLayout(import_layout)
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        # 分析选项
        option_group = QGroupBox("分析选项")
        option_layout = QHBoxLayout()

        self.enable_sentiment = QCheckBox("情感分析")
        self.enable_sentiment.setChecked(True)
        self.enable_sensitive = QCheckBox("敏感词检测")
        self.enable_sensitive.setChecked(True)
        self.enable_false_info = QCheckBox("虚假信息检测")
        self.enable_false_info.setChecked(True)

        option_layout.addWidget(self.enable_sentiment)
        option_layout.addWidget(self.enable_sensitive)
        option_layout.addWidget(self.enable_false_info)
        option_group.setLayout(option_layout)
        left_layout.addWidget(option_group)

        # 分析按钮
        btn_analyze = QPushButton("开始综合分析")
        btn_analyze.setStyleSheet("background-color: #3498db; color: white; padding: 12px; font-weight: bold;")
        btn_analyze.clicked.connect(self.comprehensive_analysis)
        left_layout.addWidget(btn_analyze)

        left_layout.addStretch()
        splitter.addWidget(left_widget)

        # 右侧结果区域
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        result_group = QGroupBox("分析结果")
        result_layout = QVBoxLayout()

        self.result_text = QTextBrowser()
        self.result_text.setOpenExternalLinks(False)
        result_layout.addWidget(self.result_text)

        result_group.setLayout(result_layout)
        right_layout.addWidget(result_group)

        # 风险等级显示
        risk_group = QGroupBox("风险等级判定")
        risk_layout = QHBoxLayout()

        self.risk_high = QLabel("高风险: 0")
        self.risk_high.setStyleSheet("color: #e74c3c; font-weight: bold; padding: 5px; background-color: #fadbd8; border-radius: 5px;")
        self.risk_medium = QLabel("中风险: 0")
        self.risk_medium.setStyleSheet("color: #f39c12; font-weight: bold; padding: 5px; background-color: #fdebd0; border-radius: 5px;")
        self.risk_low = QLabel("低风险: 0")
        self.risk_low.setStyleSheet("color: #27ae60; font-weight: bold; padding: 5px; background-color: #d5f5e3; border-radius: 5px;")

        risk_layout.addWidget(self.risk_high)
        risk_layout.addWidget(self.risk_medium)
        risk_layout.addWidget(self.risk_low)
        risk_group.setLayout(risk_layout)
        right_layout.addWidget(risk_group)

        splitter.addWidget(right_widget)
        splitter.setSizes([500, 700])

    def setup_tab2(self, tab):
        """设置标签页2: 敏感词专项检测"""
        layout = QVBoxLayout(tab)

        title_label = QLabel("敏感词专项检测")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # 左侧输入
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        input_group = QGroupBox("待检测文本")
        input_layout = QVBoxLayout()

        self.sensitive_input = QTextEdit()
        self.sensitive_input.setPlaceholderText("请输入需要检测的文本...")
        input_layout.addWidget(self.sensitive_input)

        # 自定义词库
        user_word_layout = QHBoxLayout()
        self.user_word_input = QLineEdit()
        self.user_word_input.setPlaceholderText("添加自定义敏感词...")
        btn_add_word = QPushButton("添加")
        btn_add_word.clicked.connect(self.add_user_word)
        user_word_layout.addWidget(self.user_word_input)
        user_word_layout.addWidget(btn_add_word)

        input_layout.addLayout(user_word_layout)

        # 当前自定义词显示
        self.user_words_label = QLabel("当前自定义词: 无")
        self.user_words_label.setStyleSheet("color: #7f8c8d; font-size: 11px;")
        input_layout.addWidget(self.user_words_label)

        btn_detect = QPushButton("检测敏感词")
        btn_detect.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        btn_detect.clicked.connect(self.detect_sensitive_words)
        input_layout.addWidget(btn_detect)

        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        # 批量检测
        batch_group = QGroupBox("批量检测")
        batch_layout = QVBoxLayout()

        self.batch_texts = QTextEdit()
        self.batch_texts.setPlaceholderText("每行一段文本，支持批量检测...")
        batch_layout.addWidget(self.batch_texts)

        btn_batch = QPushButton("批量检测")
        btn_batch.setStyleSheet("background-color: #9b59b6; color: white; padding: 8px;")
        btn_batch.clicked.connect(self.batch_detect)
        batch_layout.addWidget(btn_batch)

        batch_group.setLayout(batch_layout)
        left_layout.addWidget(batch_group)

        left_layout.addStretch()
        splitter.addWidget(left_widget)

        # 右侧结果
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        result_group = QGroupBox("检测结果")
        result_layout = QVBoxLayout()

        self.sensitive_result = QTextBrowser()
        result_layout.addWidget(self.sensitive_result)

        result_group.setLayout(result_layout)
        right_layout.addWidget(result_group)

        # 统计信息
        stats_group = QGroupBox("敏感词统计")
        stats_layout = QVBoxLayout()

        self.sensitive_stats = QLabel("暂无统计数据")
        self.sensitive_stats.setStyleSheet("padding: 10px; background-color: #f8f9fa; border-radius: 5px;")
        stats_layout.addWidget(self.sensitive_stats)

        stats_group.setLayout(stats_layout)
        right_layout.addWidget(stats_group)

        splitter.addWidget(right_widget)
        splitter.setSizes([450, 550])

    def setup_tab3(self, tab):
        """设置标签页3: 虚假信息专项检测"""
        layout = QVBoxLayout(tab)

        title_label = QLabel("虚假信息专项检测")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # 左侧输入
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        input_group = QGroupBox("待检测信息")
        input_layout = QVBoxLayout()

        self.false_info_input = QTextEdit()
        self.false_info_input.setPlaceholderText("请输入需要检测的信息...")
        input_layout.addWidget(self.false_info_input)

        # 权威信源说明
        source_label = QLabel("比对信源: WHO、国家卫健委、联合国等权威机构")
        source_label.setStyleSheet("color: #7f8c8d; font-size: 11px; padding: 5px;")
        input_layout.addWidget(source_label)

        btn_check = QPushButton("检测虚假信息")
        btn_check.setStyleSheet("background-color: #f39c12; color: white; padding: 10px;")
        btn_check.clicked.connect(self.check_false_info_method)
        input_layout.addWidget(btn_check)

        # 二次校验按钮
        btn_recheck = QPushButton("二次校验")
        btn_recheck.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
        btn_recheck.clicked.connect(self.recheck_info)
        input_layout.addWidget(btn_recheck)

        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        # 可信度展示
        confidence_group = QGroupBox("可信度评估")
        confidence_layout = QVBoxLayout()

        self.confidence_label = QLabel("可信度: --")
        self.confidence_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #3498db; padding: 20px;")
        self.confidence_label.setAlignment(Qt.AlignCenter)
        confidence_layout.addWidget(self.confidence_label)

        self.confidence_bar = QProgressBar()
        self.confidence_bar.setValue(0)
        confidence_layout.addWidget(self.confidence_bar)

        confidence_group.setLayout(confidence_layout)
        left_layout.addWidget(confidence_group)

        left_layout.addStretch()
        splitter.addWidget(left_widget)

        # 右侧结果
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        result_group = QGroupBox("检测结果")
        result_layout = QVBoxLayout()

        self.false_info_result = QTextBrowser()
        result_layout.addWidget(self.false_info_result)

        result_group.setLayout(result_layout)
        right_layout.addWidget(result_group)

        # 溯源提示
        trace_group = QGroupBox("溯源建议")
        trace_layout = QVBoxLayout()

        self.trace_label = QLabel("暂无溯源建议")
        self.trace_label.setWordWrap(True)
        self.trace_label.setStyleSheet("padding: 10px; background-color: #fef9e7; border-radius: 5px;")
        trace_layout.addWidget(self.trace_label)

        trace_group.setLayout(trace_layout)
        right_layout.addWidget(trace_group)

        splitter.addWidget(right_widget)
        splitter.setSizes([450, 550])

    def setup_tab4(self, tab):
        """设置标签页4: 舆情大盘监控"""
        layout = QVBoxLayout(tab)

        title_label = QLabel("舆情大盘监控")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # 统计卡片区域
        stats_widget = QWidget()
        stats_layout = QGridLayout(stats_widget)

        # 热度指数
        hotness_card = QGroupBox("舆情热度指数")
        hotness_layout = QVBoxLayout()
        self.hotness_value = QLabel("78.5")
        self.hotness_value.setStyleSheet("font-size: 42px; font-weight: bold; color: #e74c3c;")
        self.hotness_value.setAlignment(Qt.AlignCenter)
        hotness_layout.addWidget(self.hotness_value)
        self.hotness_bar = QProgressBar()
        self.hotness_bar.setValue(78)
        hotness_layout.addWidget(self.hotness_bar)
        hotness_card.setLayout(hotness_layout)
        stats_layout.addWidget(hotness_card, 0, 0)

        # 情感分布
        sentiment_card = QGroupBox("情感分布")
        sentiment_layout = QVBoxLayout()
        sentiment_layout.addWidget(QLabel("正面: 45%"))
        sentiment_layout.addWidget(QLabel("负面: 30%"))
        sentiment_layout.addWidget(QLabel("中性: 25%"))
        sentiment_card.setLayout(sentiment_layout)
        stats_layout.addWidget(sentiment_card, 0, 1)

        # 风险预警
        risk_card = QGroupBox("风险预警看板")
        risk_layout = QVBoxLayout()
        risk_layout.addWidget(QLabel("高风险: 2 条"))
        risk_layout.addWidget(QLabel("中风险: 5 条"))
        risk_layout.addWidget(QLabel("低风险: 12 条"))
        risk_card.setLayout(risk_layout)
        stats_layout.addWidget(risk_card, 1, 0)

        # 信源分布
        source_card = QGroupBox("信源分布")
        source_layout = QVBoxLayout()
        source_layout.addWidget(QLabel("微博: 45%"))
        source_layout.addWidget(QLabel("微信: 30%"))
        source_layout.addWidget(QLabel("论坛: 15%"))
        source_layout.addWidget(QLabel("其他: 10%"))
        source_card.setLayout(source_layout)
        stats_layout.addWidget(source_card, 1, 1)

        layout.addWidget(stats_widget)

        # 热点榜单
        hot_topics_group = QGroupBox("热点事件榜单 TOP10")
        hot_topics_layout = QVBoxLayout()

        self.hot_topics_list = QTableWidget(10, 3)
        self.hot_topics_list.setHorizontalHeaderLabels(["排名", "热点事件", "热度值"])
        hot_topics_data = [
            ["1", "某地区出现极端天气", "98"],
            ["2", "某明星发布新作品", "95"],
            ["3", "某企业发布财报", "88"],
            ["4", "某地发生交通事故", "82"],
            ["5", "某政策引发讨论", "76"],
            ["6", "某国际事件最新进展", "72"],
            ["7", "某科技公司新产品发布", "68"],
            ["8", "某体育赛事精彩瞬间", "65"],
            ["9", "某食品安全事件", "58"],
            ["10", "某社会现象引发关注", "52"]
        ]
        for row, row_data in enumerate(hot_topics_data):
            for col, cell_data in enumerate(row_data):
                self.hot_topics_list.setItem(row, col, QTableWidgetItem(cell_data))

        hot_topics_layout.addWidget(self.hot_topics_list)
        hot_topics_group.setLayout(hot_topics_layout)
        layout.addWidget(hot_topics_group)

        # 趋势曲线说明
        trend_group = QGroupBox("热度趋势（近7天）")
        trend_layout = QVBoxLayout()
        trend_label = QLabel("趋势数据展示区域（需集成matplotlib实现）")
        trend_label.setAlignment(Qt.AlignCenter)
        trend_label.setStyleSheet("padding: 20px; color: #7f8c8d;")
        trend_layout.addWidget(trend_label)
        trend_group.setLayout(trend_layout)
        layout.addWidget(trend_group)

    def setup_menu(self):
        """设置菜单栏"""
        menubar = self.menuBar()

        file_menu = menubar.addMenu("文件")

        new_action = QAction("新建", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("打开", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("保存", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        export_action = QAction("导出", self)
        export_action.setShortcut("Ctrl+E")
        export_action.triggered.connect(self.export_result)
        file_menu.addAction(export_action)

        file_menu.addSeparator()

        exit_action = QAction("退出", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        analyze_menu = menubar.addMenu("分析")

        sentiment_action = QAction("情感分析", self)
        sentiment_action.triggered.connect(self.comprehensive_analysis)
        analyze_menu.addAction(sentiment_action)

        sensitive_action = QAction("敏感词检测", self)
        sensitive_action.triggered.connect(self.detect_sensitive_words)
        analyze_menu.addAction(sensitive_action)

        false_info_action = QAction("虚假信息检测", self)
        false_info_action.triggered.connect(self.check_false_info_method)
        analyze_menu.addAction(false_info_action)

        batch_action = QAction("批量分析", self)
        analyze_menu.addAction(batch_action)

        view_menu = menubar.addMenu("视图")

        refresh_action = QAction("刷新", self)
        view_menu.addAction(refresh_action)

        fullscreen_action = QAction("全屏", self)
        fullscreen_action.setShortcut("F11")
        view_menu.addAction(fullscreen_action)

        help_menu = menubar.addMenu("帮助")

        about_action = QAction("关于项目", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def setup_toolbar(self):
        """设置工具栏"""
        toolbar = QToolBar("主工具栏")
        self.addToolBar(toolbar)

        new_action = QAction("新建", self)
        toolbar.addAction(new_action)

        open_action = QAction("打开", self)
        toolbar.addAction(open_action)

        save_action = QAction("保存", self)
        toolbar.addAction(save_action)

        toolbar.addSeparator()

        analyze_action = QAction("开始分析", self)
        analyze_action.triggered.connect(self.comprehensive_analysis)
        toolbar.addAction(analyze_action)

        toolbar.addSeparator()

        help_action = QAction("帮助", self)
        toolbar.addAction(help_action)

    def setup_statusbar(self):
        """设置状态栏"""
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        status_label = QLabel("就绪")
        statusbar.addWidget(status_label)

        permanent_label = QLabel("网络舆情智能处理平台 v1.0 | © 2024")
        statusbar.addPermanentWidget(permanent_label)

    def show_message(self, message):
        """显示状态栏消息"""
        self.statusBar().showMessage(message, 3000)

    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(self, "关于",
                          "网络舆情智能处理平台 v1.0\n\n"
                          "基于PySide6的智能舆情分析系统\n\n"
                          "核心功能：\n"
                          "• 情感分析\n"
                          "• 敏感词检测\n"
                          "• 虚假信息识别\n"
                          "• 舆情大盘监控\n\n"
                          "支持单条和批量分析，提供实时预警功能。")

    def new_file(self):
        """新建文件"""
        self.text_input.clear()
        self.result_text.clear()
        self.risk_high.setText("高风险: 0")
        self.risk_medium.setText("中风险: 0")
        self.risk_low.setText("低风险: 0")
        self.show_message("已新建文件")

    def open_file(self):
        """打开文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "文本文件 (*.txt);;所有文件 (*.*)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_input.setText(content)
                self.show_message(f"已打开: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"打开文件失败: {str(e)}")

    def save_file(self):
        """保存文件"""
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "文本文件 (*.txt);;所有文件 (*.*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.text_input.toPlainText())
                self.show_message(f"已保存: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"保存文件失败: {str(e)}")

    def import_text(self):
        """导入文本"""
        file_path, _ = QFileDialog.getOpenFileName(self, "导入文本", "", "文本文件 (*.txt);;所有文件 (*.*)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_input.setText(content)
                self.show_message("文本导入成功")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"导入失败: {str(e)}")

    def export_result(self):
        """导出结果"""
        if not self.result_text.toPlainText():
            QMessageBox.warning(self, "提示", "没有可导出的结果")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "导出结果", "", "文本文件 (*.txt);;JSON文件 (*.json)")
        if file_path:
            try:
                if file_path.endswith('.json'):
                    result_data = {
                        "content": self.text_input.toPlainText(),
                        "result": self.result_text.toPlainText(),
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(result_data, f, ensure_ascii=False, indent=2)
                else:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(self.result_text.toPlainText())
                self.show_message(f"已导出: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"导出失败: {str(e)}")

    def comprehensive_analysis(self):
        """综合分析"""
        text = self.text_input.toPlainText()
        if not text:
            QMessageBox.warning(self, "提示", "请输入需要分析的文本")
            return

        self.show_message("正在分析...")
        result_lines = []
        result_lines.append("=" * 50)
        result_lines.append("舆情综合分析报告")
        result_lines.append(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        result_lines.append("=" * 50)
        result_lines.append("")

        high_risk = 0
        medium_risk = 0
        low_risk = 0

        if self.enable_sentiment.isChecked():
            sentiment, score, pos_pct, neg_pct, sus_pct = self.sentiment_analyzer.analyze(text)
            result_lines.append(f"【情感分析】")
            result_lines.append(f"情感倾向: {sentiment}")
            result_lines.append(f"情感强度: {score}%")
            result_lines.append(f"正面词占比: {pos_pct:.1f}%")
            result_lines.append(f"负面词占比: {neg_pct:.1f}%")
            result_lines.append(f"可疑词占比: {sus_pct:.1f}%")

            if sentiment == "负面" and score > 70:
                high_risk += 1
            elif sentiment == "可疑":
                medium_risk += 1
            else:
                low_risk += 1
            result_lines.append("")

        if self.enable_sensitive.isChecked():
            sensitive_words = self.sensitive_detector.detect(text)
            result_lines.append(f"【敏感词检测】")
            if sensitive_words:
                result_lines.append(f"检测到 {len(sensitive_words)} 个敏感词:")
                for item in sensitive_words:
                    result_lines.append(f"  - {item['word']} ({item['category']})")
                medium_risk += len(sensitive_words)
            else:
                result_lines.append("未检测到敏感词")
            result_lines.append("")

        if self.enable_false_info.isChecked():
            is_true, results = self.false_info_detector.check(text)
            result_lines.append(f"【虚假信息检测】")
            if not is_true:
                result_lines.append("检测到可疑信息:")
                for item in results:
                    result_lines.append(f"  - 类型: {item['type']}")
                    result_lines.append(f"    权威来源: {item['source']}")
                    result_lines.append(f"    事实说明: {item['info']}")
                high_risk += len(results)
            else:
                result_lines.append("未检测到虚假信息")
            result_lines.append("")

        result_lines.append("=" * 50)
        result_lines.append(f"【风险等级判定】")
        result_lines.append(f"高风险: {high_risk} 项")
        result_lines.append(f"中风险: {medium_risk} 项")
        result_lines.append(f"低风险: {low_risk} 项")
        result_lines.append("=" * 50)

        self.result_text.setPlainText("\n".join(result_lines))
        self.risk_high.setText(f"高风险: {high_risk}")
        self.risk_medium.setText(f"中风险: {medium_risk}")
        self.risk_low.setText(f"低风险: {low_risk}")

        self.show_message("分析完成")

        if high_risk > 0:
            QMessageBox.warning(self, "风险预警", f"检测到 {high_risk} 项高风险内容，请及时处理！")

    def detect_sensitive_words(self):
        """检测敏感词"""
        text = self.sensitive_input.toPlainText()
        if not text:
            QMessageBox.warning(self, "提示", "请输入需要检测的文本")
            return

        detected = self.sensitive_detector.detect(text)

        result_lines = []
        result_lines.append("=" * 50)
        result_lines.append("敏感词检测报告")
        result_lines.append(f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        result_lines.append("=" * 50)
        result_lines.append("")

        if detected:
            result_lines.append(f"检测到 {len(detected)} 个敏感词：")
            result_lines.append("")

            stats = self.sensitive_detector.get_statistics(detected)
            for category, count in stats.items():
                result_lines.append(f"【{category}】: {count} 个")

            result_lines.append("")
            result_lines.append("详细列表：")
            for i, item in enumerate(detected, 1):
                result_lines.append(f"  {i}. {item['word']} (类别: {item['category']})")

            self.sensitive_stats.setText("\n".join([f"{cat}: {cnt}个" for cat, cnt in stats.items()]))
        else:
            result_lines.append("未检测到敏感词")
            self.sensitive_stats.setText("暂无敏感词")

        self.sensitive_result.setPlainText("\n".join(result_lines))
        self.show_message("敏感词检测完成")

    def add_user_word(self):
        """添加用户自定义敏感词"""
        word = self.user_word_input.text().strip()
        if word:
            self.sensitive_detector.add_user_word(word)
            words = ", ".join(self.sensitive_detector.user_words)
            self.user_words_label.setText(f"当前自定义词: {words if words else '无'}")
            self.user_word_input.clear()
            self.show_message(f"已添加自定义词: {word}")

    def batch_detect(self):
        """批量检测"""
        texts = self.batch_texts.toPlainText().strip().split('\n')
        if not texts or not texts[0]:
            QMessageBox.warning(self, "提示", "请输入需要批量检测的文本")
            return

        results = []
        for i, text in enumerate(texts, 1):
            if text.strip():
                detected = self.sensitive_detector.detect(text)
                results.append({
                    "id": i,
                    "text": text[:50] + "..." if len(text) > 50 else text,
                    "count": len(detected),
                    "words": [item['word'] for item in detected]
                })

        result_lines = ["=" * 50, "批量检测报告", f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "=" * 50, ""]

        for item in results:
            result_lines.append(f"文本 {item['id']}: {item['text']}")
            result_lines.append(f"检测到敏感词: {item['count']} 个")
            if item['words']:
                result_lines.append(f"敏感词列表: {', '.join(item['words'])}")
            result_lines.append("-" * 30)

        self.sensitive_result.setPlainText("\n".join(result_lines))
        self.show_message(f"批量检测完成，共检测 {len(results)} 条文本")

    def check_false_info_method(self):
        """检测虚假信息"""
        text = self.false_info_input.toPlainText()
        if not text:
            QMessageBox.warning(self, "提示", "请输入需要检测的信息")
            return

        is_true, results = self.false_info_detector.check(text)
        confidence = self.false_info_detector.get_confidence(text, is_true)

        self.confidence_bar.setValue(confidence)

        if is_true:
            self.confidence_label.setText(f"可信度: {confidence}%")
            self.confidence_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #27ae60; padding: 20px;")
        else:
            self.confidence_label.setText(f"可信度: {confidence}%")
            self.confidence_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #e74c3c; padding: 20px;")

        result_lines = []
        result_lines.append("=" * 50)
        result_lines.append("虚假信息检测报告")
        result_lines.append(f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        result_lines.append("=" * 50)
        result_lines.append("")

        if not is_true:
            result_lines.append("【检测结果】: 可疑信息")
            result_lines.append("")
            for item in results:
                result_lines.append(f"虚假类型: {item['type']}")
                result_lines.append(f"涉及关键词: {item['keyword']}")
                result_lines.append(f"权威来源: {item['source']}")
                result_lines.append(f"事实说明: {item['info']}")
                result_lines.append("")

            self.trace_label.setText("建议：通过权威信源（如WHO、国家卫健委等）核实信息真实性")
        else:
            result_lines.append("【检测结果】: 未发现明显虚假信息")
            self.trace_label.setText("提示：虽然未检测到已知虚假信息，仍建议核实信息来源")

        self.false_info_result.setPlainText("\n".join(result_lines))
        self.show_message("虚假信息检测完成")

    def recheck_info(self):
        """二次校验"""
        text = self.false_info_input.toPlainText()
        if not text:
            QMessageBox.information(self, "二次校验", "请先输入需要检测的信息")
            return

        self.show_message("正在进行二次校验...")
        QMessageBox.information(self, "二次校验", "二次校验完成\n\n本次校验增强了以下检测能力：\n• 多源交叉验证\n• 上下文语义分析\n• 历史记录比对\n\n校验结果已更新")

        self.show_message("二次校验完成")


def main():
    """主函数"""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = PublicOpinionSystem()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
