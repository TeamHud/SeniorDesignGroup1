#open packets
with open('packet1.txt', 'w') as file:
    file.write(input('Packet 1 text:'))
with open('packet1.txt', 'r') as file:
    data1 = file.read()

with open('packet2.txt', 'w') as file:
    file.write(input('Packet 2 text:'))
with open('packet2.txt', 'r') as file:
    data2 = file.read()

combined=data1+data2
file = open('combinedpacket.txt','w')
file.write(combined)
file.close()