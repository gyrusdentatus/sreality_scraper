#!/bin/bash

# Define the project base directory
BASE_DIR="$(dirname "$0")"

# Path to the virtual environment
VENV_PATH="$BASE_DIR/venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Virtual environment not found. Attempting to create one..."
    python3 -m venv "$VENV_PATH"
    # Check if virtual environment creation was successful
    if [ $? -eq 0 ]; then
        echo "Virtual environment created successfully."
    else
        echo "Failed to create virtual environment. Please create it manually with 'python3 -m venv venv'."
        exit 1
    fi
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Check for command line arguments
if [ "$1" = "setup" ]; then
    "$BASE_DIR/manage.sh" setup
elif [ "$1" = "run" ]; then
    "$BASE_DIR/manage.sh" scrape
elif [ "$1" = "visualize" ]; then
    "$BASE_DIR/manage.sh" visualize
else
    echo "Usage: $(basename "$0") {setup|run|visualize}"
    echo "setup: Setup the environment and install dependencies."
    echo "run: Fetch data from the API and save it to the database."
    echo "visualize: Generate visualizations based on the saved data."
    exit 1
fi

