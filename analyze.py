import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\backLegSensorValues.npy')
frontLegSensorValues = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)
plt.plot(frontLegSensorValues, label="Front Leg")

#print(backLegSensorValues)
#print(frontLegSensorValues)

plt.legend()
plt.show()