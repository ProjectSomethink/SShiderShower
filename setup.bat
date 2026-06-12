@echo off
:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found! Please install Python from python.org.
    pause
    exit /b
)

echo Installing dependencies...
python -m pip install -r requirements.txt

echo.
echo Setup complete!
echo You can now run the program using 'main.py' or compile it.
pause