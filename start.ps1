Write-Host "========================================" -ForegroundColor Cyan
Write-Host "      PySide6 Interface Example Launcher" -ForegroundColor Cyan
Write-Host " ========================================" -ForegroundColor Cyan
Write-Host

function Show-Menu {
    Write-Host "Please select a program to run:" -ForegroundColor Green
    Write-Host
    Write-Host "  1) Run Interface Launcher (Recommended)"
    Write-Host "  2) Run Full-Feature Interface"
    Write-Host "  3) Run Simple Interface"
    Write-Host "  4) Run Modern Dashboard"
    Write-Host "  5) Run Interface Test"
    Write-Host "  6) Install Dependencies"
    Write-Host "  7) Exit"
    Write-Host
}

function Run-Launcher {
    Write-Host "Starting Interface Launcher..." -ForegroundColor Yellow
    python run.py
}

function Run-Main {
    Write-Host "Starting Full-Feature Interface..." -ForegroundColor Yellow
    python main.py
}

function Run-Simple {
    Write-Host "Starting Simple Interface..." -ForegroundColor Yellow
    python simple_ui.py
}

function Run-Dashboard {
    Write-Host "Starting Modern Dashboard..." -ForegroundColor Yellow
    python dashboard.py
}

function Run-Test {
    Write-Host "Running Interface Test..." -ForegroundColor Yellow
    python test_ui.py
}

function Install-Deps {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
    Read-Host "Press Enter to continue..."
}

while ($true) {
    Show-Menu
    $choice = Read-Host "Please enter your choice (1-7)"
    
    switch ($choice) {
        "1" { Run-Launcher }
        "2" { Run-Main }
        "3" { Run-Simple }
        "4" { Run-Dashboard }
        "5" { Run-Test }
        "6" { Install-Deps }
        "7" {
            Write-Host "Thank you for using PySide6 Interface Examples!" -ForegroundColor Green
            Write-Host
            Read-Host "Press Enter to exit..."
            break
        }
        default {
            Write-Host "Invalid choice, please try again" -ForegroundColor Red
        }
    }
    
    if ($choice -eq "7") {
        break
    }
    
    Write-Host
}
