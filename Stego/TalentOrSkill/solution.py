dict=['A','C','G','T']

poss=['A','C','G','T']

i = 2**3-1

for i in poss:
    if len(i)<3 :
        for d in dict:
            poss.append(i+d)
dict = []
corr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ."
cc=0
for i in poss:
    if len(i)==3:
        dict.append(i)
        #print(i,corr[cc])
        cc+=1
dna = ""
with open("Beth_Harmon.dna") as f:
    dna = f.read()
    f.close()

flag = ""
for i in range(0,len(dna),3):
    if(i+2>=len(dna)):
        break
    s = dna[i]+dna[i+1]+dna[i+2]
    #print(s)
    for j in range(len(dict)):
        if(s==dict[j]):
            #print(s+"="+corr[j])
            flag+=corr[j]
            break
print(flag)
