import random
import os
import pyttsx3
import keyboard
import threading
import winsound
import time
import __main__ as gui
import sys

TICKRATE = (1.0 / 100)

def	print_banner():
	print("\
███████╗ ██████╗  ██████╗ ███████╗    ████████╗██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ \n\
██╔════╝██╔═══██╗██╔═══██╗██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗\n\
█████╗  ██║   ██║██║   ██║███████╗       ██║   ██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝\n\
██╔══╝  ██║   ██║██║   ██║╚════██║       ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗\n\
██║     ╚██████╔╝╚██████╔╝███████║       ██║   ██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║\n\
╚═╝      ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")

def loopfor(funct, secs, args=None):
	global mytimer
	mytimer.start()
	while mytimer.get() < secs:
		time.sleep(TICKRATE)
		funct(args)

class KillTraining(Exception): pass

def check_pause(flag=None):
	global mytimer
	if flag == None:
		mytimer.start()
	if gui.pauseswitch == 1:
		print("training paused. press space to resume")
		mytimer.pause()
		while gui.pauseswitch == 1:
			time.sleep(TICKRATE)
		mytimer.resume()
		print("resuming training...")
	if gui.startswitch == 0:
		raise KillTraining

def	output_sentence(sentence, engine, speed):
	global rate
	engine.setProperty('rate', rate + speed)
	engine.say(sentence)
	engine.runAndWait()

def delayed_beep(offset, beepdelay):
	time.sleep(beepdelay + 0.05 + 0.05 * (offset - 4 if offset > 4 else 0))
	winsound.Beep(2500, 500)
	# sys.stdout.write('\a')					<--- crossplatform method to produce a system sound. is not accurate in timing

def training_loop(training, engine, interval_range, weights, calls, beepdelay, shot_series=None):
	try:
		engine.setProperty('rate', rate-20)
		if training == 3:
			engine.say("start three baar training. " + shot_series)
			print("start 3-bar training: " + shot_series)
		elif training == 5:
			engine.say("start five baar training. " + shot_series)
			print("start 5-bar training: " + shot_series)
		elif training == 2:
			engine.say("start two baar training. " + shot_series)
			print("start 2-bar training: " + shot_series)
		engine.runAndWait()
		loopfor(check_pause, 3, 1)
		while 1:
			check_pause()
			clock = random.randrange(1, 2 + interval_range)
			shotcall = random.choices(calls, weights)[0]
			output_sentence("set up the ball", engine, -10)
			check_pause()
			output_sentence("time in", engine, 0)
			loopfor(check_pause, clock, 1)
			beep = threading.Thread(target=delayed_beep, args=((len(shotcall.get()), beepdelay)))
			beep.start()
			output_sentence(shotcall.get(), engine, 30)
			print("%s %*d seconds" %(shotcall.get(), 13 - len(shotcall.get()), clock))
			if training == 5:
				loopfor(check_pause, 2.0, 1)
			else:
				loopfor(check_pause, 2.5, 1)
	except KillTraining:
		print("stopped")

class MyTimer():

    def __init__(self):
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def start(self):
        self.timestarted = time.time()

    def pause(self):
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if self.paused:
            raise ValueError("Timer is already paused")
        self.timepaused = time.time()
        self.paused = True

    def resume(self):
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if not self.paused:
            raise ValueError("Timer is not paused")
        pausetime = time.time() - self.timepaused
        self.timestarted = self.timestarted + pausetime
        self.paused = False

    def get(self):
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return time.time() - self.timestarted

# print banner
print_banner()

# initialising engine and variables
# pauseswitch = 0
# kill_thread = threading.Thread(target=kill_handler)
# kill_thread.daemon = True
# kill_thread.start()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice', voices[1].id)
mytimer = MyTimer()
# keyboard.on_press_key("space", gui.handle_pauseplay)

# input reading. configuring settings
# training = input("select your training:\n\
# 1: 3-bar\n2: 5-bar\n3: 2-bar\n")
# while not training == "1" and not training == "2" and not training == "3":
# 	training = input("wrong input. choose 1 or 2:\n1: 3-bar training\n2: 5-bar training\n3: 2-bar training\n")
# if training == "1":
# 	settings = input("do you want to use default settings or custom settings:\n\
# 1: default settings\n2: custom settings\n")
# 	while not settings == "1" and not settings == "2":
# 		settings = input("wrong input. choose 1 or 2:\n1: default settings\n2: custom settings\n")
# 	if settings == "2":
# 		interval_range = input("choose the range of random time interval in seconds:\n")
# 		while not interval_range.isnumeric or int(interval_range) < 0:
# 			interval_range = input("wrong input. choose the range of random time interval in seconds:\n")
# 		holes = input("choose how many holes (3, 5 or 7):\n")
# 		while not holes == "3" and not holes == "5" and not holes == "7":
# 			holes = input ("wrong input. choose how many shot options (3, 5 or 7):\n")
# 		weights = list()
# 		print("choose the probability of each hole (starting from your side):")
# 		for hole in range(int(holes)):
# 			weights.append(input("probability for hole " + str(hole + 1) + ":\n"))
# 			while not weights[-1].isnumeric:
# 				weights[-1] = input("wrong input. please choose a numer:\nprobability for hole" + hole + ":\n")
# 			weights[-1] = float(weights[-1])
# 		interval_range = int(interval_range)
# 	else:
# 		interval_range = 12
# 		holes = "3"
# 		weights = [0.33, 0.33, 0.33]
# 	if holes == "3":
# 		calls = ["short", "middle", "long"]
# 	elif holes == "5":
# 		calls = ["one", "two", "three", "four", "five"]
# 	elif holes == "7":
# 		calls = ["one", "two", "three", "four", "five", "six", "seven"]
# elif training == "2":
# 	calls = ["lane", "wall", "overlane"]
# 	weights = [0.4, 0.4, 0.1]
# 	interval_range = 7
# if training == "3":
# 	shot_series = input("choose a 2-bar training:\n1: pullshot\n2: pinshot\n3: bankshot\n")
# 	while shot_series != "1" and shot_series != "2" and shot_series != "3":
# 		shot_series = input("wrong input. choose a 2-bar training:\n1: pullshot\n2: pinshot\n3: bankshot\n")
# 	if shot_series == "1":
# 		shot_series = "pull shot"
# 		calls = ["slice", "short square", "mid square", "spray mid", "long"]
# 	if shot_series == "2":
# 		shot_series = "pin shot"
# 		calls = ["short", "middle", "long", "near bank", "far bank"]
# 	if shot_series == "3":
# 		shot_series = "bank shot"
# 		calls = ["far bank", "near bank", "pullshot", "up slice", "down slice"]
# 	weights = [0.2, 0.2, 0.2, 0.2, 0.2]
# 	interval_range = 7
# else:
# 	shot_series = None

# beepdelay = input("choose the time between shotcall and beep (reaction speed):\nBeginner: 1.2\nAdvanced: 1\nPro: 0.8\n")
# while not beepdelay.isnumeric or float(beepdelay) < 0:
# 	beepdelay = input("wrong input. choose the time between shotcall and beep in seconds:\n")
# beepdelay = float(beepdelay)

# training_loop(training, engine, interval_range, weights, calls, shot_series)


