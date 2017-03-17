from pulp import *
import pandas as pd
import matplotlib
matplotlib.use("qt4agg")
import matplotlib.pyplot as plt
import math


tups = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]

prob = LpProblem("min abs dev", LpMinimize)
a  = LpVariable("a")
b  = LpVariable("b")
y  = LpVariable("y")
x  = LpVariable("x")
prob += x


print prob

temp =0

for i in range(0, len(tups)):
	temp = a*(tups[i][0]) + b - tups[i][1]

	prob += x >= temp
	prob += x >= -temp


print prob

status = prob.solve()
print value(prob.objective)
print value(a)



