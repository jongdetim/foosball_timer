from tkinter import *
import threading
import training_timer as t

ICON_FILE = "football_icon.ico"
ICON_PATH = sys.argv[0].rsplit('\\', 1)[0] + "\\" + ICON_FILE

default_button = 8
button_size_train = -6
defaultfont = 'TkDefaultFont 10'
bigfont = 'TkDefaultFont 11 bold'

training_selection = 3
pauseswitch = 0
startswitch = 0

def	get_series_shots(series):
	if series == "snake":
		return ["pull", "push", "middle", "near split", "far split", "near cross", "far cross"]
	if series == "pull":
		return ["long", "middle", "short", "two", "four", "brush", "john wayne"]
	if series == "stick" or series == "brush":
		return ["lane", "wall", "second man", "bounce lane", "bounce wall", "left hook"]
	if series == "pull shot":
		return ["slice", "short square", "mid square", "spray mid", "long"]
	if series == "pin shot":
		return ["short", "middle", "long", "far bank", "near bank"]
	if series == "passing":
		return ["far wall", "lane", "high wall", "near wall", "stick wall", "left hook"]
	

def	handle_pauseplay(_=None):
	if startswitch:
		global pauseswitch
		if pauseswitch == 0:
			pauseplayB.config(relief=SUNKEN, text="⏯Play")
		if pauseswitch == 1:
			pauseplayB.config(relief=RAISED, text="⏯Pause")
		pauseswitch = 1 - pauseswitch

def	handle_startstop(_=None):
	global startswitch
	if startswitch == 0:
		startswitch = 1 - startswitch
		startstopB.config(relief=SUNKEN, text="◼ Stop Training")
		probabilities = [prob.get() for prob in probs[:shot_amount.get()]]
		training_loopT = threading.Thread(target=t.training_loop, args=(training_selection, t.engine, shotcall_delay.get(), probabilities, shots[:shot_amount.get()], beepdelay.get(), series))
		training_loopT.daemon = True
		training_loopT.start()
	elif startswitch == 1:
		startstopB.config(relief=RAISED, text="▶ Start Training")
		if pauseswitch:
			handle_pauseplay()
		startswitch = 1 - startswitch

def	press_button(button):
	twobarB.config(relief=RAISED)
	threebarB.config(relief=RAISED)
	fivebarB.config(relief=RAISED)
	global training_selection
	training_selection = button
	if button == 2:
		twobarframe.tkraise()
		twobarB.config(relief=SUNKEN)
		shot_type_2b.set("pull shot")
		shot_amount.set(4)
		series_button("pull shot")
	if button == 3:
		threebarframe.tkraise()
		threebarB.config(relief=SUNKEN)
		shot_type_3b.set("snake")
		shot_amount.set(3)
		series_button("snake")
	if button == 5:
		fivebarframe.tkraise()
		fivebarB.config(relief=SUNKEN)
		shot_type_5b.set("brush")
		shot_amount.set(3)
		series_button("brush")

def	remove_probs():
	probslider1.place_forget()
	probslider2.place_forget()
	probslider3.place_forget()
	probslider4.place_forget()
	probslider5.place_forget()
	probslider6.place_forget()
	probslider7.place_forget()
	problabel1.place_forget()
	problabel2.place_forget()
	problabel3.place_forget()
	problabel4.place_forget()
	problabel5.place_forget()
	problabel6.place_forget()
	problabel7.place_forget()

def	handle_shotcount():
	global shots
	for i, shot in enumerate(shots[:shot_amount.get()]):
		shot.set(get_series_shots(series)[i])
	remove_probs()
	if shot_amount.get() >= 2:
		probslider1.place(x=260, y=0)
		probslider2.place(x=260, y=40)
		problabel1.place(x=70, y=15)
		problabel2.place(x=70, y=55)
	if shot_amount.get() >= 3:
		probslider3.place(x=260, y=80)
		problabel3.place(x=70, y=95)
	if shot_amount.get() >= 4:
		probslider4.place(x=260, y=120)
		problabel4.place(x=70, y=135)
	if shot_amount.get() >= 5:
		probslider5.place(x=260, y=160)
		problabel5.place(x=70, y=175)
	if shot_amount.get() >= 6:
		probslider6.place(x=260, y=200)
		problabel6.place(x=70, y=215)
	if shot_amount.get() >= 7:
		probslider7.place(x=260, y=240)
		problabel7.place(x=70, y=255)

