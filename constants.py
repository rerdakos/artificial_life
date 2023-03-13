import numpy as np
import random

# VARIABLES TO CHANGE
t = 1000 # Time for each simulation

numberOfGenerations = 10 # Number of Generations
populationSize = 3 # Size of Population

motorJointRange = 0.2 # Range for motors

# CONSTANT PARAMETERS
nodes = 4 # Number of node locations for limb generation
numSensorNeurons = nodes*2 # Number of possible sensor locations
numMotorNeurons = nodes*2 # Number of possible motor locations


