# Viktor Nagels
import qrcode


qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)

data = input(str("qr code information: "))

qr.add_data(data)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
