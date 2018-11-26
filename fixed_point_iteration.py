# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:56:11 2018

@author: 杨玉林
"""

import math
import matplotlib.pyplot as plt
import numpy as np

#求解X(i+1)
def g(x):
    return math.pow(2,1/2)*math.pow(x,1/2)

def fixed_point_iteration(x0,ε,N):
    k = 1
    x1 = g(x0)
    print("第1次迭代结果为",x1)
    while abs(x1-x0) > ε:
        if k<N:
            plt.plot(x0,0,'or-')
            plt.plot((x0,x1),(g(x0),g(x0)))
            plt.plot((x1,x1),(g(x1),x1))
            k=k+1
            x0 = x1
            x1 = g(x0)
            print("第%d次迭代结果为"%k,x1)
        else:
            print("迭代失败！") 
            break
    print("得出方程x^2=2x在2附近的一个根为：",x1)

print("定点迭代法求x^2=2x在2附近的一个根：")
print("假设迭代的初值x0=4,精度要求为ε=0.001,最大迭代次数N=20")
x0 = 4
ε = 0.001
N = 20
fixed_point_iteration(x0,ε,N)

x = np.linspace(0,4,100)
y1 = [g(i) for i in x]
y2 = [i for i in x]
plt.title("Fixed Point Iteration for Root Finding")
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
