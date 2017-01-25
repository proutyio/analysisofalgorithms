import math
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty
	Winter 2017
'''

inputfile = "example.input"


def readFile():
	pts=[]
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	return pts


def distance(p1,p2):
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def min(a,b):
	if(a < b):
		return a
	else:
		return b


def closestCrossPairs(pts,delta):
	dm = delta
	for i in range(1, len(pts)-1):
		j = i+1
		while pts[i+1][1] - pts[i][1] <= delta and j <= len(pts):
			d = distance(pts[i], pts[i+1])
			print d
			dm = min(d, dm)
			print dm
			j = j+1
	return dm



def divideAndConquer(pts):	
	if len(pts) <= 2:
		return (pts[0], pts[1])  
		#return distance(pts[0], pts[1])
	else:
		pts.sort(key=lambda x: x[0]) #sort points by x value - (nlogn)
		m = len(pts)/2				
		l = pts[:m]
		r = pts[-m:]
		print pts

		d1 = divideAndConquer(l)
		d2 = divideAndConquer(r)
		print d1
		print d2

		#d = min(d1,d2)
		#print d
		#return d

		
#print divideAndConquer(readFile())
pts = readFile()
pts.sort(key=lambda x: x[1])
#print pts
print closestCrossPairs(pts, 6)