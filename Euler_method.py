# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:04:08 2019

@author: 杨玉林
"""
import matplotlib.pyplot as plt
import numpy as np

#dy/dx
def f(x,y):
    return -0.5 * x**4 + 4 * x**3 - 10* x**2 + 8.5*x + 1
 
#对dy/dx微分所得到的函数 
def f1(x,y):
    return -2.0*x**3 + 12*x**2 - 20*x + 8.5
    
def Euler_method(x0,y0,h,N):
    n = 1
    plt.plot(x0,y0,'or-')
    x1 = x0 + h
    y1 = y0 + h*f1(x0,y0)
    plt.plot(x1,y1,'or-')
    plt.plot((x0,x1),(y0,y1),color="red")
    plt.annotate("h=%.2f"%h, xy=(x1,y1), xytext=(x1+0.5, y1-3),arrowprops=dict(facecolor='red', shrink=0.03, headlength = 5, headwidth = 30, width = 3))
    print("xi:",x1,"yi:",y1)
    while n!=N:
        n = n+1
        x0 = x1
        y0 = y1
        x1 = x0 + h
        y1 = y0 + h*f1(x0,y0)
        plt.plot(x1,y1,'or-')
        plt.plot((x0,x1),(y0,y1),color="red")
        print("xi:",x1,"yi:",y1)

print("常微分方程应用欧拉法求解初值问题：")        
print("当步长h=0.5时,每经过一个步长，所得x,y如下:")           
Euler_method(0,1,0.5,10)
print("当步长h=0.25时,每经过一个步长，所得x,y如下:")  
Euler_method(0,1,0.25,16)

print("1607094105 杨玉林")

plt.title("Euler method")
x = np.linspace(0,4,100)
y = [f(i,0) for i in x]
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,4)
plt.ylim(0,8)
plt.plot(x,y)
plt.annotate("True solution", xy=(2,2), xytext=(3, 1),arrowprops=dict(facecolor='blue', shrink=0.03, headlength = 5, headwidth = 30, width = 3))
plt.show()