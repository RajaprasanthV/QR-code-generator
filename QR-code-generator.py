import pyqrcode
import png
link = input("Enter your URL to generate QR code: ")
qr_code = pyqrcode.create(link)
file = input("Enter file Name to save QR: ")
qr_code.png(file + ".png", scale=5)
print("Your QR code generated!!")