@echo off
echo ================================================
echo Building QTurtle with PyOxidizer
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

REM Install/upgrade PyOxidizer if needed
echo Checking PyOxidizer...
pip show pyoxidizer >nul 2>&1
if errorlevel 1 (
    echo Installing PyOxidizer...
    pip install pyoxidizer
)

REM Build with PyOxidizer
echo.
echo Building application with PyOxidizer...
echo This may take a few minutes on first build...
echo.
pyoxidizer build

echo.
echo ================================================
echo Build complete!
echo Executable: target\release\qturtle.exe
echo ================================================
