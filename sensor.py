import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):       
        self.linkName = linkName
        self.values = np.zeros(c.t)

    def Get_Value(self,i,name):     
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(name)
        #if i == (c.t - 1):
        #    print(self.values)

       
        