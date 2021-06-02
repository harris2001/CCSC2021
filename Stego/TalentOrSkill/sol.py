with open("Beth_Harmon.dna") as f:
    dna=f.read()

flag=""
for c in dna:
    if c=="A":
        flag+="00"
    elif c=="C":
        flag+="01"
    elif c=="G":
        flag+="10"
    elif c=="T":
        flag+="11"
print(flag)
