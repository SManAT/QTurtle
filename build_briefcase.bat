@echo off
REM Build QTurtle with Briefcase and copy output to dist folder

setlocal enabledelayedexpansion

REM Output directory variables
set "BRIEFCASE_SOURCE=build\app\windows\app\src"
set "OUTPUT_DIR=dist\QCodeBriefcase"

echo ================================================
echo Building App with Briefcase
echo ================================================
echo.

REM Run Briefcase build
echo Running: briefcase create windows
call briefcase create windows
if errorlevel 1 (
    echo ERROR: Briefcase create failed
    exit /b 1
)

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

REM Clean old build
if exist "%OUTPUT_DIR%" (
    echo Cleaning old build...
    rmdir /s /q "%OUTPUT_DIR%"
)

REM Create output directory
mkdir "%OUTPUT_DIR%"
echo Created: %OUTPUT_DIR%

REM Copy all files from source to output
echo Copying files from %BRIEFCASE_SOURCE% to %OUTPUT_DIR%...
xcopy /E /I /Y "%BRIEFCASE_SOURCE%\*" "%OUTPUT_DIR%\" > nul

if errorlevel 1 (
    echo ERROR: Copy operation failed
    exit /b 1
)

echo.
echo ================================================
echo Build complete!
echo Executable: %OUTPUT_DIR%\<App>.exe
echo ================================================
