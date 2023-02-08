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

        pyrosim.Send_Cube(name="Torso", pos=[0,0,zdim/2] , size=[xdim,ydim,zdim])

        xdim2 = random.uniform(0.1, 1)*3
        ydim2 = random.uniform(0.1, 1)*3
        zdim2 = random.uniform(0.1, 1)*3

        pyrosim.Send_Joint( name = "Torso_BL" , parent= "Torso" , child = "BL" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BL", pos=[0,-ydim/2 -ydim2/2,0] , size=[xdim2,ydim2,zdim2])

        """
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "BL_LowerBackLeg" , parent= "BL" , child = "LowerBackLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        """

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BL")
        #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerBackLeg")
        #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerFrontLeg")
        #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftLeg")
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerRightLeg")

        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Torso_BL")
        #pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        #pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        #pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        #pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BL_LowerBackLeg")
        #pyrosim.Send_Motor_Neuron( name = 9 , jointName = "FrontLeg_LowerFrontLeg")
        #pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LowerLeftLeg")
        #pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_LowerRightLeg")

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
