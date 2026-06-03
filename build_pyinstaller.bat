@echo off
setlocal enabledelayedexpansion

REM Output directory variables
set "OUTPUT_DIR=dist\QrCode"

echo ================================================
echo Building App with PyInstaller
echo ================================================
echo.

REM Check if .venv exists, if so activate it
if exist .venv (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
) else (
    echo Using system Python
)

echo.
python --version
echo.

REM Install/upgrade PyInstaller and tomli if needed
echo Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo Checking tomli (for Python 3.10 and earlier)...
pip show tomli >nul 2>&1
if errorlevel 1 (
    echo Installing tomli...
    pip install tomli
)

REM Build
echo.
echo Building application...
python auto_build.py

echo.
echo ================================================
echo Build complete!
echo Executable: %OUTPUT_DIR%\
echo ================================================
