#!/usr/bin/python3.5
from plkgame import clearScreen
from math import sqrt
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

#	def printrectanglemap(self,L,W, usrLocation):
#		if (L*W) != len(mapLayout):
#			import gameError
#			ERROR(("L/W/T: "+L+"/"+W+"/"+len(mapLayout)+"\n"+"self.mapLayout: "+self.mapLayout+"\n"))


#def MoveInRoom(usrLoc):
#	while True:
#		User_Input=getch()
#		if User_Input in CONST_Valid_Moves:
#			if User_Input =="d":
#				if userLoc[1] < currentroom.mapLength:
#					userLoc+=1
#					clearScreen()
#
#
#			elif User_Input =="s":
#			elif User_Input =="a":
#			elif User_Input =="w":
#			elif User_Input =="z":
#			elif User_Input =="c":

			
#	return(location)