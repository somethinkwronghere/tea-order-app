#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start using Procfile or direct Python if Procfile fails
if [ -f "Procfile" ]; then
  echo "Running with Procfile"
  PORT=$PORT python -m gunicorn.app.wsgiapp -f Procfile
else
  echo "Running with Python directly"
  cd server && python app.py
fi 