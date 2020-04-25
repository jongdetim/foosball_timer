from tkinter import *


default_button = 10
button_size_train = -6
defaultfont = 'TkDefaultFont 10'
bigfont = 'TkDefaultFont 11 bold'

training_selection = 3

def	press_button(button):
	twobarB.config(relief=RAISED)
	threebarB.config(relief=RAISED)
	fivebarB.config(relief=RAISED)
	global training_selection
	training_selection = button
	if button == 2:
		twobarframe.tkraise()
		twobarB.config(relief=SUNKEN)
	if button == 3:
		threebarframe.tkraise()
		threebarB.config(relief=SUNKEN)
	if button ==5:
		fivebarframe.tkraise()
		fivebarB.config(relief=SUNKEN)

mainwindow = Tk()

mainwindow.title("Foos Timer")
# mainwindow.geometry('700x350')
# mainwindow.rowconfigure(0, weight=1)
# mainwindow.columnconfigure(0, weight=1)

topframe = Frame(mainwindow)
topframe.grid(row=0, column=0)

timerframe = Frame(mainwindow)
timerframe.grid(row=1, column=0)

twobarframe = Frame(mainwindow)
twobarframe.grid(row=2, column=0)
threebarframe = Frame(mainwindow)
threebarframe.grid(row=2, column=0)
fivebarframe = Frame(mainwindow)
fivebarframe.grid(row=2, column=0)

# TOPFRAME
twobarB = Button(topframe, text="2-bar", fg="red", width=button_size_train, font=bigfont, command=lambda:press_button(2))
twobarB.grid(row=0, column=0, pady=15, padx=30, sticky='nsew')
threebarB = Button(topframe, text="3-bar", fg="blue", width=button_size_train, font=bigfont, command=lambda:press_button(3))
threebarB.grid(row=0, column=1, pady=15, padx=30, sticky='nsew')
threebarB.config(relief=SUNKEN)
fivebarB = Button(topframe, text="5-bar", fg="green", width=button_size_train, font=bigfont, command=lambda:press_button(5))
fivebarB.grid(row=0, column=2, pady=15, padx=30, sticky='nsew')

# TIMERFRAME
beepdelay = DoubleVar()
beepdelay.set(1.0)

Label(timerframe, text="Beep delay (seconds)", anchor="e", font=defaultfont, width=18).grid(row=0, column=0, sticky='se', padx=30)
beepdelayW = Scale(timerframe, from_=0, to=3.0, length=200, orient='horizontal', resolution=0.1, variable=beepdelay)
beepdelayW.grid(row=0, column=1, sticky='se')

shotcall_delay = DoubleVar()
shotcall_delay.set(12.0)

Label(timerframe, text="Shotcall delay (seconds)", anchor="e", font=defaultfont, width=18).grid(row=1, column=0, sticky='se', padx=30)
shotcall_delayW = Scale(timerframe, from_=0, to=20.0, length=200, orient='horizontal', resolution=0.1, variable=shotcall_delay)
shotcall_delayW.grid(row=1, column=1, sticky='se')

# 3-BAR FRAME
shot_amount = IntVar()
shot_amount.set(5)

Label(threebarframe, text="Amount of shots", anchor="e", font=defaultfont, width=23).grid(row=0, column=0, sticky='se', padx=10, pady=20)
Radiobutton(threebarframe, text='3', variable=shot_amount, value=3).grid(row=0, column=1, padx=24, pady=20,sticky='se')
Radiobutton(threebarframe, text='5', variable=shot_amount, value=5).grid(row=0, column=2, padx=24, pady=20,sticky='se')
Radiobutton(threebarframe, text='7', variable=shot_amount, value=7).grid(row=0, column=3,padx=24, pady=20, sticky='se')

# 2-BAR FRAME




mainwindow.mainloop()