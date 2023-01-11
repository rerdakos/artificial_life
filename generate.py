from operator import length_hint
from re import X
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5*height


for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    z += 0.5*height
    length = 0.9*length
    width = 0.9*width
    height = 0.9*height
    z += 0.5*height
    

pyrosim.End()