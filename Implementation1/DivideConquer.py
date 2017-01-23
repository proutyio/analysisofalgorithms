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
	lst =[]
	with open(inputfile) as file:
		lst = [tuple(map(int, l.split(' '))) for l in file]
	return lst

def distance(tupA, tupB):
	return math.sqrt((tupB[0]-tupA[0])**2 + (tupB[1]-tupA[1])**2)

def compare(x,y):
	d = distance(x,y)
	global min
	if d < min:
		min = d
		print min

def divideAndConquer(lst):	
	if len(lst) < 2: 
		compare(lst[0], lst[0])
	else:
		mid = len(lst)/2
		left = lst[:mid]
		right = lst[-mid:]
		print left, right

		minleft = divideAndConquer(left)
		print minleft
		print

		minRight = divideAndConquer(right)
		print minRight
		print


divideAndConquer(readFile())
