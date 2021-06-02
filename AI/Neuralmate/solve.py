from pwn import *
import base64
import binascii
r = remote("192.168.125.11",4000)

print(r.recv())

with open("boards/board1.png","rb") as f:
    img = f.read()
    send=((base64.b64encode(img)))
    r.send(send)
print("OK")
print(r.recv())
print(r.recv())
