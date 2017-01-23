import math
'''
	CS 325 - Implementation 1
	Kyle Prouty
	Winter 2017
'''


def readFile():
	lst =[]
	with open("example.input") as file:
		lst = [tuple(map(int, l.split(' '))) for l in file]
	return lst


def distance(tupA, tupB):
	return math.sqrt((tupB[0]-tupA[0])**2 + (tupB[1]-tupA[1])**2)


def printDistances():
	lst = readFile()
	for tupA in lst:
		for tupB in lst:
			print distance(tupA, tupB)


printDistances()