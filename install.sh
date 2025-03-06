#!/bin/bash

# Malformed URL Detector - Installation Script
# This script sets up the malformed URL detector tool

echo "Installing Malformed URL Detector..."

# Create a virtual environment (optional but recommended)
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# No additional dependencies needed for this tool as it only uses Python standard library
echo "No additional dependencies required. Tool ready to use!"

# Create a symlink to make the tool available system-wide (optional)
# Requires sudo access
if [ "$1" == "--system" ]; then
    echo "Creating system-wide symlink (requires sudo)..."
    sudo ln -sf "$(pwd)/malformed_urls.py" /usr/local/bin/malformed-url-detector
    sudo chmod +x /usr/local/bin/malformed-url-detector
    echo "You can now run the tool using: malformed-url-detector <path_to_log_file>"
else
    # Make the script executable
    chmod +x malformed_urls.py
    echo "Tool installed successfully!"
    echo "You can run it using: python3 malformed_urls.py <path_to_log_file>"
    echo ""
    echo "To install system-wide, run: ./install.sh --system"
fi

echo ""
echo "Installation complete!" 