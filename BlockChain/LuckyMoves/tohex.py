import sys

def strToHex(s):
    print(s.encode('utf-8').hex())

def intToHex(i):
    print(int(i,16))

if __name__=="__main__":
    if(sys.argv[1]=="1"):
        print("AA1")
        strToHex(sys.argv[2])
    else:
        intToHex(sys.argv[1])
