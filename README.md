# Robin Erdakos - Artifical Life at Northwestern
# Assignment 8 - Parallel Crawler

## Running the code

Follow instructions on r/ludobots to install python, pybullet and pyrosim, create a repository and change your directory accordingly.
https://www.reddit.com/r/ludobots/wiki/installation/

From this repository, open search.py to run the simulations and use constants.py to change parameters such as time, popualtion size and number of generations.

## Goal



## Crawler Body

# Genotype

Below is a diagram of the design of our creatures genotype, this is how the bodies are generated.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/Genotype_.jpg?raw=true)

# Phenotype

Now we see how these bodies may look in actual physical space, correspoding to the genotype above. Also, we can see possible bodies
that may be randomly generated in a population.

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/Phenotype_.jpg?raw=true)

![alt text](https://github.com/rerdakos/artificial_life/blob/Final/bodies_.jpg?raw=true)

## Complex Body Plan

Below is the full body plan for our randomized creature. As you can see below, the torso has 4 node locations where joints can be placed, which lead to a 
first limb which each also has a node for another joint and second limb. When the body generates, we loop over these node locations and there is a random
choice to either place a limb or skip to the next node. This random choice is done for both limbs, so we get some creatures with no limb, 1 limb or 2 limbs 
at each of the nodes. Each of these links have randomly generated sizes and random sensor placement/colors. All sensors connect to all motors.

For evolution, motor values are randomly changed as done previously, but now upon each mutation we make a random change to the body plan that determines the
limb placement.




## Fitness Tracker

![alt text](https://github.com/rerdakos/artificial_life/blob/Assignment8/Fitness5.jpg?raw=true)

### The rest is the same as last Assignment
### Random number of links
This is done simply by setting a variable to be random.randint(1, 9), which chooses a random number between 1 and 9 for the number of links we want in our chain.

### Randomly shaped
This is achieved by setting each of the links dimensions (x,y,z) to be random.uniform(0.1, 1)*2 which chooses a random number between ~0 (0.1 because we can't have a dimension of 0)
and multiplies it by 2 so we get larger cubes for display purpsoses. This is done over an iterative loop that generates a new link with new dimensions,
as well as a joint in the appropriate position for each iteration of the loop.

### Random sensor placement + color
For this part, I used the random.choice() function to choose between 2 color values, blue or green, which would create the cube corresponing to having no sensor
or having a sensor, respectively. For a chosen color, a correponding colorString is chosen, and those values are passed down as arguments into Send_Cube().
These arguments end up in material.py and give each link the randomly chosen color. As the colors are being decided, the name of each green link is saved and once the brain is generates,
those links are given sensors, and the neural network connects the appropriate sensors to each motor.