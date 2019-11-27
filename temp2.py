import matplotlib.pyplot as plt
import numpy as np

def parabola(a=4, b=2, c=0.5):
    x = np.arange(0,10,0.01)
    y = a*x
    plt.plot(0,20, marker='o', ms=15)
    plt.plot(x,y,color='k',label='papabola')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.show()
    
parabola()
