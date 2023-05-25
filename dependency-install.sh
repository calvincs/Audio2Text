#!/bin/bash

## Setup dependencies based on OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # LINUX
    if [ -f /etc/lsb-release ] || [ -f /etc/debian_version ]; then
        # Ubuntu/Debian
        if ! ffmpeg -version &> /dev/null; then
            sudo apt-get update && sudo apt-get install -y ffmpeg
        fi
    elif [ -f /etc/redhat-release ]; then
        # CentOS/RHEL
        if ! ffmpeg -version &> /dev/null; then
            sudo yum install -y ffmpeg
        fi
    else
        echo "Unsupported Linux distribution. Please install ffmpeg manually."
    fi
    if ! pip show setuptools-rust &> /dev/null; then
        pip install setuptools-rust
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # MACOS
    if ! brew list --versions ffmpeg &> /dev/null; then
        brew install ffmpeg
    fi
    if ! pip show setuptools-rust &> /dev/null; then
        pip install setuptools-rust
    fi
else
    echo "Unsupported operating system. Please install ffmpeg and setuptools-rust manually."
fi

## Setup Python Environment
# Get the path to the Python3 interpreter
PYTHON=$(which python3)

# Create a virtual environment
$PYTHON -m venv a2text

# Activate the virtual environment
source a2text/bin/activate

# Now we are in the virtual environment, install Python dependencies
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
