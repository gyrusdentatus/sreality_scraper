#!/bin/bash

function setup_environment() {
    echo "Setting up the environment..."
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Environment setup completed."
}

function run_scraper() {
    source venv/bin/activate
    echo "Running the scraper..."
    python main.py --mode fetch
}

function init_database() {
    source venv/bin/activate
    echo "Initializing the database..."
    python main.py --mode db_init
}

function run_visualization() {
    source venv/bin/activate
    echo "Generating visualizations..."
    python main.py --mode visualize
}

function docker_build() {
    echo "Building Docker container..."
    docker build -t sreality_scraper .
}

function docker_run() {
    echo "Running Docker container..."
    docker run --rm sreality_scraper
}

case "$1" in
    setup)
        setup_environment
        ;;
    scrape)
        run_scraper
        ;;
    initdb)
        init_database
        ;;
    visualize)
        run_visualization
        ;;
    docker-build)
        docker_build
        ;;
    docker-run)
        docker_run
        ;;
    *)
        echo "Usage: $0 {setup|scrape|initdb|visualize|docker-build|docker-run}"
        exit 1
        ;;
esac

