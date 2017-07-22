#!/usr/bin/python3.5
#Imports
from time import sleep
from shutil import get_terminal_size
from _thread import start_new_thread
from getch import getch
from sys import exit
from math import sqrt
#------
#Global Variables
watchdog=False
terminal_width=get_terminal_size().columns
terminal_length=get_terminal_size().lines
cursor_location=0
CONST_Valid_Moves=["w","a","s","d","z","x","c"]
#-----
class room:
	def __init__(self, archetype, Identifier):
		self.mapLayout=open(("layouts/"+archetype+str(Identifier)),'r').read()
		self.mapLength=int(sqrt(len(self.mapLayout)))
	def printsquaremap(self,usrLocation):
		clearScreen()
		for i in range(0,self.mapLength):
			if i!=usrLocation[0]:
				print(self.mapLayout[(i*self.mapLength):(i*self.mapLength+self.mapLength)])
			else:
				print(self.mapLayout[(i*self.mapLength):(i*self.mapLength+self.mapLength-(self.mapLength-usrLocation[1]))]+"@"+self.mapLayout[(i*self.mapLength+self.mapLength-(self.mapLength-usrLocation[1])+1):(i*self.mapLength+self.mapLength)])

def cntr(userinput):
	global terminal_width
	print(userinput.center(terminal_width))

def clearScreen():
	for i in range(0,get_terminal_size().lines):
		print()


def wait():
	while input() != "":
		pass
	global watchdog
	watchdog = True

def usrInputFetcher_Init_Menu():
	global cursor_location
	while True:
		temp=getch()
		if temp=='w' or temp=='s':
			if cursor_location == 0:
				cursor_location=1
				printLoadingScreen()
			else:
				cursor_location=0	
				printLoadingScreen()
		elif temp=='z':
			break

def printLoadingScreen():
	clearScreen()
	if cursor_location==0:
		print("New File       @")
		print()
		print("Quit")
	else:
		print("New File")
		print()
		print("Quit           @")
	for i in range(0, int(terminal_length/2-3)):
		print()
def controlList():
	clearScreen()
	print("CONTROLS: \n Left=a \n Right=d \n Up=w \n Down=s \n Continue=z \n Back=x \n Menu=c")
	print()
	cntr("Press Anything to Continue")
	for i in range(0, int(terminal_length/2-10)):
		print()
	getch()
def startUpScreen():
	global terminal_width
	clearScreen()
	cntr("--------------------------")
	cntr("|       PLK GAME         |")
	cntr("|      Press Enter       |")
	cntr("--------------------------")
	for i in range(0,int(get_terminal_size().lines/2-2)):
		print()
	for i in range(0,6):
		sleep(0.2)
		if watchdog==True:
			return True
	cntr("--------------------------")
	cntr("|       PLK GAME         |")
	cntr("|                        |")
	cntr("--------------------------")
	for i in range(0,int(get_terminal_size().lines/2-2)):
		print()
	for i in range(0,6):
		sleep(0.2)
		if watchdog==True:
			return True
	return False

def moveInRoom(userLoc):
	while True:
		User_Input=getch()
		if User_Input in CONST_Valid_Moves:
			if User_Input =="d":
				if userLoc[1] < (currentroom.mapLength-1):
					userLoc[1]+=1
					clearScreen()
					currentroom.printsquaremap(userLocation)
			elif User_Input =="s":
				if userLoc[0] < (currentroom.mapLength-1):
					userLoc[0]+=1
					clearScreen()
					currentroom.printsquaremap(userLocation)
			elif User_Input =="a":
				if userLoc[1] > 0:
					userLoc[1]-=1
					clearScreen()
					currentroom.printsquaremap(userLocation)
			elif User_Input =="w":
				if userLoc[0] > 0:
					userLoc[0]-=1
					clearScreen()
					currentroom.printsquaremap(userLocation)
#			elif User_Input =="z":
#			elif User_Input =="c":

			
	return(location)

start_new_thread(wait,())
while not startUpScreen():
	pass
printLoadingScreen()
usrInputFetcher_Init_Menu()
if cursor_location == 1:
	exit("GOOD BYE")
cursor_location=0	
maplayout=open(("layouts/"+"emptyroom"+str(0)),'r')
roomarchlist=["emptyroom"]
playerhp=10
playericon="@"
userLocation=[0,0]
currentroom=room(roomarchlist[0],0)
currentroom.printsquaremap(userLocation)
while True:
	userLocation=moveInRoom(userLocation)

	
	
	
