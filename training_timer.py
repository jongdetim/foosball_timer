import random
import pyttsx3
import keyboard
import threading
import winsound

def stoprunning(_):
	print("quitting...")
	escape.set()

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
			if (escape.is_set()):
				exit()
		print("resuming training...")
		return 0

def	output_sentence(sentence, set_pause, engine):
	engine.say(sentence)
	set_pause = check_pause(set_pause)
	if escape.is_set():
		exit()
	engine.runAndWait()
	set_pause = check_pause(set_pause)
	if escape.is_set():
		exit()
	return set_pause

# input reading. configuring settings

settings = input("do you want to use default settings or custom settings:\n\
0: default settings\n1: custom settings\n")
while not settings == "0" and not settings == "1":
	settings = input("wrong input. choose 0 or 1:\n0: default settings\n1: custom settings\n")
if settings == "1":
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

# initialising engine and variables

set_pause = 0
escape = threading.Event()
engine = pyttsx3.init()     		# <-- deze text to speech init is sloom en maakt ook de exit() heel sloom
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice', voices[1].id)
if holes == "3":
	calls = ["short", "middle", "long"]
elif holes == "5":
	calls = ["one", "two", "three", "four", "five"]
elif holes == "7":
	calls = ["one", "two", "three", "four", "five", "six", "seven"]

keyboard.on_press_key("esc", stoprunning)
keyboard.on_press_key("space", pause)

# main loop

engine.say("start three baar training")
engine.runAndWait()
escape.wait(3)
while not escape.is_set():
	set_pause = check_pause(set_pause)
	clock = random.randrange(3, 4 + interval_range)
	shotcall = random.choices(calls, weights)
	output_sentence("set up the ball", set_pause, engine)
	output_sentence("time in", set_pause, engine)
	escape.wait(clock)
	output_sentence(shotcall, set_pause, engine)
	print("%s %*d seconds" %(*shotcall, 13 - len(*shotcall), clock))
	# escape.wait(1)
	winsound.Beep(2500, 500)
	escape.wait(2.5)

