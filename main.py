import qrcode

# create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
data = "https://www.linkedin.com/in/naval-prakash-364163244/"
qr.add_data(data)

# generate the QR code
qr.make(fit=True)

# create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# save the image
img.save("qr_code.png")
