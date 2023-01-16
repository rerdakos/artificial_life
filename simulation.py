from http.client import OK
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
               
        self.world = WORLD()
        self.robot = ROBOT()

    def Run():
        t = 1000

        for i in range(t):
            p.stepSimulation()

        #    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


        #    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_BackLeg", 
        #    controlMode = p.POSITION_CONTROL, targetPosition = bl_targetAngles[i], maxForce = 100)

        #    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_FrontLeg", 
        #    controlMode = p.POSITION_CONTROL, targetPosition = fl_targetAngles[i], maxForce = 100)
   
            time.sleep(1/60)
            print(i)
        p.disconnect()
