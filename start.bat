@echo off
echo =========================================================================
echo    AI-Based Laptop Problem Diagnosis System (AO* Search Engine)
echo =========================================================================
echo.
echo Starting Backend and Frontend services...
echo.

start "Laptop AI - Backend (Port 8080)" cmd /k "python -m uvicorn backend.main:app --host 127.0.0.1 --port 8080 --reload"

timeout /t 3 /nobreak >nul

cd frontend
start "Laptop AI - Frontend (Port 5173)" cmd /k "npm run dev"

timeout /t 3 /nobreak >nul

echo.
echo Launching Web Application in default browser...
start http://localhost:5173

echo.
echo =========================================================================
echo App running at:
echo   - Web UI: http://localhost:5173
echo   - API Swagger Docs: http://localhost:8080/docs
echo =========================================================================
