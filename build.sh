#!/bin/bash
echo "Starting build process..."

# Upgrade pip and install build dependencies
pip install --upgrade pip setuptools wheel

# Install requirements
pip install -r requirements.txt

echo "Build completed successfully!" 