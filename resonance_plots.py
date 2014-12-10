#! /usr/bin/python2.7

from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Asteroid parameters
a2 = 0.5
e2 = 0.2
w2 = 0.0	# Argument of pericentre
lambda2 = f2 = 0.0	# Initial condition

# Radius given a, e and true anomaly
def r(a, e, f):
	return (a*(1-e**2)/(1+e*np.cos(f)))

# Animation of the orbit
fig, ax = plt.subplots()
ax.axis([-2,2,-2,2])

x = np.arange(0, 0.1*2*np.pi, 0.01)
line, = ax.plot(np.cos(x), np.sin(x))

def animate(i):
	line.set_ydata(np.sin(x + i/10.0))
	line.set_xdata(np.cos(x + i/10.0))
	return line,

def init():
	line.set_ydata(np.ma.array(x,mask=True))
	line.set_xdata(np.ma.array(x,mask=True))
	return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1,1000),
       init_func=init, interval=25, blit=True)

plt.show()
