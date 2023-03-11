import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):       
        self.linkName = linkName
        self.values = np.zeros(c.t)

    def Get_Value(self,i,name):     
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(name)

    def Save_Fitness(self,solutionId,value):
        # Remove pass and apostrophes to save fitness values 
        pass

        '''
        f = open("fittemp4.txt", "a")
        f.write(str(int(solutionId)) + " " + str(value) + " " + "\n")
        f.close()
        '''

    def Save_Values(self):
        pass
    
        