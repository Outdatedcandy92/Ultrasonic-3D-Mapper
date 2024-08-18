import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from scipy.interpolate import griddata


x_data = []
y_data = []
z_data = []


with open('data.txt', 'r') as file:
    for line in file:
        z, x, y = map(int, line.strip().split(','))
        z_data.append(-z)
        x_data.append(x)
        y = (math.cos(z)) * y
        y_data.append(y)



x_data = np.array(x_data)
y_data = np.array(y_data)
z_data = np.array(z_data)


print("X Data:", x_data)
print("Y Data:", y_data)
print("Z Data:", z_data)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x_data, y_data, z_data, c='r', marker='o')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()