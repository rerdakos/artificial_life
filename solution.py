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
        f.close()

        os.system("del fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        self.links_with_sensors = []

        xdim = random.uniform(0.1, 1)*2
        ydim = random.uniform(0.1, 1)*2
        zdim = random.uniform(0.1, 1)*2

        color0 = random.choice(["Blue", "Green"])

        if color0 == "Blue":
            colorString0 = "0 0.0 1.0 1.0"
        else:
            colorString0 = "0 1.0 0.0 1.0"

        pyrosim.Send_Cube(name="0", pos=[0,0,1] , size=[xdim,ydim,zdim], color = color0, colorString = colorString0)

        if color0 == "Green":
             self.links_with_sensors.append(0)

        pyrosim.Send_Joint(name = "0_1" , parent= "0" , child = "1" , type = "revolute", position = [0,ydim/2,1], jointAxis = "1 0 0")


        for link in range(c.numLinks):
            
            xdim2 = random.uniform(0.1, 1)*2
            ydim2 = random.uniform(0.1, 1)*2
            zdim2 = random.uniform(0.1, 1)*2

            color1 = random.choice(["Blue", "Green"])

            if color1 == "Blue":
                colorString1 = "0 0.0 1.0 1.0"
            else:
                colorString1 = "0 1.0 0.0 1.0"

            if color1 == "Green":
                self.links_with_sensors.append(link+1)


            position1 = random.choice([[xdim2,0,0], [-xdim2,0,0], [0,ydim2,0], [0,-ydim2,0]])
            
            if position1 == [xdim2,0,0] or position1 == [xdim2,0,0]:
                axis = "0 1 0"
            else:
                axis = "1 0 0"

            pyrosim.Send_Cube(name=str(link+1), pos=position1 , size=[xdim2,ydim2,zdim2], color=color1, colorString = colorString1 )
            
            if link < c.numLinks-1:

                pyrosim.Send_Joint(name = str(link+1)+ "_" +str(link+2) , parent = str(link+1) , child = str(link+2) , type = "revolute", position = position1, jointAxis = axis)
                
        pyrosim.End()



    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        j = 0

        numSensors = len(self.links_with_sensors)

        for link in self.links_with_sensors:
            
            pyrosim.Send_Sensor_Neuron(name = j , linkName = str(link))
            j += 1

        for link in range(c.numLinks):
            pyrosim.Send_Motor_Neuron( name = link + numSensors , jointName = str(link) + "_" + str(link+1))

        for currentRow in range(numSensors):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensors , weight = self.weights[currentRow][currentColumn]  )

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self,id):
        self.myID = id
