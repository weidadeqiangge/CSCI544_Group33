from tkinter import *
import datetime
import time
import understand
import record
import os
confirm = False
confirmPhase = False
info = {}
cnt = 1

root = Tk()
root.title('Flight Booking')

def showInfo(text_msg):
	text_msg.insert(END, "Here are your information:\n", 'green')
	text_msg.insert(END, "\tName:" + info['MyName'] +"\n", 'green')
	text_msg.insert(END, "\tOrigin City:" + info['OriginCity']+"\n", 'green')
	text_msg.insert(END, "\tDestination City:" + info['DestinationCity']+"\n", 'green')
	text_msg.insert(END, "\tClass:" + info['Class']+"\n", 'green')
	if info['RoundTrip']=='True':
		text_msg.insert(END, "\tType: RoundTrip\n", 'green')
	else:
		text_msg.insert(END, "\tType: One-way\n", 'green')
	text_msg.insert(END, "\tDeparture Month:" + str(info['OutDepartureTimeMonth'])+"\n", 'green')
	text_msg.insert(END, "\tDeparture Date:" + str(info['OutDepartureTimeDate'])+"\n", 'green')
	text_msg.insert(END, "\tDeparture Year:" + str(info['OutDepartureTimeYear'])+"\n", 'green')
	if info['RoundTrip']=='True':
		text_msg.insert(END, "\tReturn Month:" + str(info['RetDepartureTimeMonth'])+"\n", 'green')
		text_msg.insert(END, "\tReturn Date:" + str(info['RetDepartureTimeDate'])+"\n", 'green')
		text_msg.insert(END, "\tReturn Year:" + str(info['RetDepartureTimeYear'])+"\n", 'green')

