# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:47:15 2018

@author: 杨玉林
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 3*np.exp(x)-4*np.cos(x)

#f(x)的一阶导  
def f1(x):
    return 3*np.exp(x)+4*np.sin(x)

#求解X(i+1)
def g(x):
    return x-f(x)/f1(x)
    
def newton_method(x0,ε,N): 
    if f(x0) == 0:
        print("得出方程3e^x-4cosx=0在0.25附近的一个根为：",x0)
    else:
        k = 1
        while f1(x0) != 0:
            x1 = g(x0)
            if abs(x1-x0) > ε:
                if k<N:
                    plt.plot(x0,f(x0),'or-')
                    plt.plot(x1,0,'or-')
                    plt.plot((x0,x1),(f(x0),0),color="red")
                    k = k+1
                    x0 = x1
                    x1 = g(x0)
                    print("第%d次迭代结果为"%k,x1)
                else:
                    print("迭代失败！")
                    break
            else:
                print("得出方程3e^x-4cosx=0在0.25附近的一个根为：",x1)
                break
        print("分母为0，函数奇异！")   
def paint():
    x = np.arange(-0.5, 2, 0.05)
    y1 = [0 * i for i in x]
    y = np.arange(-20, 25, 0.05)
    x1 = [0 * i for i in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')
                
print("牛顿切线法求f(x)=3e^x-4cosx在0.25附近的一个根：")
print("假设迭代的初值x0=2,精度要求为ε=0.001,最大迭代次数N=20")
x0 = 2
ε = 0.001
N = 20  
newton_method(x0,ε,N)

paint()
x = np.linspace(-0.5,2,100)
y = [f(i) for i in x]
plt.ylim(-5,25)
plt.title("Newton's Method for Root Finding")
plt.plot(x,y,color="black")
plt.show()













