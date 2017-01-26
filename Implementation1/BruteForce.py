import math, sys
'''
	CS 325 - Implementation 1
		Brute Force

	Kyle Prouty
	Winter 2017
'''
minlst=[]

if(len(sys.argv)>1):
	inputfile = sys.argv[1]
else:
	inputfile = 'example.input'


def readFile():
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	pts.sort(key=lambda s:s[1])
	pts.sort(key=lambda s:s[0])
	return pts


def distance(p1, p2):
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def bruteForce(pts):
	global minlst
	min = float("inf")
	x=0
	for p1 in pts:
		x+=1
		j=0
		for p2 in pts:
			print x,j
			if(j==x):
				break
			else:
				d = distance(p1, p2)
				if(d < min): 
					min = d
					minlst = [[p1,p2]]
				elif(d == min):
					if not isDuplicate(p1,p2):
						minlst.append([p1,p2])
			j+=1
	return min


def isDuplicate(p1, p2):
	global minlst
	for p in minlst:
		if((p[0]==p1) and (p[1]==p2)) or ((p[0]==p2) and (p[1]==p1)):
			return True
	return False
	

print bruteForce( readFile() )
for (a,b) in minlst:
	print a,b