question = "Please tell us your departure city and destination."
def leftClick():	
	global cnt
	global confirm
	global confirmPhase
	global info
	global question
	msgcontent = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '	
	#call myunderstand function	
	#understands = ...
	mystring = record.record()
	understands = understand.understand(mystring)
	print(understands)
	if confirmPhase:
		#[("True",)] or [("=", "DestinationCity", "Chengdu")] 
		if len(understands) == 1:
			myunderstand = understands[0]
			print(myunderstand)
			if len(myunderstand) == 1:
				if myunderstand[0] == 'True':
					confirm = True
				elif myunderstand[0] == 'False':
					question = "What modifications do you want to make?"
					#understands = [("=", "MyName", "Xie He2")]
			else:
				info[myunderstand[1]] = myunderstand[2]
				showInfo(text_msg)
				question = " Do you confirm?"
		
		#[("False",),("=", "MyName", "Xie He")]
		else:
			for myunderstand in understands:
				if len(myunderstand) != 1:
					info[myunderstand[1]] = myunderstand[2]
			showInfo(text_msg)
			question = " Do you confirm?"
	else:
		#[("=", "OriginCity", "Los Angeles"),("=", "DestinationCity", "Chengdu")/////]
		#maybe ("=", "OutDepartureTimeMonth", "11")("=", "OutDepartureTimeDate", "15")("=", "OutDepartureTimeYear", "2017")
		if cnt == 1:
			for myunderstand in understands:
				info[myunderstand[1]] = myunderstand[2]
			if 'OutDepartureTimeMonth' in info and 'OutDepartureTimeYear' not in info:
				info['OutDepartureTimeYear'] = '2017'
			if 'OriginCity' in info and 'DestinationCity' in info:
				question = "What's your name"
				cnt += 1
				#understands = [("=", "OriginCity", "Los Angeles"),("=", "DestinationCity", "Chengdu")]
		elif cnt == 2:
			#[("=", "MyName", "Xie He")]
			for myunderstand in understands:
				info[myunderstand[1]] = myunderstand[2]
			if 'MyName' in info:
				question = 'Please tell us your ticket type, roundtrip or one-way?'
				cnt += 1
				#understands = [("=", "RoundTrip", "True")]
		elif cnt == 3:
			#[("=", "RoundTrip", "True")]
			for myunderstand in understands:
				info[myunderstand[1]] = myunderstand[2]
			if 'RoundTrip' in info:
				if 'OutDepartureTimeMonth' not in info:
					question = 'Please tell us your departure date.'
					cnt += 1
					#understands = [("=", "DepartureTimeMonth", "11"),("=", "DepartureTimeDate", "12")]
				else:
					if info['RoundTrip'] == 'True':
						
						question = 'Please tell us your return date'
						cnt+=2
					else:
						question = 'Please tell us your ticket class'
						cnt+=3
					#understands = [("=", "DepartureTimeMonth", "13"),("=", "DepartureTimeDate", "14")]
		elif cnt == 4:
			#[("=", "OutDepartureTimeMonth", "11")] or [("=", "DepartureTimeMonth", "11")]
			for myunderstand in understands:
				if myunderstand[1] == 'DepartureTimeMonth':
					info['OutDepartureTimeMonth'] = myunderstand[2]
				if myunderstand[1] == 'DepartureTimeDate':
					info['OutDepartureTimeDate'] = myunderstand[2]
				if myunderstand[1] == 'DepartureTimeYear':
					info['OutDepartureTimeYear'] = myunderstand[2]
			if 'OutDepartureTimeMonth' in info and 'OutDepartureTimeYear' not in info:
				info['OutDepartureTimeYear'] = '2017'
			if 'OutDepartureTimeYear' in info and 'OutDepartureTimeDate' in info and 'OutDepartureTimeMonth' in info:
				print(info['RoundTrip'])
				if info['RoundTrip']=='True':
					question = 'Please tell us your return date'
					cnt+=1
				else:
					question = 'Please tell us your ticket class'
					cnt+=2
			#	question = 'Please tell us your return date.'
			#	cnt += 1
				#understands = [("=", "DepartureTimeMonth", "13"),("=", "DepartureTimeDate", "14")]
		elif cnt == 5:
			#[("=", "RetDepartureTimeMonth", "11")] or [("=", "DepartureTimeMonth", "11")]
			for myunderstand in understands:
				if myunderstand[1] == 'DepartureTimeMonth':
					info['RetDepartureTimeMonth'] = myunderstand[2]
				if myunderstand[1] == 'DepartureTimeDate':
					info['RetDepartureTimeDate'] = myunderstand[2]
				if myunderstand[1] == 'DepartureTimeYear':
					info['RetDepartureTimeYear'] = myunderstand[2]
			if 'RetDepartureTimeMonth' in info and 'RetDepartureTimeYear' not in info:
				info['RetDepartureTimeYear'] = '2017'
			if 'RetDepartureTimeYear' in info and 'RetDepartureTimeDate' in info and 'RetDepartureTimeMonth' in info:
				question = 'Please tell us your ticket class.'
				cnt += 1
				#understands = [("=", "Class", "Economy")]
		elif cnt == 6:
			#[("=", "Class", "Economy")]
			for myunderstand in understands:
				info[myunderstand[1]] = myunderstand[2]
			showInfo(text_msg)
			question = ' Do you confirm?'
			confirmPhase = True
			#understands = [("False",)]
			
	if not confirm:
		text_msglist.insert(END, msgcontent, 'green')
		text_msg.insert(END, question, 'green')
		text_msglist.insert(END, text_msg.get('0.0', END))
		text_msg.delete('0.0', END)
		os.system('speechtask1 '+question)
	else:
		text_msglist.insert(END, msgcontent, 'green')
		showInfo(text_msg)
		text_msg.insert(END, " Thank you for using our system!", 'green')
		text_msglist.insert(END, text_msg.get('0.0', END))
		os.system("speechtask1 Thank you for using our system")
		text_msg.delete('0.0', END)
	
				
frame_left_top   = Frame(width=500, height=310, bg='green')
frame_left_center  = Frame(width=500, height=0, bg='red')
frame_left_bottom  = Frame(width=500, height=30)

text_msglist    = Text(frame_left_top)
text_msg      = Text(frame_left_center);
button_sendmsg   = Button(frame_left_bottom, text='Ready', command=leftClick)

text_msglist.tag_config('green', foreground='#008B00')

frame_left_top.grid(row=0, column=0, padx=2, pady=5)
frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=2, column=0)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)

text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)

text_msg.insert(END, " Welcome to our system!\n", 'green')

text_msg.insert(END, " How can I help you.", 'green')
text_msglist.insert(END, text_msg.get('0.0', END))
text_msg.delete('0.0', END)
#os.system('speechtask1 Welcome to our system!')
#os.system('speechtask1 How can I help you')

root.mainloop()
