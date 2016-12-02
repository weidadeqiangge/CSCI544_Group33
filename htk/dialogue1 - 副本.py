from tkinter import *
import datetime
import time
root = Tk()
root.title('Flight Booking')

def leftClick():
	msgcontent = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
	infos = [-1 for _ in range(5)]
	dict1 = {'OriginCity':0,'DestinationCity':1,'DepartureTimeMonth':2, 'DepartureTimeDate':3, 'DepartureTimeYear':4}
	dict2 = {0:'departure city', 1:'destination city', 2: 'departure month', 3: 'departure date'}

	ques = []
	#call understanding function
	understand = [("=", "OriginCity", 'la'),("=", "DestinationCity", 'ny'),
				("=", "DepartureTimeYear", 2017)]
	for phrase in understand:
		if len(phrase) == 3:
			infos[dict1[phrase[1]]] = phrase[2]
	
	for i,info in enumerate(infos):
		#not departure year missing
		if info == -1 and i != 4:
			ques.append(dict2[i])
		#departure year missing
		if info == -1 and i == 4:
			infos[i] = 2016
	#there is missing information
	if ques:
		question = "Please tell us your ";
		if len(ques) == 1:
			question += ques[0]
		elif len(ques) == 2:
			question += (ques[0] + ' and '+ques[1])
		else:
			for i in range(len(ques)-2):
				question += (ques[i] + ', ' )
			question += (ques[len(ques)-1]+" and "+ ques[len(ques)-1])
		#print(question)
		text_msglist.insert(END, msgcontent, 'green')
		text_msg.insert(END, question, 'green')
		text_msglist.insert(END, text_msg.get('0.0', END))
		text_msg.delete('0.0', END)
	else:
		text_msglist.insert(END, msgcontent, 'green')
		text_msglist.insert(END, text_msg.get('0.0', END))
		text_msg.delete('0.0', END)
		
		
frame_left_top   = Frame(width=500, height=270, bg='green')
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

root.mainloop()