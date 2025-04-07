#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start the app with gevent worker instead of eventlet
cd server && gunicorn --worker-class gevent -w 1 app:app 