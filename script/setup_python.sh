#!/usr/bin/env bash
set -e


echo "Creating python virtual env..."
$(command -v python3) -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install --upgrade -r requirements.txt
[[ -f requirements-dev.txt ]] && pip install --upgrade -r requirements-dev.txt

echo "Done! Python is set up! You can now do 'source venv/bin/activate'"
