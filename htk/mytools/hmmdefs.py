# hmmdefs.py D:\Learing_USC\CSCI_544\Project\htk\hmms\hmm0 D:\Learing_USC\CSCI_544\Project\htk\list\monophones0

import os, sys

d_proto = str(sys.argv[1]);
d_phonelist = str(sys.argv[2]);

fo1 = open(d_proto+"\\proto",'r');
fo2 = open(d_phonelist,'r');
fo3 = open(d_proto+'\\vFloors','r')

fo1.readline();
fo1.readline();
fo1.readline();
fo1.readline();
proto = fo1.read();
os.chdir(d_proto)
fout = open('hmmdefs','w')
fout2 = open('macros', 'w')
phones = fo2.read();
phones_split = phones.split()
fout2.write("~o\n<VECSIZE> 39<MFCC_0_D_A>\n");
fout2.write(fo3.read());
fout2.close();
fo3.close();
for ph in phones_split:
	outstr = "~h " +"\"" +ph+"\"" + '\n'
	fout.write(outstr);
	fout.write(proto);

fo1.close();
fo2.close();
fout.close();