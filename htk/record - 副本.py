
import pyaudio
import wave
import sys
import os

def record():
	CHUNK = 1024


	wf = wave.open("record.wav", 'wb')
	wf.setnchannels(1)  
	wf.setsampwidth(2)  
	wf.setframerate(44100)

	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# open stream (2)
	stream = p.open(rate = 44100,format=pyaudio.paInt16,channels=1,input=True)

	# read data
	data = stream.read(CHUNK)

	# play stream (3)
	#while len(data) > 0:
		#stream.write(data)
	count = 0  
	while count < 10*30:  
		wf.writeframes(data)
		data = stream.read(CHUNK)
		print ('.')  
		count+=1

	stream.stop_stream()
	stream.close()
	wf.close()
	path=os.getcwd()
	os.system('HCopy -T 1 -C '+path+'\\config\\config3 record.wav record.mfc')
	os.system('HVite -H '+path+'\\hmms\\hmm15\\macros -H '+path+'\\hmms\\hmm15\\hmmdefs -w wdnet -p 0.0 -s 5.0 '+path+'\\dict\\mydict6 '+path+'\\list\\tiedlist record.mfc')

	fo = open("record.rec", 'r')
	result = ''
	confidence = []
	tmpstr = fo.readline();
	while tmpstr != '':
		tmplist = tmpstr.split()
		result=result+str(tmplist[2])+' '
		confidence.append(eval(tmplist[3]))
		tmpstr = fo.readline()
	os.system('speechtask1 '+result.lower())
	print(result)
	print(confidence)

	wf = wave.open("record.wav", 'rb')
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)

	# read data
	data = wf.readframes(CHUNK)

	# play stream (3)
	while len(data) > 0:
		stream.write(data)
		data = wf.readframes(CHUNK)	
	# stop stream (4)
	stream.stop_stream()
	stream.close()

	# close PyAudio (5)
	p.terminate()
	return result;