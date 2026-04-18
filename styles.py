#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 样式定义
提供各种现代化的 UI 样式
"""

from PySide6.QtGui import QColor


class Styles:
    """样式类"""
    
    # 颜色定义
    COLORS = {
        # 主色调
        "primary": "#3498db",
        "primary_dark": "#2980b9",
        "primary_light": "#5dade2",
        
        # 辅助色
        "secondary": "#2ecc71",
        "secondary_dark": "#27ae60",
        "secondary_light": "#58d68d",
        
        # 警告色
        "warning": "#f39c12",
        "warning_dark": "#e67e22",
        "warning_light": "#f7dc6f",
        
        # 危险色
        "danger": "#e74c3c",
        "danger_dark": "#c0392b",
        "danger_light": "#f1948a",
        
        # 中性色
        "dark": "#2c3e50",
        "dark_dark": "#1c2833",
        "dark_light": "#566573",
        
        "gray": "#95a5a6",
        "gray_dark": "#7f8c8d",
        "gray_light": "#bdc3c7",
        
        "light": "#ecf0f1",
        "light_dark": "#d5dbdb",
        "light_light": "#f8f9fa",
        
        # 特殊色
        "purple": "#9b59b6",
        "purple_dark": "#8e44ad",
        "purple_light": "#bb8fce",
        
        "teal": "#1abc9c",
        "teal_dark": "#16a085",
        "teal_light": "#48c9b0",
        
        "orange": "#e67e22",
        "orange_dark": "#d35400",
        "orange_light": "#f5b041",
    }
    
    # 字体定义
    FONTS = {
        "title": "Segoe UI, Microsoft YaHei, sans-serif",
        "body": "Segoe UI, Microsoft YaHei, sans-serif",
        "mono": "Consolas, Monaco, monospace",
    }
    
    @classmethod
    def get_button_style(cls, color_name="primary", size="medium", variant="filled"):
        """获取按钮样式
        
        Args:
            color_name: 颜色名称，参考 COLORS
            size: 大小，可选 "small", "medium", "large"
            variant: 变体，可选 "filled", "outline", "text"
        """
        color = cls.COLORS.get(color_name, cls.COLORS["primary"])
        color_dark = cls.COLORS.get(f"{color_name}_dark", cls.COLORS["primary_dark"])
        
        # 大小定义
        sizes = {
            "small": {"padding": "4px 12px", "font_size": "12px"},
            "medium": {"padding": "8px 16px", "font_size": "14px"},
            "large": {"padding": "12px 24px", "font_size": "16px"},
        }
        
        size_style = sizes.get(size, sizes["medium"])
        
        # 变体定义
        if variant == "filled":
            base_style = f"""
                background-color: {color};
                color: white;
                border: none;
            """
        elif variant == "outline":
            base_style = f"""
                background-color: transparent;
                color: {color};
                border: 2px solid {color};
            """
        elif variant == "text":
            base_style = f"""
                background-color: transparent;
                color: {color};
                border: none;
            """
        else:
            base_style = f"""
                background-color: {color};
                color: white;
                border: none;
            """
        
        return f"""
            QPushButton {{
                {base_style}
                border-radius: 6px;
                padding: {size_style['padding']};
                font-size: {size_style['font_size']};
                font-weight: bold;
                font-family: {cls.FONTS['body']};
            }}
            QPushButton:hover {{
                background-color: {color_dark if variant == 'filled' else color}15;
            }}
            QPushButton:pressed {{
                background-color: {color_dark if variant == 'filled' else color}30;
            }}
            QPushButton:disabled {{
                background-color: {cls.COLORS['gray_light']};
                color: {cls.COLORS['gray']};
            }}
        """
    
    @classmethod
    def get_input_style(cls, color_name="primary", size="medium"):
        """获取输入框样式"""
        color = cls.COLORS.get(color_name, cls.COLORS["primary"])
        
        sizes = {
            "small": {"padding": "4px 8px", "font_size": "12px", "height": "28px"},
            "medium": {"padding": "6px 12px", "font_size": "14px", "height": "36px"},
            "large": {"padding": "8px 16px", "font_size": "16px", "height": "44px"},
        }
        
        size_style = sizes.get(size, sizes["medium"])
        
        return f"""
            QLineEdit, QTextEdit, QComboBox {{
                background-color: white;
                color: {cls.COLORS['dark']};
                border: 2px solid {cls.COLORS['gray_light']};
                border-radius: 4px;
                padding: {size_style['padding']};
                font-size: {size_style['font_size']};
                font-family: {cls.FONTS['body']};
                min-height: {size_style['height']};
            }}
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {{
                border: 2px solid {color};
                outline: none;
            }}
            QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled {{
                background-color: {cls.COLORS['light']};
                color: {cls.COLORS['gray']};
            }}
        """
    
    @classmethod
    def get_card_style(cls, elevation="medium", color_name="light"):
        """获取卡片样式
        
        Args:
            elevation: 阴影级别，可选 "none", "small", "medium", "large"
            color_name: 背景颜色名称
        """
        color = cls.COLORS.get(color_name, cls.COLORS["light"])
        
        shadows = {
            "none": "",
            "small": "box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);",
            "medium": "box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);",
            "large": "box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);",
        }
        
        shadow = shadows.get(elevation, shadows["medium"])
        
        return f"""
            QFrame {{
                background-color: {color};
                border-radius: 8px;
                border: 1px solid {cls.COLORS['light_dark']};
                {shadow}
            }}
        """
    
    @classmethod
    def get_table_style(cls, striped=True, hover=True):
        """获取表格样式"""
        striped_css = """
            QTableWidget {
                alternate-background-color: #f8f9fa;
            }
        """ if striped else ""
        
        hover_css = """
            QTableWidget::item:hover {
                background-color: #e3f2fd;
            }
        """ if hover else ""
        
        return f"""
            QTableWidget {{
                border: none;
                background-color: white;
                gridline-color: {cls.COLORS['light_dark']};
                font-family: {cls.FONTS['body']};
            }}
            QHeaderView::section {{
                background-color: {cls.COLORS['light']};
                padding: 12px 8px;
                border: none;
                border-bottom: 2px solid {cls.COLORS['gray_light']};
                font-weight: bold;
                color: {cls.COLORS['dark']};
            }}
            QTableWidget::item {{
                padding: 8px;
            }}
            {striped_css}
            {hover_css}
        """
    
    @classmethod
    def get_progress_bar_style(cls, color_name="primary"):
        """获取进度条样式"""
        color = cls.COLORS.get(color_name, cls.COLORS["primary"])
        
        return f"""
            QProgressBar {{
                border: 2px solid {cls.COLORS['gray_light']};
                border-radius: 4px;
                text-align: center;
                font-weight: bold;
                color: {cls.COLORS['dark']};
                background-color: white;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 2px;
            }}
        """
    
    @classmethod
    def get_label_style(cls, type="normal", color_name="dark"):
        """获取标签样式
        
        Args:
            type: 类型，可选 "normal", "title", "subtitle", "caption"
            color_name: 颜色名称
        """
        color = cls.COLORS.get(color_name, cls.COLORS["dark"])
        
        types = {
            "normal": {"font_size": "14px", "font_weight": "normal"},
            "title": {"font_size": "24px", "font_weight": "bold"},
            "subtitle": {"font_size": "18px", "font_weight": "bold"},
            "caption": {"font_size": "12px", "font_weight": "normal"},
        }
        
        type_style = types.get(type, types["normal"])
        
        return f"""
            QLabel {{
                color: {color};
                font-size: {type_style['font_size']};
                font-weight: {type_style['font_weight']};
                font-family: {cls.FONTS['body']};
            }}
        """
    
    @classmethod
    def get_application_style(cls, theme="light"):
        """获取应用程序整体样式
        
        Args:
            theme: 主题，可选 "light", "dark"
        """
        if theme == "dark":
            return cls._get_dark_theme()
        else:
            return cls._get_light_theme()
    
    @classmethod
    def _get_light_theme(cls):
        """获取浅色主题"""
        return f"""
            QMainWindow {{
                background-color: {cls.COLORS['light_light']};
            }}
            QWidget {{
                font-family: {cls.FONTS['body']};
                color: {cls.COLORS['dark']};
            }}
            QMenuBar {{
                background-color: white;
                border-bottom: 1px solid {cls.COLORS['light_dark']};
            }}
            QMenuBar::item {{
                padding: 8px 16px;
            }}
            QMenuBar::item:selected {{
                background-color: {cls.COLORS['primary']};
                color: white;
            }}
            QToolBar {{
                background-color: white;
                border: none;
                border-bottom: 1px solid {cls.COLORS['light_dark']};
                spacing: 5px;
            }}
            QStatusBar {{
                background-color: white;
                border-top: 1px solid {cls.COLORS['light_dark']};
                color: {cls.COLORS['gray_dark']};
            }}
            QGroupBox {{
                font-weight: bold;
                border: 2px solid {cls.COLORS['light_dark']};
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }}
        """
    
    @classmethod
    def _get_dark_theme(cls):
        """获取深色主题"""
        return f"""
            QMainWindow {{
                background-color: {cls.COLORS['dark_dark']};
            }}
            QWidget {{
                font-family: {cls.FONTS['body']};
                color: {cls.COLORS['light']};
                background-color: {cls.COLORS['dark']};
            }}
            QMenuBar {{
                background-color: {cls.COLORS['dark']};
                border-bottom: 1px solid {cls.COLORS['dark_light']};
            }}
            QMenuBar::item {{
                padding: 8px 16px;
                color: {cls.COLORS['light']};
            }}
            QMenuBar::item:selected {{
                background-color: {cls.COLORS['primary']};
                color: white;
            }}
            QToolBar {{
                background-color: {cls.COLORS['dark']};
                border: none;
                border-bottom: 1px solid {cls.COLORS['dark_light']};
                spacing: 5px;
            }}
            QStatusBar {{
                background-color: {cls.COLORS['dark']};
                border-top: 1px solid {cls.COLORS['dark_light']};
                color: {cls.COLORS['gray_light']};
            }}
            QGroupBox {{
                font-weight: bold;
                border: 2px solid {cls.COLORS['dark_light']};
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
                color: {cls.COLORS['light']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: {cls.COLORS['light']};
            }}
        """
    
    @classmethod
    def get_color(cls, color_name):
        """获取颜色对象"""
        hex_color = cls.COLORS.get(color_name, "#000000")
        return QColor(hex_color)


# 使用示例
if __name__ == "__main__":
    print("PySide6 样式定义")
    print("=" * 50)
    
    print("\n1. 按钮样式示例:")
    print(Styles.get_button_style("primary", "medium", "filled"))
    
    print("\n2. 输入框样式示例:")
    print(Styles.get_input_style("primary", "medium"))
    
    print("\n3. 卡片样式示例:")
    print(Styles.get_card_style("medium", "light"))
    
    print("\n4. 可用的颜色:")
    for name, color in Styles.COLORS.items():
        print(f"  {name:15} {color}")