#SUSHANT

#MacLaurin Series for cos(x+y)

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider
from matplotlib import animation 

x=np.linspace(-4, 4, 50)
y=np.linspace(-4, 4, 50)
xv, yv = np.meshgrid(x, y)
zv=np.cos ( xv + yv )
fig=plt.figure()
ax=fig.add_subplot(projection="3d")
ax.set_title("Multi-variable Maclaurin series")
fig.subplots_adjust(bottom=0.20)
ax.set_zlim(-4, 4)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("cos(x+y)")
ax.view_init(elev=20, azim=0)
ax.grid(True)

#Defining the Maclaurin Polynomial for cos(x+y)
def McPoly3d(xv,yv, n):
    tv=xv**0
    plusminus=1
    for i in range(2 ,n+1, 2):
         tv=tv+((-1)**plusminus)*(xv+yv)**i/math.factorial(i)
         plusminus=plusminus+1
    return tv
n0=0
tv=McPoly3d(xv,yv, n0)

#The surfaces and the Slider
true_surface=ax.plot_surface(xv, yv, zv, cmap="viridis")
approx_surface=ax.plot_wireframe(xv, yv, tv, linewidth=.3, color='black', alpha=.6)
ax_slider=plt.axes([.25, .1, .55, .03])
slider=Slider(ax_slider, "Degree(n)", 0, 20, valinit=n0, valstep=1)
ax.legend([true_surface, approx_surface], ["cos(x+y)", "Maclaurin polynomial of cos(x+y)"], fontsize=10)

#Updating the surface as the slider is moved
def update(val):
      global approx_surface
      n=int(slider.val)
      tv=McPoly3d(xv, yv, n)
      approx_surface.remove()
      approx_surface=ax.plot_wireframe(xv, yv, tv, linewidth=.3, color='black', alpha=.6)
      fig.canvas.draw_idle()
slider.on_changed(update)


def animate(i):
    ax.view_init(elev=20, azim=5*i)
ani=animation.FuncAnimation(fig, animate, frames=72, interval=50)

plt.show()
