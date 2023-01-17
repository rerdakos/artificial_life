import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

from sensor import SENSOR
from motor import MOTOR


class ROBOT:


    def __init__(self): 
        k = 1
        self.sensor = SENSOR(k)
        self.motor = MOTOR()
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)      
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        
    def Sense(self,i):
        for name in self.sensors:
            self.sensor.Get_Value(i,name)
            

 
        
            
        

    
        