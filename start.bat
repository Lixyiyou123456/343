@echo off
chcp 65001 > nul
echo ========================================
echo      PySide6 Interface Example Launcher
echo ========================================
echo.

:menu
echo Please select a program to run:
echo.
echo  1) Run Interface Launcher (Recommended)
echo  2) Run Full-Feature Interface
echo  3) Run Simple Interface
echo  4) Run Modern Dashboard
echo  5) Run Interface Test
echo  6) Install Dependencies
echo  7) Exit

echo.

set /p choice="Please enter your choice (1-7): "

if "%choice%"=="1" goto run_launcher
if "%choice%"=="2" goto run_main
if "%choice%"=="3" goto run_simple
if "%choice%"=="4" goto run_dashboard
if "%choice%"=="5" goto run_test
if "%choice%"=="6" goto install_deps
if "%choice%"=="7" goto exit
echo Invalid choice, please try again
goto menu

:run_launcher
echo.
echo Starting Interface Launcher...
python run.py
goto menu

:run_main
echo.
echo Starting Full-Feature Interface...
python main.py
goto menu

:run_simple
echo.
echo Starting Simple Interface...
python simple_ui.py
goto menu

:run_dashboard
echo.
echo Starting Modern Dashboard...
python dashboard.py
goto menu

:run_test
echo.
echo Running Interface Test...
python test_ui.py
goto menu

:install_deps
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Dependencies installed successfully!
pause
goto menu

:exit
echo.
echo Thank you for using PySide6 Interface Examples!
echo.
pause