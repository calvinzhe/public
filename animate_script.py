#!/home/cryora/anaconda2/bin/python
from matplotlib import animation, pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(( -1, 1))
ax.set_ylim(( -1, 1))

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
	return line,
	
def animate3(i):
	#x = vx0t=> t = x/vx0
	#y = -1/2gt^2 + vy0t => -1/(2gvx0^2)x^2+vy0/vx0x
	#y = -1/(2gvx0^2)[x^2 - 2g(vy0vx0)x]
	#y = -/1(2gvx0^2){[x-g(vy0vx0)]^2-4g^2(vy0vx0)^2}
	w = 2*np.pi/1000
	t = np.linspace(0,1,1000)
	x = 3*np.cos(w*i)*t
	y = -4.5*t**2+3*np.sin(w*i)*t
	line.set_data(x,y)
	return line,


anim = animation.FuncAnimation(fig, animate3, init_func=init, frames=250, interval=1, blit=True)
plt.show()
