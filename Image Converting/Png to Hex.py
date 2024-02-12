import binascii
from PIL import Image
from random import randint
print(randint(0,3))
image='image'+str(randint(0,3))+'.png'
filename = image

with open(filename, 'rb') as f:
    content = f.read()
    im = Image.open(filename)
    im.show(filename)
print(binascii.hexlify(content).decode())
f = open('text.txt', 'w')
f.write(binascii.hexlify(content).decode())
f.close()
