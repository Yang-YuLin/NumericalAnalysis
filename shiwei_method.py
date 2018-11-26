# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:03:20 2018

@author: 杨玉林
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return math.pow(x,3)-x-1
    
def shiwei_method(a,b,c):
    plt.plot((a,b),(f(a),f(b)),color="magenta")
    b0 = (abs(f(a))*b + abs(f(b))*a) / (abs(f(b)) + abs(f(a)))
    if f(b0) == 0:
        print("方程解b0 =",b0)
        return b0
    else:
        if f(a)*f(b0) < 0:
            b = b0
        else:
            a = b0
        if abs(a-b) < c:
            print("方程解b0 =",b0)
            return b0
        else:
            shiwei_method(a,b,c)
    
print("试位法求解方程根：设函数f(x)=x^3-x-1")
print("根所在区间[a,b]中的a=1.0,b=1.7,误差要求c=0.001")
a = 1.0
b = 1.7
c = 0.001
if f(a)*f(b) > 0:
    print("对不起，方程根不在所输入的区间内！")
else:
    shiwei_method(a,b,c)

x = np.linspace(0,3,100)
y = [f(i) for i in x]
plt.xlim(1.0,1.6)
plt.ylim(-2,8)
yy = [0 for i in x]     
plt.xlabel('x')
plt.ylabel('f(x)=x^3-x-1')
plt.plot(x,y)
plt.plot(x,yy)
plt.show()