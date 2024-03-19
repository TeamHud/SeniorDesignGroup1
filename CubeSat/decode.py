
with open('text.txt') as file:
	data=file.read()
data=bytes.fromhex(data)
with open('image.jpg','wb') as file:
	file.write(data)

