import matplotlib.pyplot as plt
import numpy as np
import physconst as phc

def parabola(a=np.pi/3):
    x = np.arange(0,10,0.01)
    y = np.tan(a)*x
    plt.plot(0,20, marker='o', ms=15)
    plt.plot(x,y,color='k',label='papabola')
    x2 = np.arange(10, 0, 0.01)
    y2 = x2*np.tan(a+(4*phc.G*10/(5*phc.c**2))
    plt.plot(x2,y2,color='r',label='papabola')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.show()


parabola()
