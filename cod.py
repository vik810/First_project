import matplotlib.pyplot as plt
import numpy as np
import physconst as phc

def light_deformation(alpha=10, y_tela=1.5*10**13, r=7*10**8, m=1.9*10**30):
    """ Функция, расчитывающая угол искривления луча света 
        Параметры функции:
            alpha - угол наклона луча (относительно вертикали)
            y_tela - расстояние между телом и началом луча 
            r - расстояние между телом и точкой преломления
            m - масса тела  
    """
    alpha = alpha*np.pi/180 #перевод угла альфа из градусов в радианы
    plt.plot(0, y_tela, color='y', marker='o', ms=15) 
    #схематичное изображение солнца
    
    d = (y_tela**2 + r**2)**0.5 #расчет длины луча
    
    x11 = 0
    x12 = d*np.sin(alpha)
    y11 = 0
    y12 = d*np.cos(alpha)
    plt.plot([x11, x12], [y11, y12], color='orange')
    #изображение траектории луча до точки искревления
    
    tetta=4*phc.G*m/(r*phc.c**2) #вычисление угла искривления (tetta)
    print(tetta*180/np.pi) #вывод сислового значения угла искривления
    
    x21 = d*np.sin(alpha)
    x22 =- d*np.cos(np.pi/2 + alpha - tetta)
    y21 = d*np.cos(alpha)
    y22 = d*np.sin(np.pi/2 + alpha - tetta) + y_tela
    plt.plot([x21, x22], [y21, y22], color='orange')
    #изображение траектории луча после точки искревления
    
    x31=d*np.sin(alpha)
    x32=y22*np.tan(alpha)
    y31=d*np.cos(alpha)
    y32=d*np.sin(np.pi/2 + alpha - tetta) + y_tela
    plt.plot([x31, x32], [y31, y32], color='orange', linestyle='--')
    #изображение траектории луча без искревления
    
    
    plt.plot(x22, y22, color='orange', marker='*', ms=12)
    plt.plot(x32, y32, color='orange', marker='*', ms=12)
    #схематичное изображение звезд

    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.axis('equal')
    plt.show()
    
light_deformation()
