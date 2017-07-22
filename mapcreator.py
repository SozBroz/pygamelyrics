#!/usr/bin/python3.5
import os.path
import sys
import time
def ERROR():
	print("Usage: mapcreator.py [number of *] [filename in layouts/]")
	print("Filename must be be a string followed by a num ie 'emptyroom0'")
	sys.exit()

if len(sys.argv)!=3:
	ERROR()

try:
	if int(sys.argv[1]) < 0:
		print("How to put in a negative number of *????")
		ERROR()
except ValueError:
	ERROR()

if os.path.exists(("layouts/"+sys.argv[2])):
	if "Y" == input("File exists Overwrite (Y) ????????????\n"):
		print("Will be overwritten in 3 seconds.")
		time.sleep(3)
	else:
		sys.exit("Bye")
try: 
	(int(sys.argv[2][-1]))
	f=open(("layouts/"+sys.argv[2]),'w')
	f.write("*"*int(sys.argv[1]))
except ValueError:
	ERROR()
sys.exit("success, goodbye")



