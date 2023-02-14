import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER

#os.system("python simulate.py GUI 0")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
#phc.Show_Best()
