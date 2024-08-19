import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def read_data(file_path):
    x_data = []
    y_data = []
    z_data = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            z, x, y = map(float, line.strip().split(','))
            x_data.append(x)
            y_data.append(y)
            z_data.append(z)

    return np.array(x_data), np.array(y_data), np.array(z_data)

def plot_3d(x, y, z):
  
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    
    zi = griddata((x, y), z, (xi, yi), method='nearest')


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xi, yi, zi, cmap='viridis')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

if __name__ == "__main__":
    file_path = 'data.txt'
    x, y, z = read_data(file_path)
    plot_3d(x, y, z)