#!/bin/bash

# PySide6 界面示例启动器

clear
echo "========================================"
echo "     PySide6 界面示例启动器"
echo "========================================"
echo ""

show_menu() {
    echo "请选择要运行的程序:"
    echo ""
    echo "  1) 运行界面启动器 (推荐)"
    echo "  2) 运行完整功能界面"
    echo "  3) 运行简洁界面"
    echo "  4) 运行现代化仪表板"
    echo "  5) 运行界面测试"
    echo "  6) 安装依赖"
    echo "  7) 退出"
    echo ""
}

run_launcher() {
    echo ""
    echo "正在启动界面启动器..."
    python3 run.py
}

run_main() {
    echo ""
    echo "正在启动完整功能界面..."
    python3 main.py
}

run_simple() {
    echo ""
    echo "正在启动简洁界面..."
    python3 simple_ui.py
}

run_dashboard() {
    echo ""
    echo "正在启动现代化仪表板..."
    python3 dashboard.py
}

run_test() {
    echo ""
    echo "正在运行界面测试..."
    python3 test_ui.py
}

install_deps() {
    echo ""
    echo "正在安装依赖..."
    pip3 install -r requirements.txt
    echo ""
    echo "依赖安装完成！"
    read -p "按回车键继续..."
}

while true; do
    show_menu
    read -p "请输入选项 (1-7): " choice
    
    case $choice in
        1)
            run_launcher
            ;;
        2)
            run_main
            ;;
        3)
            run_simple
            ;;
        4)
            run_dashboard
            ;;
        5)
            run_test
            ;;
        6)
            install_deps
            ;;
        7)
            echo ""
            echo "感谢使用 PySide6 界面示例！"
            echo ""
            exit 0
            ;;
        *)
            echo "无效选项，请重新输入"
            ;;
    esac
    
    echo ""
    read -p "按回车键返回菜单..."
    clear
done