def	series_button(shot_type):
	global series
	series = shot_type
	if shot_type == "snake" or shot_type == "pull":
		handle_shotcount()
	if shot_type == "stick":
		shot_amount.set(3)
		stick_radio_0.place_forget()
		stick_radio_1.place(x=210, y=30)
		stick_radio_2.place(x=270, y=30)
		stick_radio_3.place(x=330, y=30)
		handle_shotcount()
	if shot_type == "brush":
		shot_amount.set(2)
		stick_radio_1.place_forget()
		stick_radio_2.place_forget()
		stick_radio_3.place_forget()
		stick_radio_1.place(x=300, y=30)
		stick_radio_0.place(x=240, y=30)
		handle_shotcount()
	if shot_type == "pull shot":
		shot_amount.set(4)
		radio_3b_2.place_forget()
		radio_3b_3.place_forget()
		radio_3b_4.place(x=240, y=30)
		radio_3b_5.place(x=300, y=30)
		radio_3b_6.place_forget()
		handle_shotcount()
	if shot_type == "pin shot":
		shot_amount.set(3)
		radio_3b_2.place_forget()
		radio_3b_3.place(x=240, y=30)
		radio_3b_4.place_forget()
		radio_3b_5.place(x=300, y=30)
		radio_3b_6.place_forget()
		handle_shotcount()
	if shot_type == "passing":
		shot_amount.set(2)
		radio_3b_2.place(x=210, y=30)
		radio_3b_3.place_forget()
		radio_3b_4.place(x=270, y=30)
		radio_3b_5.place_forget()
		radio_3b_6.place(x=330, y=30)
		handle_shotcount()

mainwindow = Tk()

mainwindow.title("Foos Trainer")
mainwindow.iconbitmap(ICON_PATH)
# mainwindow.geometry('450x650')

probs = [IntVar() for _ in range(7)]
for prob in probs:
	prob.set(5)

shots = [StringVar() for _ in range(7)]


topframe = Frame(mainwindow, width=450, height=100)
topframe.grid(row=0, column=0)

timerframe = Frame(mainwindow)
timerframe.grid(row=6, column=0)

probframe = Frame(mainwindow, width=450, height=300)
probframe.grid(row=3, column=0)

twobarframe = Frame(mainwindow, width=450, height=70)
twobarframe.grid(row=2, column=0)
threebarframe = Frame(mainwindow, width=450, height=70)
threebarframe.grid(row=2, column=0)
fivebarframe = Frame(mainwindow, width=450, height=70)
fivebarframe.grid(row=2, column=0)

menuframe = Frame(mainwindow, width=450, height=50)
menuframe.grid(row=7, column=0)

mainwindow.bind("<KeyPress-space>", handle_pauseplay)
mainwindow.bind("<KeyPress-s>", handle_startstop)

# TOPFRAME
twobarB = Button(topframe, text="2-bar", fg="red", width=button_size_train, font=bigfont, command=lambda:press_button(2))
twobarB.grid(row=0, column=2, pady=15, padx=30, sticky='nsew')
threebarB = Button(topframe, text="3-bar", fg="blue", width=button_size_train, font=bigfont, command=lambda:press_button(3))
threebarB.grid(row=0, column=0, pady=15, padx=30, sticky='nsew')
threebarB.config(relief=SUNKEN)
fivebarB = Button(topframe, text="5-bar", fg="green", width=button_size_train, font=bigfont, command=lambda:press_button(5))
fivebarB.grid(row=0, column=1, pady=15, padx=30, sticky='nsew')

# TIMERFRAME
beepdelay = DoubleVar()
beepdelay.set(1.0)

Label(timerframe, text="Beep delay (seconds)", anchor="e", font=defaultfont, width=18).grid(row=1, column=0, sticky='se', padx=30)
beepdelayW = Scale(timerframe, from_=0, to=3.0, length=200, orient='horizontal', resolution=0.1, variable=beepdelay)
beepdelayW.grid(row=1, column=1, sticky='se')

shotcall_delay = DoubleVar()
shotcall_delay.set(12.0)

Label(timerframe, text="Shotcall delay (seconds)", anchor="e", font=defaultfont, width=18).grid(row=0, column=0, sticky='se', padx=30)
shotcall_delayW = Scale(timerframe, from_=0, to=20.0, length=200, orient='horizontal', resolution=0.1, variable=shotcall_delay)
shotcall_delayW.grid(row=0, column=1, sticky='se')

# MENUFRAME
startstopB = Button(menuframe, text="▶ Start Training", anchor="e", width=11, font=defaultfont, command=handle_startstop)
startstopB.grid(row=0, column=0, pady=8, padx=30, sticky='sw')
pauseplayB = Button(menuframe, text="⏯Pause", anchor="w", width=7, font=defaultfont, command=handle_pauseplay)
pauseplayB.grid(row=0, column=1, pady=8, padx=50, sticky='se')

