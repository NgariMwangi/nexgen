from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for products page
@app.route('/products')
def products():
    return render_template('products.html')

# Route for services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for fuel related services
@app.route('/fuelrelated')
def fuelrelated():
    return render_template('fuelrelated.html')

# Route for non-fuel related services
@app.route('/nonfuelrelated')
def nonfuelrelated():
    return render_template('nonfuelrelated.html')

# Route for solar systems
@app.route('/solarsystems')
def solarsystems():
    return render_template('solarsystems.html')

# Route for gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route for contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for tenders
@app.route('/tenders')
def tenders():
    return render_template('tenders.html')

# Route for Afri Fuel Expo
@app.route('/afrifuel-expo-2025')
def afrifuel_expo():
    return render_template('afrifuel-expo-2025.html')

# Route for launderette
@app.route('/launderette')
def launderette():
    return render_template('launderette.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
