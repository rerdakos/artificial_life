import numpy as np
import random

t = 1000
numberOfGenerations = 10
populationSize = 1

nodes = 4
limbs = 2
numLinks = 0 #random.randint(1, 6)  Not including the initial one
numSensorNeurons = nodes*2+1
numMotorNeurons = nodes*2

motorJointRange = 0.5
