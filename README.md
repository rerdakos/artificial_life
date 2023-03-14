# Robin Erdakos - Artifical Life at Northwestern 2023
# Final Project - Evolved 3D Crawler

## Running the code

In order to run the simulations for the virtual creatures, follow instructions on r/ludobots to install python, pybullet and pyrosim, 
create a repository and change your directory accordingly.

https://www.reddit.com/r/ludobots/wiki/installation/

From this repository, open search.py to run the simulations and use constants.py to change parameters such as time, popualtion size and number of generations.

## Goal

The goal for this project is to design a virtual organisms in 3D space that can evolve in order to better achieve a given task. My project involves a creature
that moves and crawls in a specified direction. The body and brain of the creature can mutate randomly with each generation, and a parallel hill climber 
strategy is used to find the best evolved creature in a population. Below I will disucss the details of the creature and how it mutates.

## Crawler Body

### Genotype

Below is a diagram of the design of our creatures genotype, this is how the bodies are generated.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/Genotype_.jpg?raw=true)

### Phenotype

Now we see how these bodies may look in actual physical space, corresponding to the genotype above. Also, we can see possible bodies
that may be randomly generated in a population.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/Phenotype_.jpg?raw=true)

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/bodies_.jpg?raw=true)

### Detailed Description of Body Plan

As seen in the phenotype diagram, the torso has 4 node locations where joints can be placed, which lead to a 
first limb which each also has a node for another joint and second limb. When the body generates, we loop over these node locations and there is a random
choice to either place a limb or skip to the next node. This random choice is done for both limbs. This results in us getting some creatures with no limbs, 1 limb or 2 limbs 
at any given nodes. Each of these limb links have randomly generated sizes and random sensor placement/colors.

## Crawler Brain

Each of the limbs may or may not have a sensor, decided by a random sensor placement that is generated with the body. Sensorized limbs trigger the motors
to activate, allowing for locomotion. Below is a diagram of potential sensor placement, and involves a map of how active sensors connect to motors.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/brain_.jpg?raw=true)

### Mutation and Evolution

Each creature in the population acts as a "parent", which has the initial randomly generated body and brain. If we have one or more generations, for 
each one a "child" is created, which is almost identical to the parent. When this child is made there is some slight mutation from the original parent, 
which in our project involves creating or removing a limb of the creature. Furthermore, the weights of motor synpases can randomly change with each mutation, 
giving the creature the chance to optimize its movement patterns.

Below is more information and figures on the selection process for the creatures, as well as an explanation of the parallel hill climber.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/selection_.jpg?raw=true)

## Tests and Results

For this final project I have run 
### Fitness Tracker

C:\Users\robme\OneDrive\Documents\GitHub\artificial_life\Fitness5.jpg

![alt text](https://github.com/rerdakos/artificial_life/blob/Fitness5.jpg?raw=true)
