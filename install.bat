@echo off
REM Malformed URL Detector - Windows Installation Script

echo Installing Malformed URL Detector...

REM Create a virtual environment (optional but recommended)
echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM No additional dependencies needed for this tool as it only uses Python standard library
echo No additional dependencies required. Tool ready to use!

echo.
echo Installation complete!
echo You can run the tool using: python malformed_urls.py ^<path_to_log_file^>
echo. 