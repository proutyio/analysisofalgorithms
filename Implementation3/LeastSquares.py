from pulp import *
import pandas as pd
import matplotlib
matplotlib.use("qt4agg")
import matplotlib.pyplot as plt
import numpy 
import math


pts = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]

prob = LpProblem("least squares", LpMinimize)
a  = LpVariable("a")
b  = LpVariable("b")
z  = LpVariable("z")
prob += z


for x,y in pts:
    prob += ( (a*x + b) - y <= z)
    prob += ( (a*x + b) - y >= -z)


status = prob.solve()
print "status:", LpStatus[status]
print "\n\nObjective of LP:%f" %(value(prob.objective))
print "a:", value(a)
print "b:", value(b)
print "z:", value(z)


#make graph
values = numpy.array(pts)
x = numpy.linspace(0, 11, 100)
y = value(a)*x + value(b)

plt.scatter(values[:,0], values[:,1])
plt.plot(x, y)
plt.show()



