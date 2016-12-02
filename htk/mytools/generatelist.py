#sample input generatelist.py train D:\Learing_USC\CSCI_544\Project\htk\data\train
import os, sys
import string

type = str(sys.argv[1]);

code_filename = '';
train_filename = '';

if type == 'train' :
	filename = 'codetr.scp';
	train_filename = 'train.scp';

if type == 'test' :
	filename = 'codete.scp';
	train_filename = 'test.scp';
	
cwd = os.getcwd()
os.chdir("..")	
d_root = str(sys.argv[2]);
d_datadirs = '';
d_featuredir = '';
fo1 = open(filename, "w")
fo2 = open(train_filename, "w")

for root, dirs, files in os.walk(d_root):
	for file in files:
		d_datadirs = str(d_root)+"\\sound\\"+str(file)
		if '.wav' in str(file):
			d_featuredirtmp =str(d_root)+"\\feature\\"+str(file)
			d_featuredir=d_featuredirtmp.replace('.wav', '.mfc')
		else:
			d_featuredir =str(d_root)+"\\feature\\"+str(file) + ".mfc"
		fo1.write(d_datadirs + '\t'+'\t'+d_featuredir+"\n")
		fo2.write(d_featuredir+"\n")

fo1.close();
fo2.close();		
		

