import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy as np

class MOTOR:
    def __init__(self,jointName):      
        self.jointName = jointName
        #self.robotId = p.loadURDF("body.urdf")
        self.Prepare_To_Act2()

    def Prepare_To_Act2(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        xvals = np.linspace(0, 2*np.pi, c.t)
        self.motorValues = self.amplitude*np.sin(self.frequency*xvals + self.offset)    

    def Set_Value(self,i,name,robotId):
        pass

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = name, 
        controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[i], maxForce = 100)