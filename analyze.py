import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\backLegSensorValues.npy')
frontLegSensorValues = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\frontLegSensorValues.npy')

bl_targetAngles = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\bl_targetAngles.npy')
fl_targetAngles = np.load(r'C:\Users\robme\OneDrive\Desktop\Artificial Life\data\fl_targetAngles.npy')

plt.plot(bl_targetAngles,label="bl")
plt.plot(fl_targetAngles,label='fl')

#plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)
#plt.plot(frontLegSensorValues, label="Front Leg")

#print(backLegSensorValues)
#print(frontLegSensorValues)

plt.legend()
plt.show()