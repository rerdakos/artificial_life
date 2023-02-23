import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

class SOLUTION:
    
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID       

        self.torso = [random.uniform(1.5, 1.8), random.uniform(0.5, 1.5), random.uniform(0.2, 0.5)]

        self.limb1 = np.zeros((4, 3))
        self.limb2 = np.zeros((4, 3))

        for i in range(4):
            self.limb1[i,0] = random.uniform(0.1, 0.5)
            self.limb1[i,1] = random.uniform(0.1, 0.5)
            self.limb1[i,2] = 0.9

            self.limb2[i,0] = random.uniform(0.4, 0.6)
            self.limb2[i,1] = self.limb1[i,1]
            self.limb2[i,2] = 0.1

        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)

        self.weights = 2*self.weights - 1

        self.decision = np.zeros((4, 2))

        for ii in range(4):
            for jj in range(2):
                self.decision[ii,jj] = random.choice([1, 0])

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
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        self.links_with_sensors = []
        self.joint_names = []

        xdim0 = self.torso[0] 
        ydim0 = self.torso[1]
        zdim0 = self.torso[2]
        zoff = 0.8

        color0 = random.choice(["Blue", "Green"])

        if color0 == "Blue":
            colorString0 = "0 0.0 1.0 1.0"
        else:
            colorString0 = "0 1.0 0.0 1.0"

        if color0 == "Green":
             self.links_with_sensors.append(0)

        pyrosim.Send_Cube(name="0", pos=[0,0,zdim0/2+zoff] , size=[xdim0,ydim0,zdim0], color = color0, colorString = colorString0)
        
        pyrosim.Send_Joint(name = "0_" + "Head" , parent= "0" , child = "Head" , type = "revolute", position = [-xdim0/2,0,zdim0/2+zoff], jointAxis = "0 1 0")
        
        xHead = xdim0/4
        yHead = ydim0/2
        zHead = zdim0
        
        pyrosim.Send_Cube(name="Head", pos=[-xHead*0.25,0,zHead] , size=[xHead,yHead,zHead], color = "Blue", colorString = "0.0 0.0 1.0 1.0")


        for node in range(c.nodes):

            position0 = [[xdim0/3,ydim0/2,zdim0/2+zoff], [-xdim0/3,ydim0/2,zdim0/2+zoff], [-xdim0/3,-ydim0/2,zdim0/2+zoff], [xdim0/3,-ydim0/2,zdim0/2+zoff]]

            if self.decision[node,0] == 1:

                pyrosim.Send_Joint(name = "0_" + str(node+1) , parent= "0" , child = str(node+1) , type = "revolute", position = position0[node], jointAxis = "0 1 0")
                self.joint_names.append("0_" + str(node+1))

                        
                xdim1 = self.limb1[node,0]
                ydim1 = self.limb1[node,1]
                zdim1 = self.limb1[node,2]
        
                xdim2 = self.limb2[node,0]
                ydim2 = self.limb2[node,1]
                zdim2 = self.limb2[node,2] 

                position1 = [[0,ydim1/2,-zdim1/2], [0,ydim1/2,-zdim1/2], [0,-ydim1/2,-zdim1/2], [0,-ydim1/2,-zdim1/2]]

                color1 = random.choice(["Green", "Green"])

                if color1 == "Blue":
                    colorString1 = "0 0.0 1.0 1.0"
                else:
                    colorString1 = "0 1.0 0.0 1.0"

                if color1 == "Green":
                    self.links_with_sensors.append(node+1)

                pyrosim.Send_Cube(name=str(node+1), pos=position1[node] , size=[xdim1,ydim1,zdim1], color=color1, colorString = colorString1 )

                if self.decision[node,1] == 1:
            
                    position2 = [[-xdim1/2,ydim1/2,-zdim1], [-xdim1/2,ydim1/2,-zdim1], [-xdim1/2,-ydim1/2,-zdim1], [-xdim1/2,-ydim1/2,-zdim1]]

                    pyrosim.Send_Joint(name = str(node+1)+ "_" +str(node+11) , parent = str(node+1) , child = str(node+11) , type = "revolute", position = position2[node], jointAxis = "0 1 0")
                    self.joint_names.append(str(node+1)+ "_" +str(node+11))

                    position3 = [[-xdim2/2,0,0], [-xdim2/2,0,0], [-xdim2/2,0,0], [-xdim2/2,0,0]]

                    color2 = random.choice(["Green", "Green"])

                    if color2 == "Blue":
                        colorString2 = "0 0.0 1.0 1.0"
                    else:
                        colorString2 = "0 1.0 0.0 1.0"

                    if color2 == "Green":
                        self.links_with_sensors.append(node+11)

                    pyrosim.Send_Cube(name=str(node+11), pos=position3[node] , size=[xdim2,ydim2,zdim2], color=color2, colorString = colorString2 )
                else:
                    pass
            else:
                pass

        pyrosim.End()



    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        j = 0

        self.numSensors = len(self.links_with_sensors)
        self.numMotors = len(self.joint_names)

        for link in self.links_with_sensors:
            
            pyrosim.Send_Sensor_Neuron(name = j , linkName = str(link))
            j += 1
        
        j = 0
        for joint in self.joint_names:
            pyrosim.Send_Motor_Neuron( name = j + self.numSensors , jointName = joint)
            j += 1

        for currentRow in range(self.numSensors):
            for currentColumn in range(self.numMotors):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+self.numSensors , weight = self.weights[currentRow][currentColumn]  )
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,self.numSensors-1)
        randomColumn = random.randint(0,self.numMotors-1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

        decisionCol = random.randint(0,3)
        decisionRow = random.randint(0,1)

        self.decision[decisionCol,decisionRow] = random.randint(0,1)

    def Set_ID(self,id):
        self.myID = id
