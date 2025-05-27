#!/bin/bash

# Step 1: Set environment and paths
VENV_DIR="venv"
PYTHON="python3"
REQUIREMENTS="requirements.txt"
APP_PATH="app.main:app"

# Step 2: Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    $PYTHON -m venv "$VENV_DIR"
    
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

# Step 3: Activate virtual environment
source "$VENV_DIR/bin/activate"

# Confirm venv activation
PYTHON_PATH=$(which python)
echo "Using Python interpreter at: $PYTHON_PATH"

# Step 4: Install dependencies
if [ -f "$REQUIREMENTS" ]; then
    echo "Installing dependencies from $REQUIREMENTS..."
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS"
else
    echo "$REQUIREMENTS not found. Skipping dependency installation."
fi

# Step 5: Run the app
echo "Running FastAPI app..."
uvicorn "$APP_PATH" --reload
