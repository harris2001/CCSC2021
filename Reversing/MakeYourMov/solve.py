enc_str=[0x014,0x088,0x058,0x144,0x090,0x09c,0x14c,0x0c8,0x0b8,0x084,0x0ba,0x070,0x0a6,0x024,0x064,0x04a,0x04e,0x05a,0x070,0x01a,0x010,0x056,0x01b,0x035,0x021,0x03e,0x009,0x03d,0x021,0x026]

key =[0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74,0x67,0x61,0x6d,0x62,0x69,0x74]

_enc_str=[0x014,0x088,0x058,0x144,0x090,0x09c,0x14c,0x0c8,0x0b8,0x084,0x0ba,0x070,0x0a6,0x024,0x064,0x04a,0x04e,0x05a,0x070,0x01a,0x010,0x056,0x01b,0x035,0x021,0x03e,0x009,0x03d,0x021,0x026]


Z = 0
One = 1
M = -1
counter = 30
c = 30
t = 0 
b = 2
b1 = 1
b_t = 0
sh_t = 0
x = 10

def main():

	t=enc_str[20]
	enc_str[20]=enc_str[29]
	enc_str[29]=t
	t=enc_str[26]
	enc_str[26]=enc_str[25]
	enc_str[25]=t
	t=enc_str[28]
	enc_str[28]=enc_str[24]
	enc_str[24]=enc_str[22]
	enc_str[22]=t
	t=enc_str[27]
	enc_str[27]=enc_str[23]
	enc_str[23]=enc_str[21]
	enc_str[21]=t


	t=enc_str[10]     
	enc_str[10]=enc_str[19] 
	enc_str[19]=t
	t=enc_str[16]      
	enc_str[16]=enc_str[15] 
	enc_str[15]=t
	t=enc_str[18] 
	enc_str[18]=enc_str[14] 
	enc_str[14]=enc_str[12] 
	enc_str[12]=t
	t=enc_str[17] 
	enc_str[17]=enc_str[13] 
	enc_str[13]=enc_str[11] 
	enc_str[11]=t

	t=enc_str[0]    
	enc_str[0]=enc_str[9] 
	enc_str[9]=t
	t=enc_str[6]      
	enc_str[6]=enc_str[5] 
	enc_str[5]=t
	t=enc_str[8]
	enc_str[8]=enc_str[4]
	enc_str[4]=enc_str[2]
	enc_str[2]=t
	t=enc_str[7]
	enc_str[7]=enc_str[3]
	enc_str[3]=enc_str[1]
	enc_str[1]=t

	flag=[]
	for i in range(30):
		flag.append(hex(_enc_str[i]^key[i]))
		print(chr(_enc_str[i]^key[i]))
	'''
	print(hex(_enc_str[0]),(hex(enc_str[9])))########
	print(hex(_enc_str[1]),(hex(enc_str[3])))########
	print(hex(_enc_str[2]),(hex(enc_str[4])))########
	print(hex(_enc_str[3]),(hex(enc_str[7])))########
	print(hex(_enc_str[4]),(hex(enc_str[8])))########
	print(hex(_enc_str[5]),(hex(enc_str[6])))########
	print(hex(_enc_str[6]),(hex(enc_str[5])))########
	print(hex(_enc_str[7]),(hex(enc_str[1])))########
	print(hex(_enc_str[8]),(hex(enc_str[2])))########
	print(hex(_enc_str[9]),(hex(enc_str[0])))########
	print(hex(_enc_str[10]),(hex(enc_str[19])))#######
	print(hex(_enc_str[11]),(hex(enc_str[13])))#######
	print(hex(_enc_str[12]),(hex(enc_str[14])))#######
	print(hex(_enc_str[13]),(hex(enc_str[17])))#######
	print(hex(_enc_str[14]),(hex(enc_str[18])))#######
	print(hex(_enc_str[15]),(hex(enc_str[16])))#######
	print(hex(_enc_str[16]),(hex(enc_str[15])))#######
	print(hex(_enc_str[17]),(hex(enc_str[11])))#######
	print(hex(_enc_str[18]),(hex(enc_str[12])))#######
	print(hex(_enc_str[19]),(hex(enc_str[10])))#######
	print(hex(_enc_str[20]),(hex(enc_str[29])))#######
	print(hex(_enc_str[21]),(hex(enc_str[23])))#######
	print(hex(_enc_str[22]),(hex(enc_str[24])))#######
	print(hex(_enc_str[23]),(hex(enc_str[27])))#######
	print(hex(_enc_str[24]),(hex(enc_str[28])))#######
	print(hex(_enc_str[25]),(hex(enc_str[26])))#######
	print(hex(_enc_str[26]),(hex(enc_str[25])))#######
	print(hex(_enc_str[27]),(hex(enc_str[21])))#######
	print(hex(_enc_str[28]),(hex(enc_str[22])))#######
	print(hex(_enc_str[29]),(hex(enc_str[20])))#######
	'''
	print(flag)


def _func():
    flag=[]
    for i in range(30):
        flag.append(hex(_enc_str[i]^key[i]))
    print(flag)

def f_end():
    counter=11

def func2():
    if(counter==0):
        cont
    b_t=b
    sh_t=0
    t=0

# out = [0x19c,0x184,0x1b4,0x28,0x188,0x1a4,0x1d0,0x19c,0x2c,0x184,0x1b4,0x188,0xd2,0x30,0xe8,0xce,0xc2,0xda,0x34,0xc4,0xd2,0xe8,0xce,0x38,0xc2,0x6d,0x62,0x69,0x3c,0x74,0x67,0x61,0x6d,0x40,0x62,0x69,0x74]

# for i in out:
#     #if(i%2==0):
#     #    print(chr(int(i/2)))
#     #else:
#     print(chr(i))

if __name__=="__main__":
   main()
