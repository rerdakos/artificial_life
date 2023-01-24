from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0

        for key in range(c.populationSize):
            self.parents[key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1



    def Evolve(self):
        for key in range(c.populationSize):
            self.parents[key].Start_Simulation("DIRECT")

        for key in range(c.populationSize):           
            self.parents[key].Wait_For_Simulation_To_End()
        #self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        pass
        #self.Spawn()
        #self.Mutate()
        #self.child.Evaluate("DIRECT")
        #self.Print()
        #self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
        print(self.children)
        #self.child = copy.deepcopy(self.parents)
        


    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness,self.child.fitness)

    def Show_Best(self):
        pass
        #os.system("python simulate.py GUI")
