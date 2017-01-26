
from random import randint

def generatePoints():
	print
	total = input("How many points to generate? ")

	f = open('points.input', 'w')
	for i in range(0,total):
		x = randint(0,100)
		y = randint(101,200)
		f.write(str(x)+" "+str(y)+"\n")
	f.close()
	print
	print "File Created Successfully! - file name:\"points.input\""
	print

generatePoints()

