#!/bin/bash
# Ensure data directory exists
mkdir -p server/data
# Start with waitress
cd server && python -c "from waitress import serve; from app import app; serve(app, host='0.0.0.0', port=int(__import__('os').environ.get('PORT', 5000)))" 