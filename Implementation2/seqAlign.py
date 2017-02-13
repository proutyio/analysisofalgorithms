import sys

if(len(sys.argv)>2):
    topWord = '-'+sys.argv[1]
    sideWord = '-'+sys.argv[2]
else:
    topWord = '-ATCC'
    sideWord = '-TCAC'

def printA():
    ''' Display the array as it would appear on paper '''
    print '#',
    for x in topWord:
        print x,
    print ''
    for y in range(lenSide):
        for x in range(lenTop):
            if x is 0:
                print sideWord[y],
            print A[x][y],
        print ''

lenTop = len(topWord)
lenSide = len(sideWord)

# A = [[x+y if (x==0 or y==0) for x in range(lenTop)] for y in range(lenSide)]
A = [[x+y if (x==0 or y==0) else 0 for x in range(lenSide)] for y in range(lenTop)]
A[0][0] = 0
printA()

for x in range(1,lenTop):
    # print 'x = ', x
    for y in range(1,lenSide):
        A[x][y] = min(
            A[x-1][y] + 1,
            A[x][y-1] + 1,
            A[x-1][y-1] + (2, 0)[topWord[x] == sideWord[y]]
        )
        # print [x,y],(A[x][y], A[x-1][y] + 1, A[x][y-1] + 1, A[x-1][y-1] + (2, 0)[topWord[x] == sideWord[y]]), topWord[x], sideWord[y], A[x]

print 'The resulting array:'
printA()
