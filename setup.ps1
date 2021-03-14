# PowerShell script for setting up a Python virtual environment.

py -3.8 -m venv .venv                 # Create Python virtual environment
.\.venv\Scripts\Activate.ps1          # Activate the environment
pip install -U pip                    # Upgrade pip, [WinError 5] is okay
pip install -U setuptools             # Upgrae bundled setuptools
pip install -U wheel                  # Speed up subsequent package installs
pip install -U -r .\requirements.txt  # Install packages for development
