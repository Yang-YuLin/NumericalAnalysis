# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:47:57 2018

@author: 杨玉林
"""

import numpy as np
import matplotlib.pyplot as plt

def lagrangian_polynomial(x,xi=[],yi=[]):
    n = len(xi)
    fx = 0
    k = 0 #k是点的下标，从0到n 
    while k!=n:
        t = 1
        for j in range(n):
            if j!=k:
                t = t*(x-xi[j])/(xi[k]-xi[j])
                print("(x-%d)/(%d-%d)"%(xi[j],xi[k],xi[j]))
        fx = fx + t*yi[k]
        k = k+1
    print("在x=3处的值f(3)=%d"%fx)    
    return fx
 
def paint():
    x = np.arange(-4, 5, 0.05)
    y1 = [0 * i for i in x]
    y = np.arange(-6, 6, 0.05)
    x1 = [0 * i for i in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')    
    
print("求过三个点(0,1),(1,2),(2,3)的插值多项式:") 
print("1607094105 杨玉林") 
f3 = lagrangian_polynomial(3,[0,1,2],[1,2,3])    

plt.plot(0,1,'or-')
plt.plot(1,2,'or-')
plt.plot(2,3,'or-')
plt.plot(3,f3,'og-',label ='predict point')
plt.legend()

paint()
x = np.linspace(-4,5,100)
y = [i+1 for i in x]
plt.ylim(-6,6)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Lagrangian interpolation polynomial')
plt.plot(x,y,'blue')
plt.show()
