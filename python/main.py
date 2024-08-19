import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import math
import time

x_data = []
y_data = []
z_data = []

def update_graph():
    global x_data, y_data, z_data
    x_array = np.array(x_data)
    y_array = np.array(y_data)
    z_array = np.array(z_data)

    grid_x, grid_y = np.mgrid[min(x_array):max(x_array):100j, min(y_array):max(y_array):100j]
    grid_z = griddata((x_array, y_array), z_array, (grid_x, grid_y), method='nearest')

    ax.clear()
    ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.draw()
    plt.pause(0.1)

if __name__ == "__main__":
    file_path = 'data.txt'
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    try:
        plt.ion()
        plt.show()
        while True:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    z, x, y = map(int, line.strip().split(','))
                    z = (math.sin(90 - z)) * y
                    z_data.append(z)
                    x_data.append(x)
                    y = (math.cos(z)) * y
                    y_data.append(y)
                update_graph()
            time.sleep(5)
    except KeyboardInterrupt:
        pass