import numpy as np
import random

t = 500
numberOfGenerations = 1
populationSize = 1

numLinks = 5 #random.randint(1, 6)  Not including the initial one
numSensorNeurons = numLinks+1
numMotorNeurons = numLinks

motorJointRange = 0.5
