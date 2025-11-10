#!/bin/bash

# This script will install the necessary dependencies and start the website.

# Step 1: Install dependencies
echo "Installing dependencies..."
pip install flask werkzeug PyPDF2

# Step 2: Start the Flask application
echo "Starting the website..."
echo "You can access the website at http://127.0.0.1:5000"
python app.py
