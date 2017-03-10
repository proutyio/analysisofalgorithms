# Practice Implementation
# Finds minimum line fit
import math
x = [1, 2, 3, 5, 7, 8, 10]      # Data X
y = [3, 5, 7, 11, 14, 15, 19]   # Data y
print x[1]
# 1st, find Averages
X = float(sum (x))/len(x) # Average X-val
Y = float(sum (y))/len(y) # Average Y-val
print X
print Y

# 2nd, Find the Slope of the line
# sum of (xi - X)(yi - Y) over the sum of (xi - X) squared
mTop = 0
mBottom = 0
for i in xrange(len(x)):
    mTop += (x[i] - X)*(y[i] - Y)
    mBottom += math.pow(x[i] - X, 2)

M = mTop/mBottom

print "Slope: %f" % M

# 3rd, Calculate the y-intercept
# Y = MX + B which means B = Y - MX
B = Y - M*X

print "y = %.2fx + %.2f" % (M, B)

# Finally preform minimization