from simulation import SIMULATION

simulation = SIMULATION()
SIMULATION.Run()


#import pybullet as p
#import time
#import pybullet_data
#import pyrosim.pyrosim as pyrosim
#import numpy as np
#import random
#import constants as c

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.setGravity(0,0,-9.8)

#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")

#p.loadSDF("world.sdf")

#pyrosim.Prepare_To_Simulate(robotId)

#t = 1000 #number of iterations

#backLegSensorValues = np.zeros(t)
#frontLegSensorValues = np.zeros(t)

#xvals = np.linspace(0, 2*np.pi, t)

#bl_targetAngles = c.bl_amplitude*np.sin(c.bl_frequency*xvals + c.bl_phaseOffset)

#fl_targetAngles = c.fl_amplitude*np.sin(c.fl_frequency*xvals + c.fl_phaseOffset)

#np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\bl_targetAngles.npy',bl_targetAngles)
#np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\fl_targetAngles.npy',fl_targetAngles)


#for i in range(t):
#    p.stepSimulation()

#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_BackLeg", 
#    controlMode = p.POSITION_CONTROL, targetPosition = bl_targetAngles[i], maxForce = 100)

#    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_FrontLeg", 
#    controlMode = p.POSITION_CONTROL, targetPosition = fl_targetAngles[i], maxForce = 100)
   
#    time.sleep(1/60)
    #print(i)
#p.disconnect()

#np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\backLegSensorValues.npy',backLegSensorValues)
#np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\frontLegSensorValues.npy',frontLegSensorValues)

#print(backLegSensorValues)
#print(frontLegSensorValues)
