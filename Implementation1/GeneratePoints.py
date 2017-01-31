import random

def randomPoints(total):
	numberofpoints=total
	radius = 1
	rangeX = (0, 100000)
	rangeY = (0, 100000)
	deltas = set()
	for x in range(-radius, radius+1):
		for y in range(-radius, radius+1):
			if x*x + y*y <= radius*radius:
				deltas.add((x,y))
	randPoints = []
	excluded = set()
	i = 0
	while i<numberofpoints:
		x = random.randrange(*rangeX)
		y = random.randrange(*rangeY)
		if (x,y) in excluded: continue
		randPoints.append((x,y))
		i += 1
		excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
	return randPoints


def generatePoints():
	total = input("How many points to generate? ")

	f = open('points.input', 'w')
	for p in randomPoints(total):
		f.write(str(p[0])+" "+str(p[1])+"\n")
	f.close()
	print "\nFile Created Successfully! - file name:\"points.input\"\n"


generatePoints()

