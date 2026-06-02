@echo off
echo ================================================
echo Building QTurtle with Briefcase
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

REM Install/upgrade Briefcase if needed
echo Checking Briefcase...
pip show briefcase >nul 2>&1
if errorlevel 1 (
    echo Installing Briefcase...
    pip install briefcase
)

REM Build with Briefcase
echo.
echo Creating/building application with Briefcase...
echo.

REM Check if briefcase project already exists
if not exist "src\qturtle\__main__.py" (
    echo Initializing Briefcase project structure...
    briefcase create windows
)

echo Building for Windows...
briefcase build windows

echo.
echo ================================================
echo Build complete!
echo Executable: build\qturtle\windows\app\QTurtle.exe
echo ================================================
echo.
echo Optional: Package for distribution
echo   briefcase package windows
echo.
