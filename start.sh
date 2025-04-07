#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start the app directly with Python - most reliable option
cd server && python app.py 