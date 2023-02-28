import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self,linkName):       
        self.linkName = linkName
        self.values = np.zeros(c.t)
        
        #self.storefit = np.zeros(c.populationSize*(c.numberOfGenerations+1))

    def Get_Value(self,i,name):     
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(name)


    def Save_Fitness(self,solutionId,value):
        pass
        #print(self.storefit,solutionId,value)
        #self.storefit[int(solutionId)] = value
        '''
        f = open("fittemp3.txt", "a")
        f.write(str(int(solutionId)) + " " + str(value) + " " + "\n")
        f.close()
        '''
        #np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\FitnessValues2.npy',self.storefit)

    def Save_Values(self):
        pass
        np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\FitnessValues2.npy',self.storefit)
    
        