# PROBABILITY FRAME
probslider1 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[0])
probslider2 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[1])
probslider3 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[2])
probslider4 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[3])
probslider5 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[4])
probslider6 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[5])
probslider7 = Scale(probframe, from_=0, to=10, length=120, orient='horizontal', resolution=1, variable=probs[6])

problabel1 = Label(probframe, textvar=shots[0], anchor="se", font=defaultfont, width=15)
problabel2 = Label(probframe, textvar=shots[1], anchor="se", font=defaultfont, width=15)
problabel3 = Label(probframe, textvar=shots[2], anchor="se", font=defaultfont, width=15)
problabel4 = Label(probframe, textvar=shots[3], anchor="se", font=defaultfont, width=15)
problabel5 = Label(probframe, textvar=shots[4], anchor="se", font=defaultfont, width=15)
problabel6 = Label(probframe, textvar=shots[5], anchor="se", font=defaultfont, width=15)
problabel7 = Label(probframe, textvar=shots[6], anchor="se", font=defaultfont, width=15)
problabel3.place(x=100, y=0)

# 3-BAR FRAME
shot_type_3b = StringVar()

Radiobutton(threebarframe, text='Snake Shot', variable=shot_type_3b, value="snake", command=lambda:series_button("snake")).place(x=120, y=0)
Radiobutton(threebarframe, text='Pull Shot', variable=shot_type_3b, value="pull", command=lambda:series_button("pull")).place(x=230, y=0)

shot_amount = IntVar()

Label(threebarframe, text="Amount of shots", anchor="e", font=defaultfont, width=0).place(x=80, y=30)
Radiobutton(threebarframe, text='3', variable=shot_amount, value=3, command=handle_shotcount).place(x=210, y=30)
Radiobutton(threebarframe, text='5', variable=shot_amount, value=5, command=handle_shotcount).place(x=270, y=30)
Radiobutton(threebarframe, text='7', variable=shot_amount, value=7, command=handle_shotcount).place(x=330, y=30)


# 5-BAR FRAME
shot_type_5b = StringVar()
shot_type_5b.set("brush")

Radiobutton(fivebarframe, text='Brush Series', variable=shot_type_5b, value="brush", command=lambda:series_button("brush")).place(x=120, y=0)
Radiobutton(fivebarframe, text='Stick Series', variable=shot_type_5b, value="stick", command=lambda:series_button("stick")).place(x=230, y=0)

Label(fivebarframe, text="Amount of shots", anchor="e", font=defaultfont, width=0).place(x=80, y=30)
stick_radio_1 = Radiobutton(fivebarframe, text='3', variable=shot_amount, value=3, command=handle_shotcount)
stick_radio_2 = Radiobutton(fivebarframe, text='5', variable=shot_amount, value=5, command=handle_shotcount)
stick_radio_3 = Radiobutton(fivebarframe, text='6', variable=shot_amount, value=6, command=handle_shotcount)
stick_radio_0 = Radiobutton(fivebarframe, text='2', variable=shot_amount, value=2, command=handle_shotcount)

# 2-BAR FRAME
shot_type_2b = StringVar()
shot_type_2b.set("pull shot")

Radiobutton(twobarframe, text='Pullshot', variable=shot_type_2b, value="pull shot", command=lambda:series_button("pull shot")).place(x=70, y=0)
Radiobutton(twobarframe, text='Pinshot', variable=shot_type_2b, value="pin shot", command=lambda:series_button("pin shot")).place(x=180, y=0)
Radiobutton(twobarframe, text='Passing', variable=shot_type_2b, value="passing", command=lambda:series_button("passing")).place(x=290, y=0)

Label(twobarframe, text="Amount of shots", anchor="e", font=defaultfont, width=0).place(x=80, y=30)
radio_3b_2 = Radiobutton(twobarframe, text='2', variable=shot_amount, value=2, command=handle_shotcount)
radio_3b_3 = Radiobutton(twobarframe, text='3', variable=shot_amount, value=3, command=handle_shotcount)
radio_3b_4 = Radiobutton(twobarframe, text='4', variable=shot_amount, value=4, command=handle_shotcount)
radio_3b_5 = Radiobutton(twobarframe, text='5', variable=shot_amount, value=5, command=handle_shotcount)
radio_3b_6 = Radiobutton(twobarframe, text='6', variable=shot_amount, value=6, command=handle_shotcount)


if __name__ == "__main__":
	press_button(3)
	mainwindow.mainloop()