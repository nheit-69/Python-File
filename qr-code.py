# import qrcode
# img = qrcode.make('https://www.amazon.com ')
# img.save("paytmcash2.jpg")




import qrcode
from PIL import Image

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.amazon.com')
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Load the image you want to add in the center
logo = Image.open('paytmcash2.jpg')

# Calculate the size for the logo (scaling down if needed)
basewidth = 100  # Set a base width for the logo
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# Calculate the position for the logo
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

# Paste the logo on the QR code
img.paste(logo, pos)

# Save the final image
img.save('paytmcash2_with_logo.jpg')






















# import qrcode
# img = qrcode.make('hello world')
# img.save("nat.jpg")











