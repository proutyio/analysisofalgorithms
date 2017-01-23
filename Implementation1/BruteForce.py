


def readFile():
	lst =[]
	with open("example.input") as file:
		lst = [tuple(map(int, l.split(' '))) for l in file]
	print lst

readFile()
