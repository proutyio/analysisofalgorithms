from pulp import *
import pandas as pd
import matplotlib
matplotlib.use("qt4agg")
import matplotlib.pyplot as plt
import math

#####
##Read in Corvallis.csv file and convert it into a table
#####
weatherDF = pd.read_table("Corvallis.csv", sep=";")
weatherDF.drop('STATION', axis=1, inplace=True)

# make dataframe
pd.DataFrame(weatherDF)

# list for x and y coordinates
x_vals = weatherDF['day.1'].tolist()
y_vals = weatherDF['average'].tolist()

# check list values for correctness
print "\nValue of x_vals list:"
print x_vals
print "\nValue of y_vals list:"
print y_vals

# min and max for constraints
max_temp = max(y_vals)
min_temp = min(y_vals)
print "\nMax Temperature: %f\nMin Temperature: %f" %(max_temp,min_temp)
n = len(x_vals)
print "Length of n:%d" %(n)

# linear programming section
prob = LpProblem("min abs dev", LpMinimize)
x0 = LpVariable("x0")
x1 = LpVariable("x1")
x2 = LpVariable("x2")
x3 = LpVariable("x3")
x4 = LpVariable("x4")
x5 = LpVariable("x5")
Td = LpVariable("Tdvar")
prob += Td

#the different parts of the equation
lin=0
seas=0
sol=0

for i in range(0,n):
	lin = (x0 + x1 * x_vals[i])
	seas = (x2 * math.cos(2*math.pi * x_vals[i]/364.25) + x3 * math.sin(2*math.pi * x_vals[i]/364.25))
	sol = (x4 * math.cos(2*math.pi * x_vals[i]/(364.25*10.7)) + x5 * math.sin(2*math.pi*x_vals[i]/(364.25 * 10.7)))
	prob += Td >= (lin + seas + sol - y_vals[i])
	prob += Td >= -(lin + seas + sol - y_vals[i])

# solve and print output
status = prob.solve()
print "\n\nObjective of LP:%f" %(value(prob.objective))
print "Value of x0:%f" %(value(x0))
print "Value of x1:%f" %(value(x1))
print "Value of x2:%f" %(value(x2))
print "Value of x3:%f" %(value(x3))
print "Value of x4:%f" %(value(x4))
print "Value of x5:%f" %(value(x5))

# graphical output
bestFit = []
for i in range(22304):
	bestFit.append(value(x0)+value(x1)*x_vals[i]+value(x2)*math.cos(2*math.pi*x_vals[i]/364.25)+value(x3)*math.sin(2*math.pi*x_vals[i]/364.25)+value(x4)*math.cos(2*math.pi*x_vals[i]/(364.25*10.7))+value(x5)*math.sin(2*math.pi*x_vals[i]/(364.25 * 10.7)))

linear = []
for i in range(22304):
	linear.append(value(x0) + value(x1)*x_vals[i])

'''
# check contents
print "\nbestFit list contents:"
print bestFit
print "\nLinear list contents:"
print linear
'''

plt.plot(x_vals,y_vals, "bo", x_vals, bestFit, "r", x_vals, linear, "y", linewidth=5.0)
plt.axis([0,22304,min_temp,max_temp])
plt.show()

