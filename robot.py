import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import os

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:

    def __init__(self,solutionID): 
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        self.sensor = SENSOR(self)
        self.motor = MOTOR(self)
        self.robotId = p.loadURDF("body" + str(self.solutionID) + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)      
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + str(self.solutionID) + ".nndf")
        os.system("del body" + str(self.solutionID) + ".urdf")


    def Prepare_To_Sense(self):        
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        
    def Sense(self,i):
        for name in self.sensors:
            self.sensor.Get_Value(i,name)

    def Prepare_To_Act(self):        
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange

                self.motor.Set_Value(desiredAngle,jointName,self.robotId)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self,solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        f = open("tmp" + str(solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")

        exit()


 
        
            
        

    
        