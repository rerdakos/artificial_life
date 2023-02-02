import numpy as np

t = 150
numberOfGenerations = 10
populationSize = 10

numLegPairs = 10

numSensorNeurons = 1 + numLegPairs*2
numMotorNeurons = numLegPairs*4

motorJointRange = 1

amplitude = np.pi/4
frequency = 10
offset = 0

bl_amplitude = np.pi/4
bl_frequency = 10
bl_phaseOffset = 0

fl_amplitude = np.pi/4
fl_frequency = 10
fl_phaseOffset = np.pi/2