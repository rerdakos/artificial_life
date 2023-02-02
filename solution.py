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
    
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        pyrosim.Send_Joint( name = "Torso_B1" , parent= "Torso" , child = "B1" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="B1", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_F1" , parent= "Torso" , child = "F1" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="F1", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "B1_LB1" , parent= "B1" , child = "LB1" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LB1", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "F1_LF1" , parent= "F1" , child = "LF1" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LF1", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LB1")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LF1")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_B1")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_F1")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "B1_LB1")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "F1_LF1")


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
