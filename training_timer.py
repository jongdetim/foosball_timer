import sys
import random
import pyttsx3
import keyboard
import threading

def stoprunning(_):
	print("quitting...")
	escape.set()

def showusage():
	print("usage: python training_timer.py [c]\n\
        c: custom options")
	exit()

if len(sys.argv) > 1:
	if sys.argv[1] == "c":
		interval_range = input("choose the range of random time interval in seconds:\n")
		while not interval_range.isnumeric or int(interval_range) < 0:
			interval_range = input("wrong input. choose the range of random time interval in seconds:\n")
		# shots = input("choose how many shot options (3, 5 or 7):\n")
		interval_range = int(interval_range)
	else:
		showusage()
else:
	interval_range = 12

escape = threading.Event()
engine = pyttsx3.init()     				# <-- deze text to speech init is sloom en maakt ook de exit() heel sloom
calls = ["short", "middle", "long"]
keyboard.on_press_key("esc", stoprunning)

while not escape.is_set():
	clock = random.randrange(3, 4 + interval_range)
	shotcall = random.randrange(0,3)
	escape.wait(clock)
	if escape.is_set():
		break
	engine.say(calls[shotcall])
	print(calls[shotcall])
	engine.runAndWait()
	escape.wait(2)
	engine.say("set up the ball")
	engine.runAndWait()
