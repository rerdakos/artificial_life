import pybullet as p
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def Prepare_To_Sense(self):
        self.sensors = SENSOR(self)
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)

    def __init__(self):        
        self.motors = MOTOR()
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        

    
        