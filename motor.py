import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy as np

class MOTOR:
    def __init__(self,jointName):      
        self.jointName = jointName

    def Set_Value(self,desiredAngle,jointName,robotId):
        if jointName == 'Torso_FrontLeg':
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = jointName.encode('utf-8'), 
            controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 100)
        if jointName == 'Torso_BackLeg':
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = jointName.encode('utf-8'), 
            controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 100)
