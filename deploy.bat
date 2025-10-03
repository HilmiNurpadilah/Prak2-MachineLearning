@echo off
echo ========================================
echo    Railway Deployment Helper
echo ========================================
echo.

echo Checking Git status...
git status

echo.
echo ========================================
echo Step 1: Add all files to Git
echo ========================================
git add .

echo.
echo ========================================
echo Step 2: Commit changes
echo ========================================
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg="Update for Railway deployment"

git commit -m "%commit_msg%"

echo.
echo ========================================
echo Step 3: Push to repository
echo ========================================
echo Pushing to remote repository...
git push origin main

echo.
echo ========================================
echo Deployment files created:
echo - Procfile
echo - railway.json  
echo - requirements.txt (updated)
echo - .gitignore
echo - runtime.txt
echo - nixpacks.toml
echo - DEPLOYMENT.md
echo ========================================
echo.
echo Next steps:
echo 1. Go to railway.app
echo 2. Create new project
echo 3. Connect your GitHub repository
echo 4. Railway will auto-deploy your app!
echo.
echo Your app will be available at: https://your-app.railway.app
echo.
pause
