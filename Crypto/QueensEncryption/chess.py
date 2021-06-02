
dic =[
['6e','46'],['4c','0e'],['71','1d'],['7b','24'],['33','74'],['48','76'],['5a','07'],['64','0d'],
['68','08'],['47','7e'],['3c','50'],['2a','43'],['0c','22'],['00','63'],['16','28'],['20','2e'],
['61','66'],['6d','6f'],['0b','69'],['2b','4e'],['35','27'],['4a','2f'],['39','1e'],['4d','3a'],
['31','4f'],['49','36'],['5c','38'],['65','45'],['18','72'],['62','3e'],['77','7d'],['5d','60'],
['34','41'],['11','25'],['6c','42'],['44','01'],['1b','23'],['30','6b'],['02','0f'],['32','4b'],
['05','57'],['53','52'],['19','3f'],['2c','04'],['70','03'],['1f','7f'],['79','21'],['3d','40'],
['67','5b'],['51','3b'],['6a','29'],['7a','5f'],['26','1c'],['54','58'],['17','55'],['59','5e'],
['09','2d'],['14','13'],['10','12'],['15','73'],['37','75'],['06','7c'],['78','1a'],['56','0a'], 
]
ct="rnbk1bnr/p1pQpppp/1p1p4/8/3P4/2P5/PP2PPPP/RNB1KBNR~\
5k2/3Q2p1/p4n1r/1p3p2/1P4P1/1R2P3/P2KP1BP/2B4R~\
8/4k2r/p5p1/7n/1P2P1P1/1Q1R4/P3P1BP/2B1K2R~\
6k1/3Q4/8/p2n2p1/1P4P1/3RP2B/PB2P2R/3K4~\
3Q2k1/8/8/p3n1p1/1P4P1/2KR3B/PB2P2R/8~\
Q7/6k1/8/p3n3/1P4P1/2KR3B/PB2P2R/8~\
8/4kr1p/8/Q1P3P1/pp1r2p1/3B4/PP1K3P/3R1R2~\
r1bq2nr/pppkbppp/2n5/8/3P4/1Q6/PPP2PPP/RNB1KBNR~\
3q3r/5kbp/2b4n/p1rpp1p1/2P1PpPQ/PP1pnP1N/6BP/R1B1KN1R~\
3qr3/1p1bk1bp/r2p3n/p1p3p1/1nNPPp2/P1P2P1N/1P1Q2BP/R1B1K2R~\
3q3r/5kbp/1r2b2n/p1P3p1/P2pPBn1/1P1p1P1N/5QBP/2R1KN1R~\
2b2Q1r/7p/1R3n1b/3pkp2/2p3p1/r7/P1P2PPP/2B1KBR1~\
4k3/5r1p/8/ppPQ2P1/3r2p1/3B4/PP1K3P/3R1R2~\
5k1r/4n2p/8/8/8/8/P2Q3P/RNBK1BNR~\
4n1nB/p2rbk1p/8/8/7Q/8/PPKNR1PP/5BNR~\
r4b1r/ppnbnkpp/8/1Q6/8/8/PP4PP/RNB1KBNR~\
r3kbnr/p5pp/3Qb3/2p5/4p3/2P5/P5PP/R1B1KBNR~\
r1bqkbnr/pQ4pp/2n5/5pP1/8/2NPp3/PPP2P1P/R3KBNR~\
rnbqkbnr/pp4pp/2p5/3pppQ1/5P2/2PPP3/PP4PP/RNB1KBNR~"
#'''
dec = []
decoded=""
for i in ct:
    if i=="/":
        continue
    if i=="~":
        dec.append(decoded)
        #print(decoded)
        decoded=""
        continue
    if ord(i)<=ord("9") and ord(i)>=ord("0"):
        times=(ord(i)-ord("0"))
        decoded+="0"*times
    elif ord(i)<=ord("Z") and ord(i)>=ord("A"):
        decoded+="1"
    else:
        decoded+="2"

count=0
flag=""
for game in dec:
	count=0
	cc=""
	for i in range(len(game)):
	    if(i%8==0):
	        print(cc)
	        cc=""
	    cc+=game[i]+" "
	print(cc)
	print("____________________________________")
	for pawn in game:
		if pawn=="1":
			flag+=dic[count][1]
		elif pawn=="2":
			flag+=dic[count][0]
		count+=1
print(flag)
