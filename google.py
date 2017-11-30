#!/usr/bin/python3.5 
import argparse ##By: Phil King
import subprocess
def urlencodegen(): ###Used to generate the dictionary: urlkeys
	a=0
	post="""~`!%40%23%24%25^%26*()_-%2B%3D{[}]\|%3B%3A'"%2C<.>%2F%3F"""
	pre="""~`!@#$%^&*()_-+={[}]\|;:'",<.>/?"""
	urlkeys=dict([('+','%2B'), ('?','%3F'), ('@','%40'), (':','%3A'), ('$','%24'), ('&','%26'), (',','%2C'), ('=','%3D'), ('%','%25'), ('#','%23'), (';','%3B'), ('/','%2F')])
	print(urlkeys)
	print(post)
	print(pre)
	for b,character in enumerate(pre):
		i=a+b		
		print(post[i]+"/"+character)
		print(post[i:i+3:1])		
		if character != post[i] or character=="%":
			newlist[character]=post[i:i+3:1]
			a+=2
	print("dict([",end="")
		
	for i,a in enumerate(newlist):
		if i!=(len(newlist)):
			print("('"+a+"','"+newlist[a]+"'), ",end="")
		else:
			print("('"+a+"','"+newlist[a]+"')",end="")
		
	print("])")

def urlencode(): #Translates the arguments into urlencoded speach
	urlkeys=dict([('+','%2B'), ('?','%3F'), ('@','%40'), (':','%3A'), ('$','%24'), ('&','%26'), (',','%2C'), ('=','%3D'), ('%','%25'), ('#','%23'), (';','%3B'), ('/','%2F')])
	for a in args.string:
		for i,b in enumerate(a):
			google.append(b)
			if b in urlkeys:
				google.append(urlkeys[b])
		google.append(" ")
####DEFINING ARGUMENTS
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('string', metavar='N', type=str, nargs='+',
                    help='to be googled')
args=parser.parse_args()
####


		
google=[]
completedgoogle=""
newlist={}
google.append("https://www.google.ca/search?safe=active&source=hp&ei=7DAfWrGID5KUkwXpkrHYCg&q=")
urlencode()
google.append("&gs_l=psy-ab.3..0l2j0i131k1j0l7.1630.1835.0.2059.2.2.0.0.0.0.153.302.0j2.2.0....0...1c.1.64.psy-ab..0.2.301....0.qo8xvjfLnRI")
for i in google:
	completedgoogle=completedgoogle+i
subprocess.call(['firefox',completedgoogle])


