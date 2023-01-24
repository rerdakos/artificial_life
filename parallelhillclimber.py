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
        self.Evaluate(self.parents)
        
        #self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
   
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        
        self.Print()
        #self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()
        
            #self.child.Mutate()

    def Evaluate(self,solutions):
        for key in range(c.populationSize):
            solutions[key].Start_Simulation("DIRECT")

        for key in range(c.populationSize):           
            solutions[key].Wait_For_Simulation_To_End()


    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("")
        for key in self.parents:
            print(self.parents[key].fitness,self.children[key].fitness)
        print("")
    def Show_Best(self):
        pass
        #os.system("python simulate.py GUI")
