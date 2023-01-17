import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy as np

class MOTOR:
    def __init__(self,jointName):      
        self.jointName = jointName
        #self.robotId = p.loadURDF("body.urdf")
        self.Prepare_To_Act2(jointName)

    def Prepare_To_Act2(self,jointName):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset
        xvals = np.linspace(0, 2*np.pi, c.t)

        self.motorValues = self.amplitude*np.sin(self.frequency*xvals + self.offset)
        self.motorValues2 = self.amplitude*np.sin(self.frequency*0.5*xvals + self.offset)

    def Set_Value(self,i,name,robotId):
        if name == b'Torso_FrontLeg':
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = name, 
            controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[i], maxForce = 100)
        if name == b'Torso_BackLeg':
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = name, 
            controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues2[i], maxForce = 100)


 
    def Save_Values(self):
        np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\MotorValues.npy',self.motorValues)