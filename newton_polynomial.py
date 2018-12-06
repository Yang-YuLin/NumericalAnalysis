# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:15:10 2018

@author: 杨玉林
"""

import matplotlib.pyplot as plt
import numpy as np

#计算n阶差商
def chashang(xi=[],fi=[]):
    if len(xi) > 2 and len(fi) > 2:
        return (chashang(xi[:len(xi)-1],fi[:len(fi)-1])-chashang(xi[1:len(xi)],fi[1:len(fi)]))/(xi[0]-xi[-1])
    elif len(xi) == 2 and len(fi) == 2:
        return (fi[1]-fi[0])/(xi[1]-xi[0])
    else:
        return fi[0]

#得到系数并求得多项式
def newton_polynomial(n,xi=[],fi=[]):
    b=[]
    print("根据差商可求得:")
    for i in range(n+1):
        b.append(chashang(xi[:i+1],fi[:i+1]))
        print("b[%d] = %.2f"%(i,b[i]))  
    print("综上可得到多项式函数如下：")
    print("f(x)=%.2f%.2f*(x+%d)+%.2f*(x+%d)*(x+%d)%.2f*(x+%d)*(x+%d)*(x-%d)"%(b[0],b[1],-xi[0],b[2],-xi[0],-xi[1],b[3],-xi[0],-xi[1],xi[2]))    
    return b

#多项式函数
def f(x):
    return b[0] + b[1]*(x-xi[0])+b[2]*(x-xi[0])*(x-xi[1])+b[3]*(x-xi[0])*(x-xi[1])*(x-xi[2])
 
def paint():
    x = np.arange(-4, 6, 0.05)
    y1 = [0 * i for i in x]
    y = np.arange(-25, 35, 0.05)
    x1 = [0 * i for i in y]
    plt.plot(x, y1, '-', color='black')
    plt.plot(x1, y, '-', color='black')    

print("1607094105杨玉林")    
print("已知函数f(x)在节点x=-3,-1,4,5处的函数值f(x)分别是9,4,22,12")
print("求三次牛顿插值多项式并计算f(2)的近似值：") 

n = 3  #n是阶次
xi = [-3,-1,4,5]
fi = [9,4,22,12]
b = newton_polynomial(n,xi,fi)      
print("f(2)的近似值为%.2f"%f(2)) 

plt.plot(-3,9,'or-')
plt.plot(-1,4,'or-')
plt.plot(4,22,'or-')
plt.plot(5,12,'or-')
plt.plot(2,f(2),'og-',label ='predict point')
plt.legend()

paint()
x = np.linspace(-4,6,100)
y = [f(i) for i in x]
plt.ylim(-25,35)     
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton interpolation polynomial')
plt.plot(x,y,'blue')
plt.show()
