from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
#import pycryptodome
flag=bytearray.fromhex("61772cb64825c3f4847eabb3781f684c8a15694a7103f6e26062b639b674b69539f67fe9bb738af3f39ec97177015962")
iv=bytearray.fromhex("bb495ec0f46f4a0ab3bd67dc8b528071")
key=bytearray.fromhex("77898908c29d85e5bfc792c01d27a774d3fa42ceea244f6f365d5827f68f2c36")
# mode="AES_CBC"
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
flag = unpad(cipher.decrypt(flag),AES.block_size)
print(flag)
