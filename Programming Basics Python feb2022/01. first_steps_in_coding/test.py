import pyqrcode
from pyqrcode import QRCode

adress = "https://www.facebook.com/pecata.dimitrov"
url = pyqrcode.create(adress)
url.png("petko.png, scale=8")