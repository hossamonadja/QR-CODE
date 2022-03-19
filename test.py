import qrcode

img = qrcode.make("https://www.linkedin.com/in/hossam-onadja-3323a1220/")
img.save("test.png")