
from hashlib import sha256
from Crypto.Cipher import AES
from binascii import *

K = [(211617787759859142239706472988961288862%218925954923455975113808255640357734801), (7999980347242228732270030561580298923%218925954923455975113808255640357734801)]

key = (K[0].to_bytes(16,'big'))
ciphertext = unhexlify('243016cba63adb30c029581cb68a29e851b5a8607cf89ff966d9c859f42132b745aa637c0b9555adc7c4df3e2d19e3b7e9b6a2217cb448e14d7f8e3a3e6c08ac')
key = sha256(key).digest()
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(ciphertext)

print(flag)
#CCSC{s1ngul4r_curv3s_4r3_n0t_re4lly_3ll1pt1c_curv3s!!}'

