import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        
        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
               
        self.world = WORLD()
        self.robot = ROBOT()       

    def Run(self):       
        for i in range(c.t):
            p.stepSimulation()
            
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            
            #time.sleep(1/1000)
            #print(i)
        
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()