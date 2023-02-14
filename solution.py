import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

class SOLUTION:
    
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID

        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)

        self.weights = 2*self.weights - 1

    def Evaluate(self,method):
        pass
 
    def Start_Simulation(self,method):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system("start /B python simulate.py " + method + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.1)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        
        xdim = random.uniform(0.1, 1)*3
        ydim = random.uniform(0.1, 1)*3
        zdim = random.uniform(0.1, 1)*3

        pyrosim.Send_Cube(name="0", pos=[0,0,2] , size=[xdim,ydim,zdim])
        pyrosim.Send_Joint(name = "0_1" , parent= "0" , child = "1" , type = "revolute", position = [0,ydim/2,2], jointAxis = "1 0 0")


        for link in range(c.numLinks):
            
            xdim2 = random.uniform(0.1, 1)*3
            ydim2 = random.uniform(0.1, 1)*3
            zdim2 = random.uniform(0.1, 1)*3

            pyrosim.Send_Cube(name=str(link+1), pos=[0,ydim2/2,0] , size=[xdim2,ydim2,zdim2])

            if link < c.numLinks-1:

                pyrosim.Send_Joint(name = str(link+1)+ "_" +str(link+2) , parent = str(link+1) , child = str(link+2) , type = "revolute", position = [0,ydim2,0], jointAxis = "1 0 0")


        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    
        for link in range(c.numLinks+1):
            pyrosim.Send_Sensor_Neuron(name = link , linkName = str(link))

        for link in range(c.numLinks):
            pyrosim.Send_Motor_Neuron( name = link + c.numLinks + 1 , jointName = str(link) + "_" + str(link+1))

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn]  )

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self,id):
        self.myID = id
