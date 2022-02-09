import pyotp
import qrcode
from tkinter import *      

def totp_check(event):
    # Add a offset of 1
    if totp.verify(entry.get(), valid_window=1):
        print("Yes the code is indeed " + totp.now())
    else:
        print("Correct code was " + totp.now())

# Generating TOTP
key = pyotp.random_base32()
# Save key some where
totp = pyotp.TOTP(key)
# Generating link 
link = pyotp.totp.TOTP(key).provisioning_uri(name="jimmylinabcd@gmail.com", issuer_name="Python TOTP by Jimmy Lin")

# Generating QR code
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode001.png")

# GUI application
window = Tk()
window.geometry("545x595")
window.resizable(False, False)

# Displaying QR Code as image
canvas = Canvas(window, width = 545, height = 545)      
canvas.pack()      
img = PhotoImage(file="qrcode001.png")      
canvas.create_image(-20,-20, anchor=NW, image=img)

# Entry for user input
entry = Entry(window, width=545, font = "Calibri 24")
entry.pack() 

# Binding entry to enter
# TODO: Limit to 5 per 30 seconds to stop brute forcing
entry.bind("<Return>", totp_check)

mainloop()
