# NexGen Fuel Works - Flask Application

This is a Flask web application converted from the original HTML website.

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application:**
   ```bash
   python main.py
   ```

3. **Access the website:**
   Open your browser and go to: `http://localhost:5000`

## Available Routes

- `/` - Home page
- `/about` - About us page
- `/products` - Products page
- `/services` - Services page
- `/fuelrelated` - Fuel related services
- `/nonfuelrelated` - Non-fuel related services
- `/solarsystems` - Solar systems
- `/gallery` - Gallery
- `/contact` - Contact us
- `/tenders` - Tenders
- `/afrifuel-expo-2025` - Afri Fuel Expo
- `/launderette` - Launderette

## File Structure

- `main.py` - Main Flask application with all routes
- `templates/` - HTML template files
- `static/` - Static assets (CSS, JS, images, JSON, PDFs)
  - `css/` - CSS stylesheets
  - `js/` - JavaScript files
  - `images/` - Image assets
  - `json/` - JSON configuration files
  - `*.pdf` - PDF documents

## Features

- All original HTML pages are preserved
- Flask's built-in static file serving for CSS, JS, images, and other assets
- Clean URL routing
- Responsive design maintained
- Proper Flask project structure following best practices

## Quick Start

**Windows users:** Double-click `run.bat` to install dependencies and start the server.

**PowerShell users:** Run `.\run.ps1` to start the application.

**Command line users:** 
```bash
pip install -r requirements.txt
python main.py
```
