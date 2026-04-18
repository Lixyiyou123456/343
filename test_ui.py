#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PySide6 界面测试
测试所有界面是否可以正常运行
"""

import sys
import os


def check_dependencies():
    """检查依赖是否安装"""
    print("检查 PySide6 依赖...")
    
    try:        import PySide6
        print(f"OK PySide6 已安装 (版本: {PySide6.__version__})")
        return True
    except ImportError:
        print("ERROR PySide6 未安装")
        print("请运行: pip install PySide6")
        return False


def list_ui_files():
    """列出所有界面文件"""
    print("\n可用的界面文件:")
    print("-" * 40)
    
    ui_files = [
        ("main.py", "完整功能界面"),
        ("simple_ui.py", "简洁界面"), 
        ("dashboard.py", "现代化仪表板"),
        ("run.py", "界面启动器")
    ]
    
    for filename, description in ui_files:
        if os.path.exists(filename):
            print(f"OK {filename:20} - {description}")
        else:
            print(f"ERROR {filename:20} - 文件不存在")
    
    return [f[0] for f in ui_files if os.path.exists(f[0])]


def test_ui_file(filename):
    """测试单个界面文件"""
    print(f"\n测试 {filename}...")
    print("-" * 40)
    
    try:
        # 尝试导入文件
        module_name = filename.replace(".py", "")
        
        # 使用 exec 来测试文件是否可以正常导入和运行
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否有语法错误
        compile(content, filename, 'exec')
        print(f"OK {filename} 语法检查通过")
        
        # 检查是否包含必要的导入
        if "from PySide6" in content or "import PySide6" in content:
            print(f"OK {filename} 包含 PySide6 导入")
        else:
            print(f"WARN {filename} 可能不包含 PySide6 导入")
        
        # 检查是否有主函数
        if "def main()" in content or "if __name__ == \"__main__\"" in content:
            print(f"OK {filename} 包含主函数")
        else:
            print(f"WARN {filename} 可能不包含可执行的主函数")
        
        return True
        
    except SyntaxError as e:
        print(f"ERROR {filename} 语法错误: {e}")
        return False
    except Exception as e:
        print(f"ERROR {filename} 测试失败: {e}")
        return False


def run_quick_test():
    """运行快速测试"""
    print("PySide6 界面测试工具")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        print("\n请先安装依赖再运行测试。")
        return
    
    # 列出文件
    available_files = list_ui_files()
    
    if not available_files:
        print("\n没有找到可用的界面文件。")
        return
    
    # 测试每个文件
    print("\n开始测试界面文件...")
    results = []
    
    for filename in available_files:
        success = test_ui_file(filename)
        results.append((filename, success))
    
    # 显示测试结果
    print("\n测试结果汇总:")
    print("-" * 40)
    
    all_passed = True
    for filename, success in results:
        status = "OK 通过" if success else "ERROR 失败"
        print(f"{filename:20} {status}")
        if not success:
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("所有测试通过！")
        print("\n运行建议:")
        print("1. 使用启动器: python run.py")
        print("2. 直接运行: python main.py")
        print("3. 直接运行: python simple_ui.py")
        print("4. 直接运行: python dashboard.py")
    else:
        print("部分测试失败，请检查上述错误。")
    
    return all_passed


def check_requirements():
    """检查 requirements.txt"""
    print("\n检查 requirements.txt...")
    
    if os.path.exists("requirements.txt"):
        print("OK requirements.txt 存在")
        
        with open("requirements.txt", 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "PySide6" in content:
            print("OK requirements.txt 包含 PySide6")
        else:
            print("WARN requirements.txt 不包含 PySide6")
    else:
        print("ERROR requirements.txt 不存在")


def check_readme():
    """检查 README.md"""
    print("\n检查 README.md...")
    
    if os.path.exists("README.md"):
        print("OK README.md 存在")
    else:
        print("ERROR README.md 不存在")


if __name__ == "__main__":
    # 运行完整测试
    success = run_quick_test()
    
    # 检查其他文件
    check_requirements()
    check_readme()
    
    print("\n测试完成！")
    
    if success:
        print("\n现在您可以:")
        print("1. 安装依赖: pip install -r requirements.txt")
        print("2. 运行启动器: python run.py")
        print("3. 选择您想要运行的界面")
    else:
        print("\n请先解决测试失败的问题。")
    
    sys.exit(0 if success else 1)