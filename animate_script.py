#!/home/cryora/anaconda2/bin/python
from matplotlib import animation, pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.exp(-0.01 * i) * np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

def animate2(i):
	# 20ms/step => 50steps/s
	factor = 20.0/1000 #(20ms/step)*(1s/1000ms) = 0.02s/step
	# Multiply factor by angular frequency, in radians per second, to get "step" frequency, in radians per step
	
	x = np.linspace(0, 2, 1000)
	if i/50%2 == 0:
		y = np.exp(-x)*np.sin(2*np.pi * (x/2 - 1*factor * i))
	elif i/50%2 == 1:
		y = np.sin(2*np.pi * (x + 2*factor * i))
	line.set_data(x, y)
	return line,


anim = animation.FuncAnimation(fig, animate2, init_func=init, frames=500, interval=20, blit=True)
plt.show()
