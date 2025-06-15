# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 20:07:34 2025

@author: smitp
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

s = 10
r = 28
b = 8/3

max_iter = 3000

def new_point(x, y, z, del_t):
    
    x_new = s*(y - x)*del_t + x
    y_new = (x*(r - z) - y)*del_t + y
    z_new = (x*y - b*z)*del_t + z
    
    return x_new, y_new, z_new

x_old, y_old, z_old = 0, 1, 0
x_plot = [x_old]
y_plot = [y_old]
z_plot = [z_old]

for n in range(max_iter):
    x_new, y_new, z_new = new_point(x_old, y_old, z_old, 0.01)
    x_old, y_old, z_old = x_new, y_new, z_new
    x_plot.append(x_new)
    y_plot.append(y_new)
    z_plot.append(z_new)
    
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x_plot, y_plot, z_plot, lw = 0.75, color = 'blue', label = '(x,y,z) = (0,1,0)')
ax.legend()
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.savefig('Lorentz.png')
plt.show()

