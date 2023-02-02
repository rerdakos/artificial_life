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
    
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        l = 1
        
        xp = [0]*c.numLegPairs
        for num in range(c.numLegPairs):
            xp[num] = (num+1)/(c.numLegPairs+1) - 0.5
        

        for num in range(c.numLegPairs):

            pyrosim.Send_Joint( name = "Torso_B" + str(l) , parent= "Torso" , child = "B" + str(l) , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="B" + str(l), pos=[xp[num],-0.5,0] , size=[0.2,1,0.2])

            pyrosim.Send_Joint( name = "B" + str(l) + "_LB" + str(l) , parent= "B" + str(l) , child = "LB" + str(l) , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LB" + str(l), pos=[xp[num],0,-0.5] , size=[0.2,0.2,1])

            pyrosim.Send_Joint( name = "Torso_F" + str(l) , parent= "Torso" , child = "F" + str(l) , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="F" + str(l), pos=[xp[num],0.5,0] , size=[0.2,1,0.2])

            pyrosim.Send_Joint( name = "F" + str(l) + "_LF" + str(l) , parent= "F" + str(l) , child = "LF" + str(l) , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LF" + str(l), pos=[xp[num],0,-0.5] , size=[0.2,0.2,1])

 
            l += 1
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        j = 1
        k = c.numSensorNeurons
        for l in range(c.numLegPairs):
            l += 1

            pyrosim.Send_Sensor_Neuron(name = j , linkName = "LB" + str(l))
            j += 1
            pyrosim.Send_Sensor_Neuron(name = j , linkName = "LF" + str(l))
            j += 1

            pyrosim.Send_Motor_Neuron( name = k , jointName = "Torso_B" + str(l))
            k += 1
            pyrosim.Send_Motor_Neuron( name = k , jointName = "Torso_F" + str(l))
            k += 1
            pyrosim.Send_Motor_Neuron( name = k , jointName = "B" + str(l) + "_LB" + str(l))
            k += 1
            pyrosim.Send_Motor_Neuron( name = k , jointName = "F" + str(l) + "_LF" + str(l))
            k += 1

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
