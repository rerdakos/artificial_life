import numpy as np
import random

t = 200
numberOfGenerations = 1
populationSize = 1

numLinks = random.randint(1, 9) # Not including the initial one
numSensorNeurons = numLinks+1
numMotorNeurons = numLinks

motorJointRange = 0.5
