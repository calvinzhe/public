#!/home/cryora/anaconda2/bin/python

import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import animation, pyplot as plt

FFMpegWriter = animation.writers['libx264']
metadata = dict(title='Monte Carlo Plasma', artist='Calvin He',
comment='Physics + Statistics + Computation!')
writer = FFMpegWriter(fps=30, bitrate=-1, metadata=metadata)

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

dt = 30

def UniformCircularMotion2dFunc(i):
	t = i*dt
	return [r0*np.cos(w*t), r0*np.sin(w*t)]

fig = plt.figure()
line, = plt.plot([], [], 'r,', alpha=0.25)

plt.xlim((-2, 2))
plt.ylim((-2, 2))

with writer.saving(fig, "./Monte_Carlo_Plasma.mp4", 100):
	for i in range(500):
		vector = UniformCircularMotion2dFunc(i)
		line.set_data(vector[0], vector[1])
		writer.grab_frame()
