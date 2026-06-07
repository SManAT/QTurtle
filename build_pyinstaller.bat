@echo off
setlocal enabledelayedexpansion

REM Output directory variables
set "OUTPUT_DIR=dist\QTurtle"

echo ================================================
echo Building App with PyInstaller
echo ================================================
echo.
echo What will be done:
echo  1. Clean old build artifacts (dist, build, __pycache__)
echo  2. Check/install PyInstaller and tomli
echo  3. Run auto_build.py to create executable
echo  4. Output: %OUTPUT_DIR%\
echo  5. To enable compression for PyInstaller, download upx.exe from upx.github.io (https://upx.github.io/).
echo     and set upx_dir in pyproject.toml
echo.
echo  6. Check pyproject.toml for correct build parameters!
echo.
echo.
set /p PROCEED="Proceed? (y/N): "
if /i not "%PROCEED%"=="y" (
    echo Cancelled.
    exit /b 0
)
echo.

REM Clean old build artifacts
echo Cleaning old build artifacts...
if exist dist rmdir /s /q %OUTPUT_DIR%
if exist build rmdir /s /q build
if exist __pycache__ rmdir /s /q __pycache__
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
    pip install pyinstaller>=6.0.0
) else (
    echo PyInstaller installed
)

echo Checking tomli (for Python 3.10 and earlier)...
pip show tomli >nul 2>&1
if errorlevel 1 (
    echo Installing tomli...
    pip install tomli
) else (
    echo tomli installed
)

REM UPX is optional: reduces executable size via compression
REM Download from https://upx.github.io/ and place upx.exe in PATH,
REM or set upx_dir in pyproject.toml [tool.qturtle_app.build]
where upx >nul 2>&1
if errorlevel 1 (
    echo Note: UPX not found in PATH - compression will be skipped
    echo       Download from https://upx.github.io/ to enable
) else (
    echo UPX found - compression enabled
)

REM Verify PyInstaller installation
echo.
echo Verifying installation...
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: PyInstaller installation failed!
    exit /b 1
)
echo All dependencies ready

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM Build
echo.
echo Building application...
python auto_build.py

echo.
echo ================================================
echo Build complete!
echo Executable in : %OUTPUT_DIR%
REM size from Output
powershell -NoProfile -Command "$b = (Get-ChildItem '%OUTPUT_DIR%' -Recurse 2>$null | Measure-Object -Property Length -Sum).Sum; $gb = $b/1GB; $mb = $b/1MB; $kb = $b/1KB; if ($gb -ge 1) { \"$([math]::Round($gb,2)) GB\" } elseif ($mb -ge 1) { \"$([math]::Round($mb,2)) MB\" } elseif ($kb -ge 1) { \"$([math]::Round($kb,2)) KB\" } elseif ($b -gt 0) { \"$b bytes\" } else { \"0 bytes\" }"
echo ================================================
