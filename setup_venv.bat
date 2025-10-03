@echo off
echo ========================================
echo    Setup Virtual Environment
echo ========================================
echo.

echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Virtual environment setup complete!
echo ========================================
echo.
echo To activate venv in the future, run:
echo venv\Scripts\activate.bat
echo.
echo To deactivate, run:
echo deactivate
echo.
pause
