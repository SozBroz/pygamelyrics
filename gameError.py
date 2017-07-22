#!/usr/bin/python3.5
def Error(Location
#R
	):
	f=open(ERRORLOG.FFS, 'a')
	f.write(Location)
	#f.write(R)
	print(Location)
	#print(R)
	sys.exit(0)