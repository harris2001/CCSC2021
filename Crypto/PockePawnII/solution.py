import binascii
import base64
a="1-596c042805f58c6106a7a82db9912e430e9606ce444012cdd8a8f52aac90e332ca6c601a61"
b="2-0xd6e485ab4d003895d4138077afd0dd50b4279ce7978cbe1be1670de47d1206603f8b8b1bb8"
c="3-0xd341b5f99464863a27ea0a0102ce357d72c965d39a7110aa310c8b9f18ddeec43fd61e051a"

result="90b908ed5587d8ad5351ee2fe0325963ff04ce6fc88cb3309afcf1622fb0e22484615334c4"

#Ripped Paper:
r1="1bCO>11;nJARo700JYI@3&G5W@PTYr3&WR)2E3L(2)R<K1c-"
r2="sA2dnCO3ArU$0K3H$An*MK0k3.Q2e\"UQAN+$Q@lH(uA7T:\\"

d="4-422a1dedb8024384fcb216863f683e557344207a0e961b07b9fc001c7d7b4be7a2c704ddfa"
hexx=""
hexx2=""
for i in r1:
    hexx+=hex(ord(i))[2:]
for i in r2:
    hexx2+=hex(ord(i))[2:]
print(hexx)
print(hexx2)
