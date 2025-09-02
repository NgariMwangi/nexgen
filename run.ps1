Write-Host "Installing Flask dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host ""
Write-Host "Starting NexGen Flask Application..." -ForegroundColor Green
Write-Host ""
Write-Host "The website will be available at: http://localhost:5000" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python main.py
