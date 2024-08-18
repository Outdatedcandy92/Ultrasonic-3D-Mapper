import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import math


x_data = []
y_data = []
z_data = []


with open('data.txt', 'r') as file:
    for line in file:
        z, x, y = map(int, line.strip().split(','))
        z = (math.sin(90-z)) * y
        z_data.append(z)
        x_data.append(x)
        y = (math.cos(z)) * y
        y_data.append(y)


x_data = np.array(x_data)
y_data = np.array(y_data)
z_data = np.array(z_data)


print("X Data:", x_data)
print("Y Data:", y_data)
print("Z Data:", z_data)


print("Z Data Range:", np.min(z_data), np.max(z_data))

grid_x, grid_y = np.mgrid[min(x_data):max(x_data):100j, min(y_data):max(y_data):100j]


grid_z = griddata((x_data, y_data), z_data, (grid_x, grid_y), method='nearest')


print("Interpolated Z Data Range:", np.min(grid_z), np.max(grid_z))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()