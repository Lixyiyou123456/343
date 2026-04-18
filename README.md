# PySide6 UI 界面示例

本项目包含三个不同风格的 PySide6 界面示例，展示了如何使用 PySide6 创建现代化的桌面应用程序界面。

## 文件说明

### 1. `main.py` - 完整功能界面
- 包含 PySide6 所有主要控件的完整示例
- 4个标签页：基本控件、输入控件、表格和列表、高级控件
- 完整的菜单栏、工具栏、状态栏
- 适合学习和参考各种控件的使用方法

### 2. `simple_ui.py` - 简洁界面
- 专注于界面设计和布局的简洁示例
- 现代化的配色方案
- 清晰的布局结构
- 适合作为实际项目的基础模板

### 3. `dashboard.py` - 现代化仪表板
- 数据可视化和管理界面
- 卡片式布局设计
- 实时数据更新
- 适合数据分析和管理类应用

## 运行要求

### 系统要求
- Python 3.8 或更高版本
- Windows/Linux/macOS

### 安装依赖
```bash
pip install -r requirements.txt
```

## 运行方法

### 运行完整功能界面
```bash
python main.py
```

### 运行简洁界面
```bash
python simple_ui.py
```

### 运行仪表板界面
```bash
python dashboard.py
```

## 界面特点

### 共同特点
- 使用 PySide6 构建
- 现代化的 UI 设计
- 响应式布局
- 完整的菜单和工具栏
- 状态栏显示系统信息

### 各界面独特特点

#### `main.py`
- 展示所有 PySide6 控件
- 包含完整的交互功能
- 适合学习 PySide6 控件使用

#### `simple_ui.py`
- 简洁美观的设计
- 合理的布局结构
- 适合作为项目起点

#### `dashboard.py`
- 数据卡片展示
- 实时数据更新
- 表格数据管理
- 适合数据分析应用

## 项目结构
```
.
├── main.py              # 完整功能界面
├── simple_ui.py         # 简洁界面
├── dashboard.py         # 仪表板界面
├── requirements.txt     # 依赖文件
└── README.md           # 说明文档
```

## 学习要点

### 1. 基本窗口创建
```python
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.show()
sys.exit(app.exec())
```

### 2. 布局管理
- QVBoxLayout: 垂直布局
- QHBoxLayout: 水平布局
- QGridLayout: 网格布局
- QSplitter: 分割器布局

### 3. 常用控件
- QLabel: 标签
- QPushButton: 按钮
- QLineEdit: 单行输入框
- QTextEdit: 多行文本框
- QComboBox: 下拉框
- QCheckBox: 复选框
- QRadioButton: 单选框
- QTableWidget: 表格
- QListWidget: 列表

### 4. 样式设计
- 使用样式表 (CSS-like)
- 设置字体和颜色
- 自定义控件外观

## 扩展建议

### 1. 添加数据库支持
- 使用 SQLite 存储数据
- 添加数据库操作功能

### 2. 添加图表功能
- 集成 matplotlib 或 pyqtgraph
- 实现数据可视化

### 3. 添加网络功能
- 实现 API 调用
- 添加网络数据获取

### 4. 添加多语言支持
- 使用 Qt 的翻译系统
- 支持中英文切换

## 注意事项

1. 确保已安装 PySide6
2. 界面代码仅供参考，实际项目需要根据需求调整
3. 建议在虚拟环境中运行
4. 大型项目建议使用 MVC 或 MVVM 架构

## 许可证

本项目代码仅供学习和参考使用，可根据需要自由修改和使用。

## 联系

如有问题或建议，欢迎交流讨论。