import numpy as np
import random

t = 1000
numberOfGenerations = 1
populationSize = 5
nodes = 4
limbs = 2
numLinks = 0 #random.randint(1, 6)  Not including the initial one
numSensorNeurons = nodes*2
numMotorNeurons = nodes*2

motorJointRange = 0.2
