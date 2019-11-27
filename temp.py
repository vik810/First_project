import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()



telo= plt.plot([], [], 'r-')
xdata, ydata = [], []

# =============================================================================
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# =============================================================================
r = 10

def iskriv_ray(t):
    xdata.append(d*np.sin(alpha))
    ydata.append(d*np.cos(alpha))
    G=6.67*10**(-11)
    telo.set_data(xdata, ydata)
    tetta= (4*G*M)/(r*c**2)
ani = FuncAnimation(fig,
                    iskriv_ray,
                    frames=np.arange(0, 15*np.pi, 0.1),
                    interval=10)
                  
ani.save('ani.gif')
