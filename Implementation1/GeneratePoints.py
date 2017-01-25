
from random import randint

def generatePoints():
	total = input("How many points to generate? ")
	print total

	f = open('points.input', 'w')
	for i in range(0,total):
		x = randint(0,100)
		y = randint(0,100)
		f.write(str(x)+" "+str(y)+"\n")
	f.close()

generatePoints()

