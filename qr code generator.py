# Viktor Nagels
import qrcode
from barcode import EAN13
# ?barcode as png
from barcode.writer import ImageWriter

qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)

# TODO data given in a qr code:
# qrcode data formaat = weblink/sublink/qrcode-unique id


data = input(str("qr code information: "))

qr.add_data(data)

# ?barcode as png
barcode = EAN13(data, writer=ImageWriter())

# ?barcode as svg
#barcode = EAN13(date)
barcode.save('barcode')

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
