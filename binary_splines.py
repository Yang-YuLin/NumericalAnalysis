# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:53:33 2018

@author: 杨玉林
"""

import numpy as np
import sympy
import matplotlib.pyplot as plt

#N+1个数据点
x = [3,4.5,7,9]
y = [2.5,1,2.5,0.5]

#初始化row_data列表，元素的值都为0
def init_list(length):
    data = []
    for i in range(length):
        data.append(0)
    return data

#对3N个条件列方程，得出关于条件的矩阵
def condition_matrix(x):
    condition = [] #二维
    N = len(x) -1 #N个区间

    #内点处列的2N-2个条件
    i = 1
    while i < N:
        row_data1 = init_list(3*N)
        row_data1[(i-1)*3] = x[i]*x[i]
        row_data1[(i-1)*3+1] = x[i]
        row_data1[(i-1)*3+2] = 1
                 
        row_data2 = init_list(3*N)
        row_data2[i*3] = x[i]*x[i]
        row_data2[i*3+1] = x[i]
        row_data2[i*3+2] = 1
        
        condition.append(row_data1[1:])
        condition.append(row_data2[1:])
        i = i+1
     
    #两个端点处列的2个条件
    row_data1 = init_list(3*N-1)
    row_data1[0] = x[0]
    row_data1[1] = 1
    condition.append(row_data1)

    row_data2 = init_list(3*N)
    row_data2[(N-1)*3] = x[-1]*x[-1]
    row_data2[(N-1)*3+1] = x[-1]
    row_data2[(N-1)*3+2] = 1
    condition.append(row_data2[1:])
    
    #内点一阶导数相等列的N-1个条件
    i = 1
    while i < N:
        row_data = init_list(3*N)
        row_data[(i-1)*3] = 2*x[i]
        row_data[(i-1)*3 + 1] = 1
        row_data[i*3] = -2*x[i]
        row_data[i*3+1] = -1
        condition.append(row_data[1:]) 
        i = i+1
        
    return condition
 
#对3N个条件列方程，得出关于因变量y的矩阵,返回样条函数的系数
def y_matrix(y):
    N = len(y) - 1 #N个区间
    column_data = init_list(3*N-1) #一维
    
    i = 1
    while i < N:
        column_data[(i-1)*2] = y[i]
        column_data[(i-1)*2+1] = y[i]
        i = i+1
    column_data[(N-1)*2] = y[0]
    column_data[(N-1)*2+1] = y[-1]
    
    a = np.array(condition_matrix(x)) 
    b = np.array(column_data)      
    return np.linalg.solve(a,b)    
    
print("用二次样条对(3,2.5),(4.5,1),(7,2.5),(9,0.5)进行插值,并估计函数在5处的值。")
print('\n')    
print("对4个数据点列9个方程得到如下：")
condition = y_matrix(y) #condition为样条函数的系数，即[b1,c1,a2,b2,c2,a3,b3,c3]
print("样条函数的系数[b1,c1,a2,b2,c2,a3,b3,c3] =")
print(condition)
print('\n')
print("a1 = 0","      b1 =",condition[0],"    c1 =",condition[1])
print("a2 =",condition[2],"   b2 =",condition[3],"   c2 =",condition[4])
print("a3 =",condition[5],"   b3 =",condition[6],"    c3 =",condition[7])
print('\n')
x = sympy.Symbol('x') # 首先定义x为一个符号，表示一个变量
fx1 = condition[0]*x + condition[1] 
fx2 = round(condition[2],2)*x*x + round(condition[3],2)*x + condition[4]
fx3 = round(condition[5],1)*x*x + round(condition[6],1)*x + round(condition[7],1)
print("fx1 =",fx1)
print("fx2 =",fx2)
print("fx3 =",fx3)
print('\n')
f5 = condition[2]*5*5 + condition[3]*5 + condition[4]
print("在x=5处的函数值为：",f5)
print("1607094105 杨玉林")

plt.title("binary_splines")
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(2,10)
plt.ylim(0,5)

plt.scatter(3,2.5,color="red")
plt.scatter(4.5,1,color="red")
plt.scatter(7,2.5,color="red")
plt.scatter(9,0.5,label="data_point",color="red")
plt.legend()

x1 = np.linspace(3,4.5)
y1 = [condition[0]*i + condition[1] for i in x1]
plt.plot(x1,y1,label = fx1)
plt.legend()

x2 = np.linspace(4.5,7)
y2 = [condition[2]*i*i + condition[3]*i + condition[4] for i in x2]
plt.plot(x2,y2,label = fx2)
plt.legend()

x3 = np.linspace(7,9)
y3 = [condition[5]*i*i + condition[6]*i + condition[7] for i in x3]
plt.plot(x3,y3,label = fx3)
plt.legend()

plt.scatter(5,f5,label="predict_point",color="green")  
plt.legend() 
plt.show()