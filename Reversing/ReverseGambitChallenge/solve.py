import os
import subprocess

i=0xffffffff
i=4291830000
while i>0:
    result=subprocess.run(["./challenge",hex(i)[2:]],stdout=subprocess.PIPE)
    if(i%10000==0):
        print(i,result.stdout)
    if(result.stdout!=b'Invalid key\n'):
        print(i)
        break
    i-=1
