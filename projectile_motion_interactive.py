import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
fig.subplots_adjust(bottom=0.30)

#Set up the time domain and initial conditions:
t = np.linspace(0,2,100)
theta0=np.pi/4
v0=2.5

#Define functions of v and theta:
def x(v,theta):
	return v*np.cos(theta)*t
def y(v,theta):
	return v*np.sin(theta)*t - 4.9*t**2
def tof(v,theta):
	return 2*v*np.sin(theta)/9.8
def ymax(v,theta):
	return v**2*np.sin(theta)**2/9.8 - 4.9*(v**2*np.sin(theta)**2)/9.8**2
def xrang(v,theta):
	return v*np.cos(theta)*2*v*np.sin(theta)/9.8

#Instantiate plots objects:
[line] = ax.plot(x(v0,theta0), y(v0,theta0))
vvec = ax.quiver(0,0,v0*np.cos(theta0),v0*np.sin(theta0),scale=20,scale_units='x')

#Instantiate texts and calculations:
toftext = ax.text(0.01,0.95, "Time of Flight: "+str(round(tof(v0,theta0),2))+" s")
ymtext = ax.text(xrang(v0,theta0)/2-0.075,ymax(v0,theta0)+0.05,"ymax = "+str(round(ymax(v0,theta0)))+" m")
xrtext = ax.text(xrang(v0,theta0), 0.025,"xrange = "+str(round(xrang(v0,theta0),2))+" m")
kepmtext = ax.text(0.01, 0.85, "Initial KE/mass: "+str(round(0.5*v0**2,2))+" J/kg")
mpepmtext = ax.text(0.01, 0.80, "Max PE/mass: "+str(round(9.8*ymax(v0,theta0),2))+" J/kg")

#Define plot properties:
ax.set_title("Projectile Motion")
ax.set_xlim([0,2])
ax.set_ylim([0,1])
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

#Instantiate interactables:
theta_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
theta_slider = Slider(theta_slider_ax, 'Initial Angle (rad)', 0.1, np.pi/2, valinit=theta0)
v_slider_ax = fig.add_axes([0.25, 0.10, 0.65, 0.03])
v_slider = Slider(v_slider_ax, 'Initial Speed (m/s)', 0.1, 5, valinit=v0)

#Define update functions:
def sliders_on_changed(val):
	#Update trajectory curve:
	line.set_xdata(x(v_slider.val, theta_slider.val))
	line.set_ydata(y(v_slider.val, theta_slider.val))
	
	#Update text and calculations:
	toftext.set_text("Time of Flight: "+str(round(tof(v_slider.val,theta_slider.val),2))+" s")
	ymtext.set_x(xrang(v_slider.val,theta_slider.val)/2-0.075)
	ymtext.set_y(ymax(v_slider.val,theta_slider.val)+0.05)
	ymtext.set_text("ymax = "+str(round(ymax(v_slider.val,theta_slider.val),2))+" m")
	xrtext.set_x(xrang(v_slider.val,theta_slider.val))
	xrtext.set_text("xrange = "+str(round(xrang(v_slider.val,theta_slider.val),2))+" m")
	kepmtext.set_text("Initial KE/mass: "+str(round(0.5*v_slider.val**2,2))+" J/kg")
	mpepmtext.set_text("Max PE/mass: "+str(round(9.8*ymax(v_slider.val,theta_slider.val),2))+" J/kg")
	
	#Update v0 vector:
	vvec.set_UVC(v_slider.val*np.cos(theta_slider.val),v_slider.val*np.sin(theta_slider.val))
	
	#No idea what this does but is apparently necessary:
	#fig.canvas.draw_idle()
	
#Connect interaction with triggered function:
v_slider.on_changed(sliders_on_changed)
theta_slider.on_changed(sliders_on_changed)

#Display plot:
plt.show()
