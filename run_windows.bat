@echo off
title Smart Water Tank Monitoring Agent
echo ============================================
echo   Smart Water Tank Monitoring Agent
echo ============================================
echo.
where py >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_CMD=py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set PYTHON_CMD=python
    ) else (
        echo Python was not found.
        echo Install Python 3.10 or newer from https://www.python.org/downloads/
        echo During installation, tick "Add Python to PATH".
        pause
        exit /b 1
    )
)
echo Installing required package...
%PYTHON_CMD% -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo Package installation failed. Check internet connection and Python installation.
    pause
    exit /b 1
)
echo.
echo Starting the app in your browser...
%PYTHON_CMD% -m streamlit run app.py
pause
