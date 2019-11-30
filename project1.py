import matplotlib.pyplot as plt
import numpy as np
import physconst as phc

def parabola(a=10, y_tela=1.5*10**13, r=7*10**8, m=1.9*10**30):
    """ jhill
    """
    a = a*np.pi/180
    plt.plot(0, y_tela, marker='o', ms=15)
    
    d = (y_tela**2 + r**2)**0.5
    
    x11 = 0
    x12 = d*np.sin(a)
    y11 = 0
    y12 = d*np.cos(a)
    plt.plot([x11, x12], [y11, y12])
    
    tetta=4*phc.G*m/(r*phc.c**2)
    print(tetta*180/np.pi)
    
    x21 = d*np.sin(a)
    x22 =- d*np.cos(np.pi/2 + a - tetta)
    y21 = d*np.cos(a)
    y22 = d*np.sin(np.pi/2 + a - tetta) + y_tela
    plt.plot([x21, x22], [y21, y22])
    

    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.axis('equal')
    plt.show()
    
parabola()


