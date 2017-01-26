import math
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty, Levi Willmeth
	Winter 2017
'''

inputfile = "example.input"#"example.input"
DEBUGGING = True

delta = 999
min_pts = []

def readFile():
	pts=[]
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
	global delta, min_pts
	d = distance(a,b)
	if(d < delta):
		min_pts = [(a, b)]
		delta = d
	elif(d == delta):
		min_pts.append(pts)
	return d


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
			dm = minDistance(d, dm, cur_pts)
			j = j+1
			break
	return dm


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
		return min( findDistance(pts[0], pts[2]),findDistance(pts[1], pts[2]) )
		
	else:
		m = len(pts)/2
		L = pts[:m]
		R = pts[-m:]

		dL = divideAndConquer(L)
		dR = divideAndConquer(R)
		d = min(dL, dR)
		#if DEBUGGING: print 'dL={}, dR={}, d={}, min_pts={}'.format(dL, dR, d, min_pts)
		return d

inputs = readFile()
inputs.sort(key=lambda s: s[0]) #sort points by x value - (nlogn)
d = divideAndConquer(inputs)
L = findXL(inputs)
if DEBUGGING:
	#print 'L is: {}, {}'.format(L, inputs)
	print 'Delta: {}, closest (side) points are: {}'.format(d, min_pts)
