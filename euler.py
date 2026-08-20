
#SUSHANT

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

x=np.linspace(-10, 10,500)
y=np.linspace(-10, 10, 500)
xv,yv=np.meshgrid(x, y)
zv= (xv)**2+(yv)**2 # HOMOGENEOUS FUNCTION OF DEGREE 2 DEPENDANT ON TWO VARIABLES

# ADDING 3-D SUBPLOTS

fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(1,1,1,projection='3d')
ax.view_init(elev=30, azim=0)
ax.set_xlabel("x**2")
ax.set_ylabel("y**2")
ax.set_zlabel("x**2+y**2")
ax.set_title("Verification of Euler's theorem for a homogeneous function of degree 2")
dy=y[1]-y[0]
dx=x[1]-x[0]
dzy, dzx=np.gradient(zv, dy, dx)
surf=ax.plot_surface(xv, yv, dzx*xv+dzy*yv , cmap='viridis', alpha=.7, label="x*fx+y*fy") #LHS OF EULER'S THEOREM
wire=ax.plot_wireframe(xv, yv, 2*zv, color="black", linewidth=.3, label="2*f(x,y)") #RHS OF EULER'S THEOREM
ax.legend([surf, wire], ["x*fx+y*fy", "2*f(x,y)"])

# ADDING ANIMATION

def animate(i):
    ax.view_init(elev=30, azim=3*i)
ani=animation.FuncAnimation(fig, animate, frames=120, interval=50)
plt.show()
