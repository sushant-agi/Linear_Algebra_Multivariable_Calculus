
#SUSHANT

#MacLaurin Series for log(1+x) and exp(x)

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider
x=np.linspace(-1, 3, 20000)
x=x[x!=-1]
x2=np.linspace(-15, 10, 2000)
y1=np.log(1+x)
y2=np.exp(x2)
fig, axes=plt.subplots(1, 2, figsize=(5,5))
plt.subplots_adjust(bottom=0.20)



#Defining the Maclaurin Polynomial for log(1+x) and exp(x)
def McPoly1(x, n1):
    z=x*0
    plusminus=0
    for i in range(1 ,n1+1, 1):
         z=z+((-1)**plusminus)*x**i/i
         plusminus=plusminus+1
    return z
n0=0
z1=McPoly1(x, n0)

def McPoly2(x2, n):
    z=x2**0
    
    for i in range(1 ,n+1, 1):
         z=z+x2**i/math.factorial(i)
         
    return z
n0=0
z2=McPoly2(x2, n0)

#The Curve and the Slider
ax1=axes[0]
true_curve1,=ax1.plot(x, y1, label="log(1+x)")
approx_curve1,=ax1.plot(x, z1, label=" Approximate Maclaurin polynomial(degree {n0})", linestyle="--")
ax1_slider=plt.axes([.15, .1, .35, .03])
ax1.set_ylim(top=10, bottom=-10)
slider=Slider(ax1_slider, "LOG Degree(n)", 0, 30, valinit=n0, valstep=1)
ax1.grid(True)
ax2=axes[1]
true_curve2,=ax2.plot(x2, y2, label="exp(x)", color="green")
approx_curve2,=ax2.plot(x2, z2, label=" Approximate Maclaurin polynomial(degree {n0})", linestyle="--", color="brown")
ax2_slider=plt.axes([.15, .02, .35, .03])
ax2.set_ylim(top=10, bottom=-1)
ax2.set_xlim(left=-15, right=8)
ax2.grid(True)
slider2=Slider(ax2_slider, "EXP Degree(n)", 0, 30, valinit=n0, valstep=1)

#Updating the curve as the slider is moved
def update(val):
      n1=int(slider.val)
      n2=int(slider2.val)
      z1=McPoly1(x, n1)
      z2=McPoly2(x2, n2)
      approx_curve1.set_ydata(z1)
      approx_curve2.set_ydata(z2)
      
      approx_curve1.set_label("Approximate Maclaurin polynomial log(degree {n})")
      approx_curve2.set_label("Approximate Maclaurin polynomial exp(degree {n})")

      fig.canvas.draw_idle()
      ax1.legend(loc="upper left", fontsize=8)
      ax2.legend(loc="upper left", fontsize=8)
slider.on_changed(update)
slider2.on_changed(update)

plt.show()