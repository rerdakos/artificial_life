import numpy as np

t = 1000
numberOfGenerations = 1
populationSize = 1

numLinks = 3 # Not including the initial one
numSensorNeurons = numLinks+1
numMotorNeurons = numLinks

motorJointRange = 0.2

amplitude = np.pi/4
frequency = 10
offset = 0

bl_amplitude = np.pi/4
bl_frequency = 10
bl_phaseOffset = 0

fl_amplitude = np.pi/4
fl_frequency = 10
fl_phaseOffset = np.pi/2