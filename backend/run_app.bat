@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Step 1: Set environment and paths
SET VENV_DIR=venv
SET PYTHON=python
SET REQUIREMENTS=requirements.txt
SET APP_PATH=app.main:app

REM Step 2: Check if venv exists
IF NOT EXIST "%VENV_DIR%\Scripts\activate.bat" (
    echo Virtual environment not found. Creating one...
    %PYTHON% -m venv %VENV_DIR%
    
    IF ERRORLEVEL 1 (
        echo Failed to create virtual environment.
        exit /b 1
    )
)

REM Step 3: Activate virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

REM Confirm venv activation by checking python executable path
for /f "delims=" %%i in ('where python') do (
    set PYTHON_PATH=%%i
    goto :breakloop
)
:breakloop

echo Using Python interpreter at: !PYTHON_PATH!

REM Step 4: Install dependencies
IF EXIST "%REQUIREMENTS%" (
    echo Installing dependencies from %REQUIREMENTS%...
    pip install --upgrade pip >nul
    pip install -r %REQUIREMENTS%
) ELSE (
    echo requirements.txt not found. Skipping dependency installation.
)

REM Step 5: Run the app
echo Running FastAPI app...
uvicorn %APP_PATH% --reload

pause
ENDLOCAL
