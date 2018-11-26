# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:27:26 2018

@author: 杨玉林
"""

import matplotlib.pyplot as plt 
import numpy as np
import math

def f(x):
    return math.pow(x,3)-x-1

def binary_method(a,b,c):
    x0 = (a + b) / 2
    plt.plot(x0,0,'|r-')
    if f(x0) == 0:
        print("方程解x0 =",x0)
        return x0
    else:
        if f(a)*f(x0) < 0:
            b = x0
        elif f(x0)*f(b) < 0:
            a = x0
        if abs(a-b) < c:
            print("方程解x0 =",x0)
            return x0
        else:
            binary_method(a,b,c)
            
print("二分法求解方程根：设函数f(x)=x^3-x-1")
print("根所在区间[a,b]中的a=1.0,b=2.0,误差要求c=0.001")
a = 1.0
b = 2.0
c = 0.001
if f(a)*f(b) > 0:
    print("对不起，方程根不在所输入的区间内！")
else:
    binary_method(a,b,c)

x = np.linspace(0,3,100)
y = [f(i) for i in x]
plt.xlim(1.0,2.0)
plt.ylim(-2,8)
yy = [0 for i in x]
plt.xlabel('x')
plt.ylabel('f(x)=x^3-x-1')
plt.plot(x,y)
plt.plot(x,yy)
plt.show()