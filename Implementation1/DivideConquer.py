import math
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty
	Winter 2017
'''

inputfile = "example.input"#"example.input"

delta = 0
min_pts = []

def readFile():
	pts=[]
	with open(inputfile) as file:
		pts = [tuple(map(int, l.split(' '))) for l in file]
	return pts


def distance(p1,p2):
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def min(d,dm, pts):
	if(d <= dm):
		min_pts.append(pts)
		return d
	else:
		return dm

def min2(p1, p2):
	''' Returns smaller of two points, based on x '''
	if(p1[0]<p2[0]):
		return p1
	return p2

def closestCrossPairs(pts,dt):
	dm = dt
	for i in range(1, len(pts)-1):
		j = i+1
		while pts[i+1][1] - pts[i][1] <= dt and j <= len(pts):
			d = distance(pts[i], pts[i+1])
			if d == 0:
				break
			cur_pts = (pts[i], pts[i+1])
			#print cur_pts
			dm = min(d, dm, cur_pts)
			j = j+1
			break
	return dm


def findDelta(ptA, ptB):
	return abs(ptB[0]-ptA[0])


def divideAndConquer(pts):
	if len(pts) <= 3:

		d1 = distance(pts[0], pts[1])
		if d1 < delta:
			delta = d1
			min_pairs = (pts[0], pts[1])
		else if d1 == delta:
			min_pairs += (pts[0], pts[1])

		if len(pts) == 3:
			d2 = distance(pts[0], pts[2])
			if d2 < delta:
				delta = d2
				min_pairs = (pts[0], pts[2])
			else if d2 == delta:
				min_pairs += (pts[0], pts[2])

			d3 = distance(pts[1], pts[2])
			if d3 < delta:
				delta = d3
				min_pairs = (pts[1], pts[2])
			else if d3 == delta:
				min_pairs += (pts[1], pts[2])

	else:
		m = len(pts)/2
		l = pts[:m]
		r = pts[-m:]

		d1 = divideAndConquer(l)
		d2 = divideAndConquer(r)

		#if d1 and d2 is not None:
			#delta = min( distance(d1[0],d1[1]), distance(d2[0],d2[1]) )
		pts.sort(key=lambda s: s[1])
		print pts
		dm = closestCrossPairs(pts,2)
		return dm

inputs = readFile()
inputs.sort(key=lambda s: s[0]) #sort points by x value - (nlogn)

print divideAndConquer(inputs)
#min_pts.sort(key=lambda s:s[0])
#for pt in min_pts:
#	print pt[0], pt[1]
