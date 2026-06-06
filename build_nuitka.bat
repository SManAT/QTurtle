@echo off
setlocal enabledelayedexpansion

set "OUTPUT_DIR=dist\QTurtleNuitka"
set "NUITKA_TEMP=dist\_nuitka_build"

echo ================================================
echo Building App with Nuitka
echo ================================================
echo.
echo What will be done:
echo  1. Check/install Nuitka (and ordered-set for faster compilation)
echo  2. Compile QTurtle to standalone executable
echo  3. Output: %OUTPUT_DIR%\QTurtle.exe
echo.
echo  Note: Nuitka compiles Python to C, then to native code.
echo        First run downloads the C compiler - may take extra time.
echo        Subsequent builds are faster.
echo.
echo  Check pyproject.toml for build parameters!
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

REM Check for Nuitka
echo Checking Nuitka...
pip show nuitka >nul 2>&1
if errorlevel 1 (
    echo Installing Nuitka...
    pip install nuitka
) else (
    echo Nuitka installed
)

REM Verify Nuitka
echo.
echo Verifying installation...
python -m nuitka --version 
if errorlevel 1 (
    echo ERROR: Nuitka not found!
    exit /b 1
)
echo All dependencies ready

REM Clean old output
echo.
echo Cleaning old build artifacts...
if exist "%OUTPUT_DIR%" rmdir /s /q "%OUTPUT_DIR%"
if exist "%NUITKA_TEMP%" rmdir /s /q "%NUITKA_TEMP%"
if exist __pycache__ rmdir /s /q __pycache__
if exist src\qturtle\__pycache__ rmdir /s /q src\qturtle\__pycache__
echo.

echo Building with Nuitka (this may take several minutes on first run)...
python -m nuitka ^
    --standalone ^
    --windows-disable-console ^
    --enable-plugin=pyside6 ^
    --follow-imports ^
    --include-data-dir=src/qturtle/css=qturtle/css ^
    --include-data-dir=src/qturtle/ui=qturtle/ui ^
    --windows-icon-from-ico=assets/app.ico ^
    --output-dir=%NUITKA_TEMP% ^
    --output-filename=QTurtle ^
    --python-flag=no_site ^
    --python-flag=no_docstrings ^
    --nofollow-import-to=matplotlib ^
    --nofollow-import-to=scipy ^
    --nofollow-import-to=numpy ^
    --nofollow-import-to=pandas ^
    --nofollow-import-to=PIL ^
    --nofollow-import-to=wx ^
    --nofollow-import-to=IPython ^
    --nofollow-import-to=jupyter ^
    --nofollow-import-to=tkinter ^
    --nofollow-import-to=PyQt6 ^
    --remove-output ^
    src/qturtle/__main__.py

if errorlevel 1 (
    echo.
    echo ERROR: Nuitka build failed!
    exit /b 1
)

REM Move dist folder to final output location
echo.
echo Moving output to %OUTPUT_DIR%...
set "NUITKA_DIST=%NUITKA_TEMP%\__main__.dist"
if exist "%NUITKA_DIST%" (
    move "%NUITKA_DIST%" "%OUTPUT_DIR%"
    rmdir /s /q "%NUITKA_TEMP%" 2>nul
) else (
    echo ERROR: Expected dist folder not found: %NUITKA_DIST%
    exit /b 1
)

echo.
echo ================================================
echo Build complete!
echo Executable in : %OUTPUT_DIR%\
REM size from Output
powershell -NoProfile -Command "$b = (Get-ChildItem '%OUTPUT_DIR%' -Recurse 2>$null | Measure-Object -Property Length -Sum).Sum; $gb = $b/1GB; $mb = $b/1MB; $kb = $b/1KB; if ($gb -ge 1) { \"$([math]::Round($gb,2)) GB\" } elseif ($mb -ge 1) { \"$([math]::Round($mb,2)) MB\" } elseif ($kb -ge 1) { \"$([math]::Round($kb,2)) KB\" } elseif ($b -gt 0) { \"$b bytes\" } else { \"0 bytes\" }"
echo ================================================
