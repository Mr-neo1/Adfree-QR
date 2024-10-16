import qrcode
from flask import Flask, send_file, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Function to generate QR code and save itcle\
def generate_qr(link, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

# Route to render the form page with a background image
@app.route('/')
def home():
    return render_template('index.html')  # Serves the HTML form

# Route to generate QR and download it (via POST request)
@app.route('/generate_qr', methods=['POST'])
def download_qr():
    link = request.form.get('link')  # Get the link from the form data
    filename = 'qrcode.png'
    
    if link:
        generate_qr(link, filename)
        return send_file(filename, as_attachment=True)
    else:
        return "Please provide a valid link", 400

# Route to suppress favicon error
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
