
import numpy as np
from matplotlib import animation, pyplot as plt
from matplotlib.widgets import Slider

vectors = False

fps = 60
interval = 1000/fps
anim_time = 60 #Time in seconds for animation to run before restarting (delays skipping)
frames = anim_time*fps

# Initial Conditions:
A = 5
v = 0
# System Parameters:
k = 100
m = 1
w = np.sqrt(k/m)
f = w/(2*np.pi)
T = 1/f
a = -A*w**2
# Set up time array for iterating and graphing:
t = np.linspace(0,f*anim_time,frames)
tgraph = np.linspace(-1,0,100)

fig = plt.figure(figsize=(10,5))
fig.subplots_adjust(hspace=1,wspace=0.35)
fig.suptitle("Simple Harmonic Oscillation")

# Position Animation:
ax0 = fig.add_subplot(321)
point, = ax0.plot(0,A,'go')
ax0.set_xlim(-1,1)
ax0.set_ylim(-A,A)
ax0.set_xlabel("x (m)")
ax0.set_ylabel("y (m)")
ax0.set_title("2D position")

if vectors:
    # Velocity Vector Animation:
    ax9 = fig.add_subplot(3,6,1)
    ax9.set_xlim(-1,1)
    ax9.set_ylim(-A*w,A*w)
    ax9.set_xticks([])
    ax9.set_yticks([])
    ax9.set_title("Velocity")
    
    # Acceleration Vector Animation
    ax10 = fig.add_subplot(3,6,3)
    ax10.set_xlim(-1,1)
    ax10.set_ylim(-A*w**2,A*w**2)
    ax10.set_xticks([])
    ax10.set_yticks([])
    ax10.set_title("Acceleration")

# Position Graph:
ax1 = fig.add_subplot(323)
liney, = ax1.plot([],[])
ax1.set_xlim(-1,1)
ax1.set_ylim(-A,A)
ax1.set_xlabel("t - t_present (s)")
ax1.set_ylabel("y (m)")
ax1.set_title("y position in time")

# Velocity Graph:
ax2 = fig.add_subplot(325)
linev, = ax2.plot([],[])
ax2.set_xlim(-1,1)
ax2.set_ylim(-A*w,A*w)
ax2.set_xlabel("t - t_present (s)")
ax2.set_ylabel("v (m/s)")
ax2.set_title("y speed in time")

# Potential Energy Graph:
ax3 = fig.add_subplot(324)
linePE, = ax3.plot([],[])
ax3.set_xlim(-1,1)
ax3.set_ylim(0,0.5*(A)**2*k)
ax3.set_xlabel("t - t_present (s)")
ax3.set_ylabel("PE (J)")
ax3.set_title("Potential Energy in time")

# Kinetic Energy Graph:
ax4 = fig.add_subplot(326)
lineKE, = ax4.plot([],[])
ax4.set_xlim(-1,1)
ax4.set_ylim(0,0.5*m*(A*w)**2)
ax4.set_xlabel("t - t_present (s)")
ax4.set_ylabel("KE (J)")
ax4.set_title("Kinetic Energy in time")

# Set up paramater controls:
k_slider_ax = fig.add_subplot(6,6,5)
k_slider = Slider(k_slider_ax, 'Spring Constant (N/m)', .1, 200, valinit=100)
m_slider_ax = fig.add_subplot(6,6,11)
m_slider = Slider(m_slider_ax, 'Mass (kg)', .1, 10, valinit=1)

class manipu_animate(object):
    # Pass in initial conditions:
    def __init__(self,w,t,A,k,m):
        self.w = w
        self.t = t
        self.A = A
        self.k = k
        self.m = m
        pass
    # Update object variables when user interacts with sliders:
    def sliders_on_changed(self,val):
        self.k = k_slider.val
        self.m = m_slider.val
        self.A = np.sqrt(k*A**2/self.k)
        self.w = np.sqrt(self.k/self.m)
        self.T = 2*np.pi/self.w
        self.f = 1/self.T
        self.t = np.linspace(0,self.f*anim_time,frames)
        ax0.set_ylim(-self.A,self.A)
        ax1.set_ylim(-self.A,self.A)
        ax2.set_ylim(-self.A*self.w,self.A*self.w)
        ax3.set_ylim(0,0.5*self.A**2*self.k)
        ax4.set_ylim(0,0.5*self.m*self.A**2*self.w**2)
    # Animation update:
    def animate(self,i):
        wa = self.w
        ta = self.t
        Aa = self.A
        ka = self.k
        ma = self.m
        
        pointanim = Aa*np.cos(wa*ta[i])
        point.set_data(0,pointanim)
        
        yanim = Aa*np.cos(wa*(tgraph+ta[i]))
        liney.set_data(tgraph,yanim)
        
        vanim = -wa*Aa*np.sin(wa*(tgraph+ta[i]))
        linev.set_data(tgraph,vanim)
            
        if vectors:
            vvecanim = -wa*Aa*np.sin(wa*ta[i])
            vvec = ax9.quiver(0,0,0,vvecanim,scale=250,width=0.025)
            
            avecanim = -wa**2*Aa*np.cos(wa*ta[i])
            avec = ax10.quiver(0,0,0,avecanim,scale=1500,width=0.025)
        else:
            vvec = None
            avec = None
        
        PEanim = 0.5*(Aa**2)*ka*(np.cos(wa*(tgraph+ta[i]))**2)
        linePE.set_data(tgraph,PEanim)
        
        KEanim = 0.5*ma*(Aa*wa)**2*(np.sin(wa*(tgraph+ta[i]))**2)
        lineKE.set_data(tgraph,KEanim)
        return point, liney, linev, linePE, lineKE, #vvec, avec

ma = manipu_animate(w, t, A, k, m)
    
k_slider.on_changed(ma.sliders_on_changed)
m_slider.on_changed(ma.sliders_on_changed)

ani = animation.FuncAnimation(fig, ma.animate,frames=frames, interval=interval, blit=True)
    
plt.show()