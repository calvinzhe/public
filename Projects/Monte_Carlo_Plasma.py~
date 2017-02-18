#!/home/cryora/anaconda2/bin/python

import numpy as np
from matplotlib import animation, pyplot as plt

N = 50000

vx = np.random.normal(5,1,N)
vy = np.random.normal(0,1,N)
m = np.random.normal(10000,1000,N)
Bz = np.random.normal(10,2,N)
x0 = np.random.normal(1,0.2,N)
y0 = np.random.normal(0,0.2,N)

a = (Bz*vy - Bz*vx)/m
v2 = vx**2 + vy**2
v = np.sqrt(v2)
r = v2/a
w = v/r
r0 = np.sqrt(x0**2+y0**2)

dt = 15

def UniformCircularMotion2dFunc(i):
	t = i*dt
	return [r0*np.cos(w*t), r0*np.sin(w*t)]

fig, ax = plt.subplots()

ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], 'r,', alpha=0.25)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    vector = UniformCircularMotion2dFunc(i)
    line.set_data(vector[0], vector[1])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=500, interval=20, blit=True)
#plt.show()
anim.save('Monte_Carlo_Plasma.mp4', fps=30, extra_args = ['-vcodec','libx264'])
