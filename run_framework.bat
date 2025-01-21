@echo off
:: Prompt the user to choose a browser
echo Please choose a browser:
echo 1. Chrome
echo 2. Edge
set /p BROWSER_CHOICE="Enter the number (1 or 2): "

:: Set the browser based on user input and convert to lowercase
if "%BROWSER_CHOICE%"=="1" (
    set BROWSER=chrome
) else if "%BROWSER_CHOICE%"=="2" (
    set BROWSER=edge
) else (
    echo Invalid choice. Defaulting to Chrome.
    set BROWSER=chrome
)

:: Convert the browser name to lowercase (in case of accidental capitalization)
for %%i in (%BROWSER%) do set BROWSER=%%i

:: Activate the virtual environment
call "%~dp0venv\Scripts\activate.bat"

:: Run pytest with the specified browser
pytest --browser_name=%BROWSER% --html=report.html --self-contained-html

:: Deactivate the virtual environment
deactivate

pause
