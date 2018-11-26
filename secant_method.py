# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:44:34 2018

@author: 杨玉林
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 3*np.exp(x)-4*np.cos(x)

#求解X(i+1)
def g(x0,x1):
    return x1 - f(x1)*(x0-x1) / (f(x0)-f(x1))
    
def secant_method(x0,x1,ε,N):  
    k = 1
    x2 = g(x0,x1)
    print("第1次迭代结果为",x2)
    while abs(f(x2)) > ε:
        if k < N:
            plt.plot(x0,0,'or-')
            plt.plot(x1,0,'or-')
            plt.vlines(x0,0,f(x0))
            plt.plot((x0,x2),(f(x0),0),color="red")
            k = k+1
            x0 = x1
            x1 = x2
            x2 = g(x0,x1)
            print("第%d次迭代结果为"%k,x1)
        else:
            print("迭代失败！")
            break
    print("得出方程3e^x-4cosx=0在0.25附近的一个根为：",x2)

def paint():
    x = np.arange(-0.5, 2, 0.05)
    y1 = [0 * i for i in x]
    y = np.arange(-15, 20, 0.05)
    x1 = [0 * i for i in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')    
    
print("正割法求f(x)=3e^x-4cosx在0.25附近的一个根：")
print("初值x0=1.8,初值x1=1.6")
print("精度要求为ε=0.001,最大迭代次数N=20")
x0 = 1.8
x1 = 1.6
ε = 0.001
N = 20
secant_method(x0,x1,ε,N)

paint()
x = np.linspace(-0.5,2,100)
y = [f(i) for i in x]  
plt.ylim(-5,20)
plt.title("The Secant Method for Root Finding")
plt.plot(x,y,color="black")
plt.show()

