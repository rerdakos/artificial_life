import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):       
        self.linkName = linkName
        self.values = np.zeros(c.t)
        print(self.values)
 

    def Get_Value(self,i,t):
        #print(self.values)
        pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        print(i,t)

       
        