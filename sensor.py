import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):       
        self.linkName = linkName
        self.values = np.zeros(c.t)
        print(type(self.values))

    def Get_Value(self,linkName,i):
        #self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)
        print(SENSOR.linkName)

        print(linkName,i)
        print(pyrosim.Get_Touch_Sensor_Value_For_Link(linkName))

       
        