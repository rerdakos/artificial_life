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
        self.joint_names = []

        xdim0 = random.uniform(1.5, 2.0)
        ydim0 = random.uniform(0.5, 1.5)
        zdim0 = random.uniform(0.2, 0.5)

        color0 = random.choice(["Blue", "Green"])

        if color0 == "Blue":
            colorString0 = "0 0.0 1.0 1.0"
        else:
            colorString0 = "0 1.0 0.0 1.0"

        if color0 == "Green":
             self.links_with_sensors.append(0)

        pyrosim.Send_Cube(name="0", pos=[0,0,zdim0/2] , size=[xdim0,ydim0,zdim0], color = color0, colorString = colorString0)
        
        pyrosim.Send_Joint(name = "0_" + "Head" , parent= "0" , child = "Head" , type = "revolute", position = [-xdim0/2,0,zdim0/2], jointAxis = "0 1 0")
        
        xHead = xdim0/4
        yHead = ydim0/2
        zHead = zdim0*0.75
        
        pyrosim.Send_Cube(name="Head", pos=[-xHead*0.25,0,zHead] , size=[xHead,yHead,zHead], color = "Cyan", colorString = "0.0 1.0 1.0 1.0")


        for node in range(c.nodes):

            position0 = [[xdim0/3,ydim0/2,zdim0/2], [-xdim0/3,ydim0/2,zdim0/2], [-xdim0/3,-ydim0/2,zdim0/2], [xdim0/3,-ydim0/2,zdim0/2]]

            decision0 = random.choice(["Yes", "No"]) #decide to create first limb

            if decision0 == "Yes":

                pyrosim.Send_Joint(name = "0_" + str(node+1) , parent= "0" , child = str(node+1) , type = "revolute", position = position0[node], jointAxis = "1 0 0")
                self.joint_names.append("0_" + str(node+1))

                xdim1 = random.uniform(0.1, 0.5)
                ydim1 = random.uniform(0.4, 0.8)
                zdim1 = random.uniform(0.05, 0.2)

                position1 = [[xdim1/2,ydim1/2,-zdim1/2], [-xdim1/2,ydim1/2,-zdim1/2], [-xdim1/2,-ydim1/2,-zdim1/2], [xdim1/2,-ydim1/2,-zdim1/2]]

                color1 = random.choice(["Blue", "Green"])

                if color1 == "Blue":
                    colorString1 = "0 0.0 1.0 1.0"
                else:
                    colorString1 = "0 1.0 0.0 1.0"

                if color1 == "Green":
                    self.links_with_sensors.append(node+1)

                pyrosim.Send_Cube(name=str(node+1), pos=position1[node] , size=[xdim1,ydim1,zdim1], color=color1, colorString = colorString1 )
            
                position2 = [[xdim1,ydim1,-zdim1/2], [0,ydim1,-zdim1/2], [0,-ydim1,-zdim1/2], [xdim1,-ydim1,-zdim1/2]]


                decision1 = random.choice(["Yes", "No"]) #decide to create second limb

                if decision1 == "Yes":

                    pyrosim.Send_Joint(name = str(node+1)+ "_" +str(node+11) , parent = str(node+1) , child = str(node+11) , type = "revolute", position = position2[node], jointAxis = "0 1 0")
                    self.joint_names.append(str(node+1)+ "_" +str(node+11))

                    xdim3 = random.uniform(0.3, 1)
                    ydim3 = random.uniform(0.1, 0.5)
                    zdim3 = 0.2

                    position3 = [[xdim3/2,-ydim3/2,-zdim3/2], [xdim3/2,-ydim3/2,-zdim3/2], [xdim3/2,ydim3/2,-zdim3/2], [xdim3/2,ydim3/2,-zdim3/2]]

                    color2 = random.choice(["Blue", "Green"])

                    if color2 == "Blue":
                        colorString2 = "0 0.0 1.0 1.0"
                    else:
                        colorString2 = "0 1.0 0.0 1.0"

                    if color2 == "Green":
                        self.links_with_sensors.append(node+11)

                    pyrosim.Send_Cube(name=str(node+11), pos=position3[node] , size=[xdim3,ydim3,zdim3], color=color2, colorString = colorString2 )
                else:
                    pass
            else:
                pass

        pyrosim.End()



    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        j = 0

        numSensors = len(self.links_with_sensors)
        numMotors = len(self.joint_names)

        for link in self.links_with_sensors:
            
            pyrosim.Send_Sensor_Neuron(name = j , linkName = str(link))
            j += 1
        
        j = 0
        for joint in self.joint_names:
            pyrosim.Send_Motor_Neuron( name = j + numSensors , jointName = joint)
            j += 1

        for currentRow in range(numSensors):
            for currentColumn in range(numMotors):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensors , weight = self.weights[currentRow][currentColumn]  )
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self,id):
        self.myID = id
