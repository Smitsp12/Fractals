# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 21:53:07 2025

@author: smitp
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Lorentz attractor parameters
s = 10
r = 28
b = 8/3

#Solving Lorentz ODE
def new_point(x, y, z, del_t):
    
    x_new = s*(y - x)*del_t + x
    y_new = (x*(r - z) - y)*del_t + y
    z_new = (x*y - b*z)*del_t + z
    
    return x_new, y_new, z_new

#Calculating Trajectory
def lorentz(x_old, y_old, z_old, max_iter, del_t):
    x_plot, y_plot, z_plot = [x_old], [y_old], [z_old]
    for n in range(max_iter):
        x_new, y_new, z_new = new_point(x_old, y_old, z_old, del_t)
        x_old, y_old, z_old = x_new, y_new, z_new
        x_plot.append(x_new)
        y_plot.append(y_new)
        z_plot.append(z_new)
    return x_plot, y_plot, z_plot

#data
max_iter = 5000
del_t = 0.01
x1, y1, z1 = lorentz(0.9, 0, 0, max_iter, del_t)
x2, y2, z2 = lorentz(0, 0.9, 0, max_iter, del_t)
x3, y3, z3 = lorentz(0, 1.1, 0, max_iter, del_t)


#Plotting figure 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(min(min(x1), min(x2)), max(max(x1), max(x2)))
ax.set_ylim(min(min(y1), min(y2)), max(max(y1), max(y2)))
ax.set_zlim(min(min(z1), min(z2)), max(max(z1), max(z2)))
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

line1, = ax.plot([], [], [], lw=0.75, color='blue', label='(x,y,z) = (0.9,0,0)')
line2, = ax.plot([], [], [], lw=0.75, color='red', label='(x,y,z) = (0,0.9,0)')
line3, = ax.plot([], [], [], lw=0.75, color='green', label='(x,y,z) = (0,0,0.9)')

ax.legend()


#update function
def animate(frame):
    line1.set_data(x1[:frame], y1[:frame])
    line1.set_3d_properties(z1[:frame])
    
    line2.set_data(x2[:frame], y2[:frame])
    line2.set_3d_properties(z2[:frame])
    
    line3.set_data(x3[:frame], y3[:frame])
    line3.set_3d_properties(z3[:frame])
    
    return line1, line2, line3

#funcanimaton
anim = FuncAnimation(fig,  #figure
                     animate, #animate function
                     frames=len(x1),  #total frames
                     interval = 10,  #interval in ms between frames
                     blit = True, #only computes new part of the plot
                     repeat = False
                     )
anim.save("lorenz.gif", writer='Pillow', fps=50)