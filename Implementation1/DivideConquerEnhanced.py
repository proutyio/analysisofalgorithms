#!/usr/bin/python
'''
	CS 325 - Implementation 1
	Enhanced Divide and Conquer

	Kyle Prouty, Levi Willmeth
	Winter 2017
'''
import math, sys, time

if(len(sys.argv)>1):
	inputfile = sys.argv[1]
else:
	inputfile = 'example.input'

def readFile():
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	return pts


def distance(p1,p2):
	'Returns distance between two points'
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2), [(p1,p2)]


def closestCrossPairs(pts, best):
	'Checks center area for nearby pairs, returns delta'
	print best[0], pts, len(pts)
	for i in range(len(pts)):
		j = i+1
		# print 'Checking within ', best[0],' of i=', i, ', j=', j
		while j<len(pts) and pts[j][0]-pts[i][0]<=best[0]:
			# print "i={0}, j={1} found {2}".format(i, j, distance(pts[i], pts[j]))
			best = compareTwo(distance(pts[i], pts[j]), best)
			j += 1
	return best


def compareTwo(a, b):
	'Returns smallest or combined list of a and b as (f, [(f, f)])'
	if a[0]<b[0]:
		return a
	if a[0]==b[0]:
		return a[0], a[1]+b[1]
	return b


def minOfThree(a, b, c):
	'Returns smallest or combined list of 3 smallest points'
	s = compareTwo(distance(a, b), distance(a, c))
	return compareTwo(s, distance(b, c))


def divideAndConquer(pts):
	'Returns distance and list of points formatted as (dist, [(x,y),...])'
	if len(pts) == 2:
		return distance(pts[0], pts[1])
	elif len(pts) == 3:
		return minOfThree(pts[0], pts[1], pts[2])
	else: # More than 3 elements means we need to divide and conquer.
		m = len(pts)/2
		L = pts[:m]
		R = pts[m:]

		dL = divideAndConquer(L)
		dR = divideAndConquer(R)
		bestSides = compareTwo(dL, dR) # best of left and right halves
		delta = bestSides[0]

		# find midpoint between two centermost array elements
		midX = float(pts[m+1][0]-pts[m][0])/2+pts[m][0]
		# Note!  Here is the problem!  middlePairs should be generated from pts_y
		# but not using a list comp, you should carefully generate it by hand to
		# be more efficient.  Don't check past x and maybe even use binary search to find x
		middlePairs = [p for p in pts if p[0]>=midX-delta and p[0]<=midX+delta]
		# middlePairs.sort(key=lambda s: s[1])
		return closestCrossPairs(middlePairs, bestSides)

pts = readFile()
pts.sort(key=lambda s: s[0])

distance, points = divideAndConquer(pts)
print distance
points = sorted(set(points))
for p in points:
	print "{} {} {} {}".format(p[0][0], p[0][1], p[1][0], p[1][1])
