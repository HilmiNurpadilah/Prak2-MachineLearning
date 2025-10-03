@echo off
echo ========================================
echo    Running Flask App with Virtual Env
echo ========================================
echo.

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Flask application...
echo Server will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

echo.
echo Deactivating virtual environment...
deactivate
echo.
pause
