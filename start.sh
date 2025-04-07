#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start the app with waitress instead of gevent
cd server && python -m waitress --port=$PORT app:app 