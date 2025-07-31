#!/bin/bash
set -e

echo "🚀 Starting Render deployment..."

# Check if we're in a Python environment
if command -v python &> /dev/null; then
    echo "✅ Python is available"
    python --version
else
    echo "❌ Python not found"
    exit 1
fi

# Check if wsgi.py exists
if [ -f "wsgi.py" ]; then
    echo "✅ wsgi.py found"
else
    echo "❌ wsgi.py not found"
    exit 1
fi

# Test the Flask app
echo "🧪 Testing Flask app..."
python -c "
import sys
sys.path.insert(0, 'web')
from api import app
print('✅ Flask app loaded successfully')
"

echo "✅ Render deployment ready!" 