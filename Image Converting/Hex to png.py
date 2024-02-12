#make sure to install pillow
from PIL import Image
#open a txt file in hex and convert it to png
with open('text.txt') as file:
    data = file.read()
data = bytes.fromhex(data)
#this is actually the part that converts it to png, the first part just opens the text and reads it
with open('image.png', 'wb') as file:
    file.write(data)
    im= Image.open("image.png")
    im.show('image.png')