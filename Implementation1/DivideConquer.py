#!/usr/bin/python
import math, sys
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty, Levi Willmeth
	Winter 2017
'''

if(len(sys.argv)>1):
	inputfile = sys.argv[1]
else:
	inputfile = 'points.input'

DEBUGGING = True
delta = 999
min_pts = []
pts=[]

def readFile():
	global pts
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	return pts


def distance(p1,p2):
	'Returns distance between two points'
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

'''
def minDistance(distance,delta, pts):
	if(distance < delta):
		min_pts = [pts]
		delta = distance
	elif(distance == delta):
		min_pts.append(pts)
	return delta
'''

def findDistance(a, b):
	'Updates globals based on distance between two points'
	global delta, min_pts, pts
	d = distance(a,b)
	# print '({},{}) = {}'.format(a,b,d)
	if(d < delta):
		# print '{} < {} for ({},{})'.format(d, delta, a, b)
		min_pts = [[a, b]]
		delta = d
	elif(d == delta):
		# print '{} == {} for ({},{})'.format(d, delta, a, b)
		min_pts.append([a,b])
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

# def closestCrossPairs(pts,dt):
# 	dm = dt
# 	for i in range(1, len(pts)-1):
# 		j = i+1
# 		while pts[i+1][1] - pts[i][1] <= dt and j <= len(pts):
# 			d = distance(pts[i], pts[i+1])
# 			if d == 0:
# 				break
# 			cur_pts = (pts[i], pts[i+1])
# 			#print cur_pts
# 			dm = minDistance(d, dm, cur_pts)
# 			j = j+1
# 			break
# 	return dm


def findXL(fullList):
	'Returns midpoint on x line, between the middle two elements'
	m = len(fullList)/2
	L = float(fullList[m+1][0]-fullList[m][0])/2+fullList[m][0]
	#if DEBUGGING: print "Midpoint is between {} and {}.".format(fullList[m][0], fullList[m+1][0])
	return L


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
		L = pts[:m+1]
		R = pts[-m:]
		# print 'Checking L[{}]'.format(L)
		dL = divideAndConquer(L)
		# print 'Checking R[{}]'.format(R)
		dR = divideAndConquer(R)
		d = min(dL, dR)
		#if DEBUGGING: print 'dL={}, dR={}, d={}, min_pts={}'.format(dL, dR, d, min_pts)
		return d

inputs = readFile()
inputs.sort(key=lambda s: s[0]) #sort points by x value - (nlogn)
d = divideAndConquer(inputs)
L = findXL(inputs)

# if DEBUGGING:
# 	print 'L is: {} from points {}'.format(L, inputs)
# 	print 'Delta: {}, qualifying (side) pairs are: {}'.format(d, min_pts)

middlePairs = [p for p in inputs if p[0] >= L-delta and p[0] <= L+delta]

deltaMiddle = closestCrossPairs(middlePairs, delta)

# if DEBUGGING:
# 	print 'deltaMiddle=',deltaMiddle
# 	print 'Global Delta: {}, qualifying (side) pairs are: {}'.format(d, min_pts)

# Here is the real result:
print d
for (a,b) in min_pts:
	print a,b
