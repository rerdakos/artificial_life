import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self,directOrGUI,solutionID):
        
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID

        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
               
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)       

    def Run(self):       
        for i in range(c.t):
            p.stepSimulation()
            
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            
            if self.directOrGUI == "GUI":
                time.sleep(1/10000)

            #print(i)
        
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self,solutionID):
        pass
        #self.robot.Get_Fitness(solutionID)