import base64
base1=""
base2=""
txt=""
data=""
with open("encoded-message.txt") as f:
	data = f.read()
base1 = data.split("===\n")[0]
base2 = data.split("===\n")[1]
print(base1+"===")
#print(base2)
#ans1=""
#ans2=""
#for i in range(len(base1)):
#    if(base1[i]==base2[i]):
#        ans1+=base1[i]
#        ans2+=base2[i]
        
#print(ans1)
#print(ans2)
