import random, sys

if(len(sys.argv)>1):
    size = int(sys.argv[1])
else:
    print "Usage: python generateInputs.py <num chars per input>"
    sys.exit()

validChars = list('AGTC')

with open('imp2input.txt', 'w+') as f:
    for i in xrange(10):
        a = ''
        b = ''
        for n in xrange(size):
            a += random.choice(validChars)
            b += random.choice(validChars)
        f.write('{},{}\n'.format(a, b))
