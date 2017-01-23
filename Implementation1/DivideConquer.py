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

def compare(pointA,pointB):
	d = distance(pointA,pointB)
	global min
	if d < min:
		min = d
		#print min

def divideAndConquer(points):	
	if len(points) == 2: 
		compare(points[0], points[1])
	else:
		mid = len(points)/2
		left = points[:mid]
		right = points[-mid:]
		print left, right

		compare(left[0],right[0])
		global min
		print min
		minleft = divideAndConquer(left)
		minRight = divideAndConquer(right)
		

divideAndConquer(readFile())
print min
