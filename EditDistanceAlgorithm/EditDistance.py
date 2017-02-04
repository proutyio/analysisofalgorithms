

def editDistance(strA, strB):

	lenA = len(strA)
	lenB = len(strB)
	table = [[0 for s in range(lenB+1)] for s in range(lenA+1)]

	for x in range(lenA+1):
	    for y in range(lenB+1): 
	        if(x == 0):
	            table[x][y] = y
	        
	        elif(y == 0):
	            table[x][y] = x

	        elif(strA[(x-1)] == strB[(y-1)]):
	            table[x][y] = table[x-1][y-1] 

	        else:
	            table[x][y] = 1+min(table[x][y-1],
	                                table[x-1][y],
	                                table[x-1][y-1])     
	return table


def printTable(table):
	for r in table:
		print r

printTable( editDistance("intention","execution") )