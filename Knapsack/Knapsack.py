

#try to make as much money for max weight for knapsack

#do i take item (x)?
#weight left in sack = total weight of already taken items
#edge:
#	adding item
#	neg value of item

#keep track of
#	(item looking at, weight of taken items)


def knapsack(weight, items):

	maxweight = weight+1
	maxitems  = len(items)+1
	
	#build table like EditDistance problem
	table = [[0 for s in range(maxweight)] for s in range(maxitems)]

	for x in range(maxitems):
		for y in range(maxweight):

			if(x==0 or y==0):
				table[x][y] = 0

			elif(items[(x-1)][0] <= y):
				t = items[(x-1)][1] + table[(x-1)][(y-items[(x-1)][0])]
				m = max(t,table[(x-1)][y])
				table[x][y] = m

			else:
				table[x][y] = table[(x-1)][y]

	return (table[maxitems-1][maxweight-1],table)


#items = (weight,value)
items=[(6,30),(3,14),(4,16),(2,9)]
t = knapsack(10,items)

print "Max Value:",t[0]
for i in t[1]:
	print i