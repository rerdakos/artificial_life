import numpy as np
import random

t = 1000 # Time for each simulation

numberOfGenerations = 0 # Number of Generations
populationSize = 1 # Size of Population

nodes = 4 # Number of node locations for limb generation
numSensorNeurons = nodes*2 # Number of possible sensor locations
numMotorNeurons = nodes*2 # Number of possible motor locations

motorJointRange = 0.2 # Range for motors
