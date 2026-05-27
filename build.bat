@echo off
echo ================================================
echo Building with PyInstaller
echo ================================================

REM Check if .venv exists
if not exist .venv (
    echo Error: .venv not found!
    echo Please create virtual environment first:
    echo   install.bat
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Verify activation
echo.
echo Python: %PYTHON%
python --version
echo.

REM Install/upgrade PyInstaller if needed
echo Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Build
echo.
echo Building application...
python auto_build.py

REM Deactivate
call deactivate

echo.
echo ================================================
echo Build complete!
echo Executable: in dist\*.exe
echo ================================================
