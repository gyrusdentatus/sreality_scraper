#!/bin/bash

# Source the virtual environment
source venv/bin/activate

# Check for command line arguments
if [ "$1" = "setup" ]; then
    ./manage.sh setup
elif [ "$1" = "run" ]; then
    ./manage.sh scrape
elif [ "$1" = "visualize" ]; then
    ./manage.sh visualize
else
    echo "Usage: start.sh {setup|run|visualize}"
    echo "setup: Setup the environment and install dependencies."
    echo "run: Fetch data from the API and save it to the database."
    echo "visualize: Generate visualizations based on the saved data."
fi

