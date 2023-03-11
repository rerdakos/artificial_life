import numpy as np
import matplotlib.pyplot as plt
import constants as c
import pandas as pd

with open('fittemp.txt') as f:
    all_fitnesses = f.read()
    print(all_fitnesses)


rawfit = np.zeros(c.populationSize*(c.numberOfGenerations+1))
rawint = np.zeros(c.populationSize*(c.numberOfGenerations+1))


for i in range(c.populationSize*(c.numberOfGenerations+1)):

    print(all_fitnesses[23*i:2+23*i])
    rawfit[i] = all_fitnesses[2+23*i:21+23*i]
    rawint[i] = all_fitnesses[23*i:2+23*i]

print(rawfit)
print(rawint)


xy = pd.DataFrame({'x': rawint, 'y': rawfit})
xy.sort_values('x', inplace=True)

print(xy['x'])
