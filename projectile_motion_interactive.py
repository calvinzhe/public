import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.30)

t = np.linspace(0,2,100)
theta0=np.pi/4
v0=2.5

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

[line] = ax.plot(x(v0,theta0), y(v0,theta0))

toftext = ax.text(0.01,0.95, "Time of Flight: "+str(round(tof(v0,theta0),2))+" s")
ymtext = ax.text(xrang(v0,theta0)/2-0.075,ymax(v0,theta0)+0.05,"ymax = "+str(round(ymax(v0,theta0)))+" m")
xrtext = ax.text(xrang(v0,theta0), 0.025,"xrange = "+str(round(xrang(v0,theta0),2))+" m")

ax.set_title("Projectile Motion")
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

theta_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
theta_slider = Slider(theta_slider_ax, 'Initial Angle (rad)', 0.1, np.pi/2, valinit=theta0)
v_slider_ax = fig.add_axes([0.25, 0.10, 0.65, 0.03])
v_slider = Slider(v_slider_ax, 'Initial Speed (m/s)', 0.1, 5, valinit=v0)

def sliders_on_changed(val):
	line.set_xdata(x(v_slider.val, theta_slider.val))
	line.set_ydata(y(v_slider.val, theta_slider.val))
	
	toftext.set_text("Time of Flight: "+str(round(tof(v_slider.val,theta_slider.val),2))+" s")
	ymtext.set_x(xrang(v_slider.val,theta_slider.val)/2-0.075)
	ymtext.set_y(ymax(v_slider.val,theta_slider.val)+0.05)
	ymtext.set_text("ymax = "+str(round(ymax(v_slider.val,theta_slider.val),2))+" m")
	xrtext.set_x(xrang(v_slider.val,theta_slider.val))
	xrtext.set_text("xrange = "+str(round(xrang(v_slider.val,theta_slider.val),2))+" m")
	
	fig.canvas.draw_idle()
	
v_slider.on_changed(sliders_on_changed)
theta_slider.on_changed(sliders_on_changed)

plt.show()
