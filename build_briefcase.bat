@echo off
REM Build with Briefcase and copy output to dist folder

setlocal enabledelayedexpansion

set "FORMAL_NAME=QTurtle"
set "APP_ID=qturtle"
set "BRIEFCASE_SOURCE=build\%APP_ID%\windows\app\src"
set "OUTPUT_DIR=dist\%FORMAL_NAME%Briefcase"

echo ================================================
echo Building App with Briefcase
echo ================================================
echo.
echo App ID     : %APP_ID%
echo Formal name: %FORMAL_NAME%
echo.
echo What will be done:
echo  1. Check/install Briefcase
echo  2. Clean old build artifacts (dist, build, __pycache__)
echo  3. Run briefcase create windows
echo  4. Run briefcase build windows
echo  5. Copy executable to: %OUTPUT_DIR%\
echo.
echo  6. Check pyproject.toml for correct build parameters!
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

REM Check for Briefcase
echo Checking Briefcase...
pip show briefcase >nul 2>&1
if errorlevel 1 (
    echo Installing Briefcase...
    pip install briefcase>=0.3.0
) else (
    echo Briefcase installed
)

REM Verify Briefcase installation
echo.
echo Verifying installation...
briefcase --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Briefcase installation failed!
    exit /b 1
)
echo All dependencies ready

REM Clean old build artifacts
echo.
echo Cleaning old build artifacts...
if exist "%OUTPUT_DIR%" rmdir /s /q "%OUTPUT_DIR%"
if exist build rmdir /s /q build
if exist __pycache__ rmdir /s /q __pycache__
if exist src\%APP_ID%\__pycache__ rmdir /s /q src\%APP_ID%\__pycache__
echo.

echo Creating Briefcase project structure...
call briefcase create windows

echo.
echo Running: briefcase build windows
call briefcase build windows
if errorlevel 1 (
    echo ERROR: Briefcase build failed
    exit /b 1
)

echo.
echo ================================================
echo Copying executable to dist folder
echo ================================================
echo.

REM Check if source directory exists
if not exist "%BRIEFCASE_SOURCE%" (
    echo ERROR: Briefcase output directory not found
    echo Expected: %BRIEFCASE_SOURCE%
    exit /b 1
)

REM Clean old output and copy fresh build
if exist "%OUTPUT_DIR%" (
    echo Cleaning old output...
    rmdir /s /q "%OUTPUT_DIR%"
)

mkdir "%OUTPUT_DIR%"
echo Created: %OUTPUT_DIR%

echo Copying files from %BRIEFCASE_SOURCE% to %OUTPUT_DIR%...
xcopy /E /I /Y "%BRIEFCASE_SOURCE%\*" "%OUTPUT_DIR%\" >nul 2>&1

if errorlevel 1 (
    echo Trying robocopy...
    robocopy "%BRIEFCASE_SOURCE%" "%OUTPUT_DIR%" /E /Y
    if errorlevel 8 (
        echo ERROR: Copy operation failed
        exit /b 1
    )
)

echo.
echo ================================================
echo Build complete!
echo Executable in : %OUTPUT_DIR%
powershell -NoProfile -Command "$b = (Get-ChildItem '%OUTPUT_DIR%' -Recurse 2>$null | Measure-Object -Property Length -Sum).Sum; $gb = $b/1GB; $mb = $b/1MB; $kb = $b/1KB; if ($gb -ge 1) { \"$([math]::Round($gb,2)) GB\" } elseif ($mb -ge 1) { \"$([math]::Round($mb,2)) MB\" } elseif ($kb -ge 1) { \"$([math]::Round($kb,2)) KB\" } elseif ($b -gt 0) { \"$b bytes\" } else { \"0 bytes\" }"
echo ================================================
