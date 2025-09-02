@echo off
echo Installing Flask dependencies...
pip install -r requirements.txt

echo.
echo Starting NexGen Flask Application...
echo.
echo The website will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python main.py

pause
