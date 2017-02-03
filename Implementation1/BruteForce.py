#!/usr/bin/python
'''
	CS 325 - Implementation 1
		Brute Force

	Kyle Prouty, Levi Willmeth, Andrew Morrill
	Winter 2017
'''
import math, sys, time

minlst=[]

if(len(sys.argv)>1):
	inputfile = sys.argv[1]
else:
	inputfile = 'example.input'

def readFile():
	with open(inputfile) as file:
		pts = [tuple(map(float, l.split(' '))) for l in file]
	pts.sort(key=lambda s:s[0])
	return pts


def distance(p1, p2):
	return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)


def bruteForce(pts):
	global minlst
	min = float("inf")
	size = len(pts)

	for i in range(0,size):
		for j in range(i+1,size):
			d = distance(pts[i], pts[j])
			if(d < min):
				min = d
				minlst = sorted([[pts[i],pts[j]]])
			elif(d == min):
				if not isDuplicate(pts[i],pts[j]):
					minlst.append(sorted([pts[i],pts[j]]))
	return min


def isDuplicate(p1, p2):
	global minlst
	for p in minlst:
		if((p[0]==p1) and (p[1]==p2)) or ((p[0]==p2) and (p[1]==p1)):
			return True
	return False


def sortPoints(lst):
	lst.sort(key=lambda x: [x[0], x[1]])
	for x in range(0,len(lst)):
		if lst[x][0][0] > lst[x][1][0]:
			lst[x] = (lst[x][1],lst[x][0])
		elif lst[x][0][1] > lst[x][1][1]:
			lst[x] = (lst[x][1],lst[x][0])
	return lst


print bruteForce( readFile() )

minlst = sortPoints(minlst)
for (a,b) in minlst:
	print a,b
