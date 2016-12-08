def transform():
	file1 = open('testtranscript.txt', 'r')
	file2 = open('testdata.txt', 'w')
	
	while(1):
		line = file1.readline().strip()
		if(not line): 
			break
		file2.write('<s> ' + str(line) + ' </s>\n')
	file1.close()
	file2.close()

transform()