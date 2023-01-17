import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

from sensor import SENSOR
from motor import MOTOR


class ROBOT:


    def __init__(self):        
        self.motors = MOTOR()
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)

    def Prepare_To_Sense(self):        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        
    def Sense(self,t):
        for t in self.sensors:
            SENSOR.Get_Value(self,i,t)
            

 
        
            
        

    
        