@echo off
setlocal enabledelayedexpansion

set "OUTPUT_DIR=dist\QTurtle"
set "CXFREEZE_TEMP=build\cxfreeze_temp"

echo ================================================
echo Building App with cx_Freeze
echo ================================================
echo.
echo What will be done:
echo  1. Check/install cx_Freeze
echo  2. Build APP to standalone executable via setup_cxfreeze.py
echo  3. Copy output to: %OUTPUT_DIR%\
echo.
echo  Check setup_cxfreeze.py for build parameters!
echo.
set /p PROCEED="Proceed? (y/N): "
if /i not "%PROCEED%"=="y" (
    echo Cancelled.
    exit /b 0
)
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

REM Check for cx_Freeze
echo Checking cx_Freeze...
pip show cx-freeze >nul 2>&1
if errorlevel 1 (
    echo Installing cx_Freeze...
    pip install cx-freeze
) else (
    echo cx_Freeze installed
)

REM Verify cx_Freeze
echo.
echo Verifying installation...
python -c "import cx_Freeze" >nul 2>&1
if errorlevel 1 (
    echo ERROR: cx_Freeze not found!
    exit /b 1
)
echo All dependencies ready

REM Clean old output
echo.
echo Cleaning old build artifacts...
if exist "%OUTPUT_DIR%" rmdir /s /q "%OUTPUT_DIR%"
if exist "%CXFREEZE_TEMP%" rmdir /s /q "%CXFREEZE_TEMP%"
if exist __pycache__ rmdir /s /q __pycache__
echo.
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

echo Building with cx_Freeze...
python setup_cxfreeze.py build_exe

if errorlevel 1 (
    echo.
    echo ERROR: cx_Freeze build failed!
    exit /b 1
)

REM Move output to final location
echo.
echo Moving output to %OUTPUT_DIR%...
if exist "%CXFREEZE_TEMP%" (
    xcopy /E /I /Y "%CXFREEZE_TEMP%\*" "%OUTPUT_DIR%\" >nul 2>&1
) else (
    echo ERROR: Build output not found at expected path: %CXFREEZE_TEMP%
    echo Check setup_cxfreeze.py build_exe path setting.
    exit /b 1
)

REM Clean leftover build folder if empty
for /d %%i in (build) do (
    rd "%%i" 2>nul
)

echo.
echo ================================================
echo Build complete!
echo Executable in : %OUTPUT_DIR%\
REM size from Output
powershell -NoProfile -Command "$b = (Get-ChildItem '%OUTPUT_DIR%' -Recurse 2>$null | Measure-Object -Property Length -Sum).Sum; $gb = $b/1GB; $mb = $b/1MB; $kb = $b/1KB; if ($gb -ge 1) { \"$([math]::Round($gb,2)) GB\" } elseif ($mb -ge 1) { \"$([math]::Round($mb,2)) MB\" } elseif ($kb -ge 1) { \"$([math]::Round($kb,2)) KB\" } elseif ($b -gt 0) { \"$b bytes\" } else { \"0 bytes\" }"
echo ================================================
