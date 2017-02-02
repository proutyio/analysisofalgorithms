#!/usr/bin/python
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty, Levi Willmeth
	Winter 2017
'''
import math, sys, time

if(len(sys.argv)>1):
	inputfile = sys.argv[1]
else:
	inputfile = 'example.input'

delta = float("inf")
min_pts = []

def readFile():
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	pts.sort(key=lambda s: s[0])
	return pts



def distance(p1,p2):
	'Returns distance between two points'
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)



def findDistance(p1, p2):
	'Updates globals based on distance between two points'
	global delta, min_pts
	d = distance(p1,p2)
	if(d < delta):
		min_pts = [[p1, p2]]
		delta = d
	elif(d == delta):
		if not isDuplicate(p1,p2):
			min_pts.append([p1,p2])
	return d



def closestCrossPairs(pts, dt):
	'Checks center area for nearby pairs, returns delta'
	dm = dt
	for i in range(1, len(pts)-1):
		j = i+1
		while pts[i+1][1] - pts[i][1] <= dt and j <= len(pts):
			d = findDistance(pts[i], pts[i+1])
			j += 1
	return dm



def findMidX(pts):
	'Returns midpoint on x line, between the middle two elements'
	m = len(pts)/2
	midX = float(pts[m+1][0]-pts[m][0])/2+pts[m][0]
	return midX



def divideAndConquer(pts):
	if len(pts) == 2:
		return findDistance(pts[0], pts[1])
	elif len(pts) == 3:
		return min(
			findDistance(pts[0], pts[1]),
			findDistance(pts[0], pts[2]),
			findDistance(pts[1], pts[2])
		)
	else:
		m = len(pts)/2
		L = pts[:m]
		R = pts[m:]

		dL = divideAndConquer(L)
		dR = divideAndConquer(R)
		d = min(dL, dR)

		midX = findMidX(pts)
		pts.sort(key=lambda s: s[1])
		middlePairs = [p for p in pts if p[0] >= midX-delta and p[0] <= midX+delta]
		deltaMiddle = closestCrossPairs(middlePairs, delta)
		return deltaMiddle


def isDuplicate(p1, p2):
	for p in min_pts:
		if((p[0]==p1) and (p[1]==p2)) or ((p[0]==p2) and (p[1]==p1)):
			return True
	return False


def sortPoints(lst):
	for x in range(0,len(lst)):
		if lst[x][0][0] > lst[x][1][0]:
			lst[x] = (lst[x][1],lst[x][0])
		elif lst[x][0][1] > lst[x][1][1]:
			lst[x] = (lst[x][1],lst[x][0])
	return lst


print divideAndConquer( readFile() )

min_pts = sortPoints(min_pts)
for (a,b) in min_pts:
	print a,b
