#!/usr/bin/python3.5
from math import sqrt
mapLayout=5*"*****"
mapLength=int(sqrt(len(mapLayout)))
usrLocation=[1,3]
for i in range(0,mapLength):
	if i!=usrLocation[0]:
		print(mapLayout[(i*mapLength):(i*mapLength+mapLength)])
	else:
		print(mapLayout[(i*mapLength):(i*mapLength+mapLength-(mapLength-usrLocation[1]))]+"@"+mapLayout[(i*mapLength+mapLength-(mapLength-usrLocation[1])+1):(i*mapLength+mapLength)])