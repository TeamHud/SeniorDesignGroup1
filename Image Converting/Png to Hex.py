import binascii
filename = '480x480.png'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content).decode())
f = open('text.txt', 'w')
f.write(binascii.hexlify(content).decode())
f.close()
