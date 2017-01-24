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


def min(a,b):
	if(a < b):
		return a
	else:
		return b


def closestCrossPairs():
	print


def divideAndConquer(points):	
	if len(points) <= 3: 
		return distance(points[0], points[1])
	else:
		mid = len(points)/2
		left = points[:mid]
		right = points[-mid:]

		d1 = divideAndConquer(left)
		d2 = divideAndConquer(right)
		d = min(d1,d2)
		return d

		
print divideAndConquer(readFile())
