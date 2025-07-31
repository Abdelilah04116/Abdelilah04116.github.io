#!/bin/bash
set -e

echo "🚀 Starting build process..."

# Upgrade pip and install build dependencies
echo "📦 Upgrading pip and build dependencies..."
pip install --upgrade pip setuptools wheel

# Install requirements
echo "📋 Installing Python requirements..."
pip install -r requirements.txt

# Verify the wsgi.py file exists
echo "🔍 Verifying wsgi.py exists..."
if [ ! -f "wsgi.py" ]; then
    echo "❌ Error: wsgi.py not found!"
    exit 1
fi

# Test import
echo "🧪 Testing Python imports..."
python -c "import wsgi; print('✅ wsgi.py imports successfully')"

echo "✅ Build completed successfully!" 