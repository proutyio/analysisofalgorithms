import math
'''
	CS 325 - Implementation 1
		Divide and Conquer

	Kyle Prouty
	Winter 2017
'''

inputfile = "example.input"

delta =0

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

#def minPts(p1,p2)
	#a = distance(p1)


def closestCrossPairs(pts,dt):
	dm = dt
	for i in range(1, len(pts)-1):
		j = i+1
		while pts[i+1][1] - pts[i][1] <= dt and j <= len(pts):
			d = distance(pts[i], pts[i+1])
			dm = min(d, dm)
			j = j+1
	return dm



def divideAndConquer(pts):	
	if len(pts) < 3:
		return pts  
	else:
		pts.sort(key=lambda s: s[0]) #sort points by x value - (nlogn)
		m = len(pts)/2				
		l = pts[:m]
		r = pts[-m:]

		d1 = divideAndConquer(l)
		d2 = divideAndConquer(r)

		if d1 and d2 is not None:
			global delta
			#delta = min( distance(d1[0],d1[1]), distance(d2[0],d2[1]) )

		pts.sort(key=lambda s: s[1])
		dm = closestCrossPairs(pts,1)
		return dm

		
print divideAndConquer(readFile())
