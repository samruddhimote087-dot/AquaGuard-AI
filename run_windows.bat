@echo off
cd /d "%~dp0"
echo ==========================================
echo       AquaGuard AI - Setup and Run
echo ==========================================
where py >nul 2>nul
if %errorlevel%==0 (
  set PY=py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (set PY=python) else (
    echo Python was not found. Install Python 3.10 or newer from https://www.python.org/downloads/
    echo During installation, tick "Add Python to PATH".
    pause
    exit /b 1
  )
)
%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt
if errorlevel 1 (
  echo Dependency installation failed. Check your internet connection and Python installation.
  pause
  exit /b 1
)
%PY% -m streamlit run app.py
pause
