import random
import signal
import os
import pyttsx3
import keyboard
import threading
import winsound
import time

def	print_banner():
	print("\
███████╗ ██████╗  ██████╗ ███████╗    ████████╗██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ \n\
██╔════╝██╔═══██╗██╔═══██╗██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗\n\
█████╗  ██║   ██║██║   ██║███████╗       ██║   ██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝\n\
██╔══╝  ██║   ██║██║   ██║╚════██║       ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗\n\
██║     ╚██████╔╝╚██████╔╝███████║       ██║   ██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║\n\
╚═╝      ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")

def kill_handler():
	switch = 0
	while switch == 0:
		if keyboard.is_pressed('esc'):
			switch = 1
	print("quitting...")
	os.kill(os.getpid(), signal.SIGINT)

def pause(_):
	global set_pause
	set_pause = 1

def showusage():
	print("usage: python training_timer.py\n[space]: pause, [esc]: quit")
	exit()

def check_pause(set_pause):
	if set_pause == 1:
		print("training paused. press space to resume")
		while not keyboard.is_pressed('space') == 1:
			pass
		print("resuming training...")
		return 0

def	output_sentence(sentence, set_pause, engine):
	engine.say(sentence)
	set_pause = check_pause(set_pause)
	engine.runAndWait()
	set_pause = check_pause(set_pause)
	return set_pause

def training_loop(training, engine, set_pause, interval_range, weights, calls):
	if training == "1":
		engine.say("start three baar training")
	elif training == "2":
		engine.say("start five baar training")
	engine.runAndWait()
	time.sleep(3)
	while 1:
		set_pause = check_pause(set_pause)
		clock = random.randrange(3, 4 + interval_range)
		shotcall = random.choices(calls, weights)
		output_sentence("set up the ball", set_pause, engine)
		output_sentence("time in", set_pause, engine)
		time.sleep(clock)
		output_sentence(shotcall, set_pause, engine)
		print("%s %*d seconds" %(*shotcall, 13 - len(*shotcall), clock))
		winsound.Beep(2500, 500)
		time.sleep(2.5)

# print banner
print_banner()

# initialising engine and variables
set_pause = 0
kill_thread = threading.Thread(target=kill_handler)
kill_thread.daemon = True
kill_thread.start()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice', voices[1].id)

keyboard.on_press_key("space", pause)

# input reading. configuring settings
training = input("select your training:\n\
1: 3-bar\n2: 5-bar\n")
while not training == "1" and not training == "2":
	training = input("wrong input. choose 1 or 2:\n1: 3-bar training\n2: 5-bar training\n")
if training == "1":
	settings = input("do you want to use default settings or custom settings:\n\
1: default settings\n2: custom settings\n")
	while not settings == "1" and not settings == "2":
		settings = input("wrong input. choose 1 or 2:\n1: default settings\n2: custom settings\n")
	if settings == "2":
		interval_range = input("choose the range of random time interval in seconds:\n")
		while not interval_range.isnumeric or int(interval_range) < 0:
			interval_range = input("wrong input. choose the range of random time interval in seconds:\n")
		holes = input("choose how many holes (3, 5 or 7):\n")
		while not holes == "3" and not holes == "5" and not holes == "7":
			holes = input ("wrong input. choose how many shot options (3, 5 or 7):\n")
		weights = list()
		print("choose the probability of each hole (starting from your side):")
		for hole in range(int(holes)):
			weights.append(input("probability for hole " + str(hole + 1) + ":\n"))
			while not weights[-1].isnumeric:
				weights[-1] = input("wrong input. please choose a numer:\nprobability for hole" + hole + ":\n")
			weights[-1] = float(weights[-1])
		interval_range = int(interval_range)
	else:
		interval_range = 12
		holes = "3"
		weights = [0.33, 0.33, 0.33]
	if holes == "3":
		calls = ["short", "middle", "long"]
	elif holes == "5":
		calls = ["one", "two", "three", "four", "five"]
	elif holes == "7":
		calls = ["one", "two", "three", "four", "five", "six", "seven"]
elif training == "2":
	calls = ["lane", "wall", "overlane"]
	weights = [0.4, 0.4, 0.1]
	interval_range = 7

training_loop(training, engine, set_pause, interval_range, weights, calls)


