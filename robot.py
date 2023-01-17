import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self): 
        
        self.sensor = SENSOR(self)
        self.motor = MOTOR(self)
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)      
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        
    def Sense(self,i):
        for name in self.sensors:
            self.sensor.Get_Value(i,name)

    def Prepare_To_Act(self):        
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,i):
        for name in self.motors:
            self.motor.Set_Value(i,name,self.robotId)
            

 
        
            
        

    
        