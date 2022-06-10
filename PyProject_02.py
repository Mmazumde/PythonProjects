# This is a sample Python script.
# Create a QR Code with python.

import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.linkedin.com/in/mohiuddin-mazumder-76b8bb48/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming
url.svg("mylinkedin.svg", scale = 10)
