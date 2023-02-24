import numpy as np
import matplotlib.pyplot as plt

#FitnessValues1 = np.load(r'C:\Users\robme\OneDrive\Documents\GitHub\artificial_life/FitnessValues.npy')
FitnessValues = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\FitnessValues2.npy')

#np.save(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\FitnessValues.npy',xCoordinateOfLinkZero)
#np.save(r'C:\Users\robme\OneDrive\Documents\GitHub\artificial_life/FitnessValues.npy',xCoordinateOfLinkZero)

print(FitnessValues)

plt.plot(FitnessValues,label="Fitness")

#plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)
#plt.plot(frontLegSensorValues, label="Front Leg")

#print(backLegSensorValues)
#print(frontLegSensorValues)

plt.legend()
plt.show()