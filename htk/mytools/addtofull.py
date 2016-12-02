#addtofull D:\Learing_USC\CSCI_544\Project\htk\list\fulllist D:\Learing_USC\CSCI_544\Project\htk\list\triphones1
import sys, os

f1 = str(sys.argv[1])
f2 = str(sys.argv[2])

fo1 = open(f1,'r+')
fo2 = open(f2,'r')

tricontent = fo1.read();
trilist = tricontent.split();
lista = []
while True:
	strx = fo2.readline();
	strc = strx.split();
	if strx =='':
		break;
	if not (strc[0] in trilist):
		fo1.write(strx)

fo1.close();
fo2.close();
#fo1 = open(f1,'w')
#for strc in trilist:
#	fo1.write(strc)

#fo1.close()
