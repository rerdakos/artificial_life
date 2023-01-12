import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

t = 100 #number of iterations
backLegSensorValues = np.zeros(t)
frontLegSensorValues = np.zeros(t)


for i in range(t):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #print(backLegTouch)
    #print(frontLegTouch)

    time.sleep(1/60)
    #print(i)
p.disconnect()

np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\backLegSensorValues.npy',backLegSensorValues)
np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\frontLegSensorValues.npy',frontLegSensorValues)

#print(backLegSensorValues)
#print(frontLegSensorValues)
