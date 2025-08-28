import qrcode as qr
qrImg = qr.make("https://www.linkedin.com/in/ritu-sarswat-78a69b2b1/")
qrImg.save('demo.png')