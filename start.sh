#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start the app with gunicorn and eventlet worker
cd server && gunicorn --worker-class eventlet -w 1 app:app 