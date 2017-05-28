import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib import animation, pyplot as plt

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def destroy(e):
    sys.exit()

root = Tk.Tk()
root.wm_title("Embedding in TK")


correction_factor = 1

A=5
f=1
w=2*np.pi*f
T = 1/f*correction_factor
t = np.linspace(0,T,1000)
tgraph = np.linspace(-1,0,1000)

fig = plt.figure()
fig.subplots_adjust(hspace=0.5)
ax = fig.add_subplot(211)
ax1 = fig.add_subplot(212)

point, = ax.plot([A],[0],'go')
ax.set_xlim(-1,1)
ax.set_ylim(-A,A)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Simple Harmonic Motion")

line, = ax1.plot([],[])
ax1.set_xlim(-1,1)
ax1.set_ylim(-A,A)
ax1.set_xlabel("t - t_present")
ax1.set_ylabel("y")


def animate(i):
    point.set_data(0,A*np.cos(w*t[i]))
    vanim = A*np.cos(w*(tgraph+t[i]))
    line.set_data(tgraph,vanim)
    return point, line,


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=root, text='Quit', command=sys.exit)
button.pack(side=Tk.BOTTOM)

ani = animation.FuncAnimation(fig, animate,frames=1000, interval=1, blit=True)

Tk.mainloop()
