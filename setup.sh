#!/bin/bash
# Setup script for Fyra Streamlit Map Application

echo "🚀 Setting up Fyra Streamlit Map Application..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV package manager..."
    pip install uv
else
    echo "✅ UV is already installed"
fi

# Create virtual environment
echo "🔧 Creating virtual environment..."
uv venv

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source .venv/bin/activate
uv pip install -r requirements.txt

echo ""
echo "✨ Setup complete!"
echo ""
echo "To run the application:"
echo "  1. Activate the virtual environment: source .venv/bin/activate"
echo "  2. Run the app: streamlit run app.py"
echo ""
