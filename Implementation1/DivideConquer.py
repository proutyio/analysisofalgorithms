import math
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty
	Winter 2017
'''

inputfile = "example.input"
min = float("inf")

def readFile():
	points =[]
	with open(inputfile) as file:
		points = [tuple(map(int, l.split(' '))) for l in file]
	return points


def distance(pointA,pointB):
	return math.sqrt((pointB[0]-pointA[0])**2 + (pointB[1]-pointA[1])**2)


def min(p1,p2):
	a = distance(p1[0],p1[1])
	b = distance(p2[0],p2[1])
	if(a < b):
		return a
	else:
		return b


def closestCrossPairs():
	print


def divideAndConquer(pts):	
	if len(pts) <= 3: 
		return distance(pts[0], pts[1])
	else:
		pts.sort(key=lambda x: x[0]) #sort points by x value - (nlogn)
		m = len(pts)/2				
		l = pts[:m]
		r = pts[-m:]

		d1 = divideAndConquer(l)
		d2 = divideAndConquer(r)
		#d = min(d1,d2)
		#return d

		
print divideAndConquer(readFile())
