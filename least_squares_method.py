# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:49:32 2018

@author: 杨玉林
"""

'''以线性回归为例,用最小二乘法进行曲线拟合'''

import numpy as np
import matplotlib.pyplot as plt   

def least_squares_method(d={}):
    for x,y in d.items():
        plt.plot(x,y,'or-')
    
    sum_xiyi = 0
    for x,y in d.items():
        sum_xiyi = sum_xiyi + x*y
     
    sum_xi = 0
    for x in d:
        sum_xi = sum_xi + x
        
    sum_yi = 0
    for y in d.values():
        sum_yi = sum_yi + y
        
    sum_xi2 = 0
    for x in d:
        sum_xi2 = sum_xi2 + x*x
    
    n = len(d)
    y_average = sum_yi/n 
    x_average = sum_xi/n
    
    k = (n*sum_xiyi - sum_xi*sum_yi) / (n*sum_xi2 - np.power(sum_xi,2))
    b = y_average - k*x_average
    print("用最小二乘法得出来的拟合直线为:y=%.2f+%.2fx"%(b,k))
    
    print("图像如下所示:")
    x = np.linspace(0.0,1.0,100)
    y = [k*i+b for i in x]
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,y)
    plt.show()
 
print("已知试验数据：")
print("xi | 0.0  0.2  0.4  0.6  0.8")
print("yi | 0.9  1.9  2.8  3.3  4.2")
       
least_squares_method({0.0:0.9 , 0.2:1.9 , 0.4:2.8 , 0.6:3.3 , 0.8:4.2})
        
    
  
    
    
