@echo off
:: Create a virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Install dependencies
pip install -r requirements.txt

:: Deactivate the virtual environment
deactivate

echo "Setup complete! Dependencies are installed."

pause