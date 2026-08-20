#SUSHANT

#MacLaurin Series for Cos(x)

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider
x=np.linspace(-15, 15, 2000)
y=np.exp(x)
fig, axes=plt.subplots()
plt.subplots_adjust(bottom=0.20)
plt.ylim(top=100000, bottom=-2)
axes.grid(True)

#Defining the Maclaurin Polynomial for cos(x)
# def McPoly(x, n):
#     z=x**0   
#     for i in range(0 ,n+1, 1):
#          z=z+x**i/math.factorial(i)
         
#     return z
# n0=0
# z=McPoly(x, n0)

def McPoly(x, n):
    z=np.exp(x**0*10)
    
    for i in range(1 ,n+1, 1):
         z=z+np.exp(x**0*10)*(x-10)**i/math.factorial(i)
         
    return z
n0=0
z=McPoly(x, n0)

#The Curve and the Slider
true_curve,=axes.plot(x, y, label="exp(x)")
approx_curve,=axes.plot(x, z, label=" Approximate Maclaurin polynomial(degree {n0})", linestyle="--")
ax_slider=plt.axes([.25, .1, .55, .03])
slider=Slider(ax_slider, "Degree(n)", 0, 30, valinit=n0, valstep=1)

#Updating the curve as the slider is moved
def update(val):
      n=int(slider.val)
      z=McPoly(x, n)
      approx_curve.set_ydata(z)
      approx_curve.set_label("Approximate Maclaurin polynomial(degree {n})")
      fig.canvas.draw_idle()
      axes.legend(loc="upper right", fontsize=10)
slider.on_changed(update)

plt.show()
