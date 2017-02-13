import sys, re

if(len(sys.argv)>2):
    costFile = '-'+sys.argv[1]
    seqFile = '-'+sys.argv[2]
else:
    print "Usage: python seqAlign <cost file> <sequence file>"

def readCostFile(cFile):
    ''' Read the cost array into a dictionary '''
    costs = {}
    with open(cFile, 'r') as file:
        chars = ''
        for f in file:
            f = f.strip('\n')
            f = f.split(',')
            if f[0] is '*':
                # Read in available chars but skip the leading *
                chars = f
                for k in f[1:]:
                    costs[k] = {}
            else:
                # Treat this line as costs for the far left char
                for i, c in enumerate(f):
                    # print f[0], chars[i], ' => ', c
                    costs[f[0]][chars[i]] = c
    return costs, chars[1:]

def printArr(arr):
    ''' Display the array as it would appear on paper '''
    # Print the header
    print ' #',
    for x in topWord:
        # Pad each column to 2 spaces to fix large inputs
        print "{:>2}".format(x),
    print ''
    # Print each line
    for y in range(lenSide):
        for x in range(lenTop):
            if x is 0:
                print "{:>2}".format(sideWord[y]),
            print "{:>2}".format(arr[x][y]),
        print ''

def printCosts(arr):
    ''' Display the costs as an unsorted array '''
    # Print the header
    print ' #',
    for a in costs:
        # Pad each column to 2 spaces to fix large inputs
        print "{:>2}".format(a),
    print ''
    # Print each line
    for a in costs:
        print "{:>2}".format(a),
        for b in costs:
            print "{:>2}".format(costs[a][b]),
        print ''

def getCost(a, b):
    ''' Returns cost to convert from one letter to another '''
    return int(costs[a][b])

# Save word sizes for later
# GTTACTTGACAGGTCCCCCCG,ACCATCCATGAACTTGCGACCCTC
topWord =  '-AAATGTGTGTGTTCCCCAACGATGTCTCTAGAAGACGAACATCCC'
sideWord = '-ATGGAAACGTGAACCTAACTAACACATATGGATCCGACTGACGTTCTCTGATGTAGCCT'
lenTop = len(topWord)
lenSide = len(sideWord)

# A = [[x+y if (x==0 or y==0) else 0 for x in range(lenSide)] for y in range(lenTop)]
A = [[0 for x in range(lenSide)] for y in range(lenTop)]

costs, chars = readCostFile('imp2cost.txt')

for i in range(1,lenTop):
    A[i][0] = A[i-1][0] + getCost('-', topWord[i])

for i in range(1, lenSide):
    A[0][i] = A[0][i-1] + getCost('-', sideWord[i])
# for a in chars:
#     for b in chars:
#         print a,b,getCost(a,b)

print '=== Result Array ==='
printArr(A)
print '=== Cost Array ==='
printCosts(costs)
print '=== Calculating ==='

print "Cost to convert from A to G:"

for x in range(1,lenTop):
    for y in range(1,lenSide):
        a, b = topWord[x], sideWord[y]
        A[x][y] = min(
            A[x-1][y] + getCost('-', sideWord[y]),
            A[x][y-1] + getCost(topWord[x], '-'),
            A[x-1][y-1] + getCost(topWord[x], sideWord[y])
        )
        # print x-1, y-1, topWord[x-1], sideWord[y-1], '=>', A[x][y]
        # A[x][y] = min(
        #     A[x-1][y] + 1,
        #     A[x][y-1] + 1,
        #     A[x-1][y-1] + (2, 0)[topWord[x] == sideWord[y]]
        # )

print 'The resulting array:'
printArr(A)
