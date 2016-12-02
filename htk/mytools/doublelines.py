import sys,os

d = str(sys.argv[1])

filename = str(sys.argv[2])

os.chdir(d);
fo = open(filename, 'r')
fo2 = open("double"+filename, 'w')
count = 1
while True:
	strs = fo.readline();
	if strs == '':
		break;
	if count < 10:
		outstr1 = "S000"+str(count)+"_1 "+strs;
		outstr2 = "S000"+str(count)+"_2 "+strs;
	elif count < 100:
		outstr1 = "S00"+str(count)+"_1 "+strs;
		outstr2 = "S00"+str(count)+"_2 "+strs;
	elif count < 1000:
		outstr1 = "S0"+str(count)+"_1 "+strs;
		outstr2 = "S0"+str(count)+"_2 "+strs;
	elif count < 10000:
		outstr1 = "S"+str(count)+"_1 "+strs;
		outstr2 = "S"+str(count)+"_2 "+strs;
	fo2.write(outstr1)
	fo2.write(outstr2)
	count = count +1

fo.close()
fo2.close()