# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 20:48:35 2025

@author: smitp
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Counting iteration before Z escape the Mandelbrot set
def mandelbrot(x, y, max_iter):
    z, n = 0, 0
    c = complex(x, y)
    for n in range(max_iter):
        if abs(z) > 2:
            return n+1
        z = z**2 + c
    return n+1

#Complex space
Re = np.linspace(-2, 1, 300)
Im = np.linspace(-1.5, 1.5, 300)
max_iter = 10

#iteration counter
def iteration_counter(max_iter):
    iteration_matrix = []
    for y in Im:
        row = []
        for x in Re:
            row.append(mandelbrot(x, y, max_iter))
        iteration_matrix.append(row)
    return iteration_matrix
    
#plotting the data
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_axis_off()
#img = ax.imshow(iteration_matrix, cmap='inferno', extent=[-2, 1, -1.5, 1.5], origin='lower', interpolation='none')
plot_text = ax.text(-0.5, 1.4,r"$z_{n+1} = z^2_{n} + c$", color = 'white', size = 10, ha='center', va = 'top')
#plt.savefig('Mandelbrot_set.jpg', dpi=300, transparent=True, bbox_inches='tight', pad_inches=0)

#animate function
def animate(frame):
    matrix = iteration_counter(frame)
    #ax.text(-0.5, 1.4,r"$z_{n+1} = z^2_{n} + c$", color = 'white', size = 10, ha='center', va = 'top')
    img = ax.imshow(matrix, cmap='inferno', extent=[-2, 1, -1.5, 1.5], origin='lower', interpolation='none')
    return plot_text, img,

#funcanimation
anim = FuncAnimation(fig,  #figure
                     animate, #animate function
                     frames=range(max_iter),  #total frames
                     interval = 100,  #interval in ms between frames
                     blit = True, #only computes new part of the plot
                     repeat = False
                     )
# Save as HTML
#anim.save("mandelbrot_set.html", writer="html")
