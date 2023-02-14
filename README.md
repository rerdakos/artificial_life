# Robin Erdakos - Artifical Life at Northwestern
# Assignment 6 - Randomized Snake

## Running the code

Follow instructions on r/ludobots to install python, pybullet and pyrosim, create a repository and change your directory accordingly.
https://www.reddit.com/r/ludobots/wiki/installation/

## Goal

Our goal is to generate a kinematic chain (a jointed, motorized, innervated, sensorized snake) 
with a random number of randomly shaped links with random sensor placement along the chain. Finally, the links with and without sensors should be colored green and blue, respectively.
I will describe how I achieved each aspect of this goal below.

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