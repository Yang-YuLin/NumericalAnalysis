# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:12:03 2018

@author: 杨玉林
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return np.power(x,5)-3.5*np.power(x,4)+2.75*np.power(x,3)+2.125*np.power(x,2)-3.875*x+1.25

def g(m,n):
    X =m+n*1j
    return np.power(X,5)-3.5*np.power(X,4)+2.75*np.power(X,3)+2.125*np.power(X,2)-3.875*X+1.25

a = [1.25,-3.875,2.125,2.75,-3.5,1]
b = [0,0,0,0,0,0] #b = ['b0','b1','b2','b3','b4','b5']
c = [0,0,0,0,0,0] #c = ['c0','c1','c2','c3','c4','c5'] 
          
def getB(r,s):
    b[5] = round(a[5],5)
    b[4] = round(a[4]+r*b[5],5)
    for i in range (4,0,-1):
        i = i-1
        b[i] = round(a[i]+r*b[i+1]+s*b[i+2],5)
    
def getC(r,s):
    c[5] = round(b[5],5)
    c[4] = round(b[4]+r*c[5],5)
    for i in range(3,0,-1):
        c[i] = round(b[i]+r*c[i+1]+s*c[i+2],5)
    
#n是阶次,j存放解的下标   
def belsto_method(n,r,s,ξ,N,k,j,L):
    getB(r,s)
    getC(r,s)
    Δr = (b[0]*c[3]-b[1]*c[2]) / (c[2]*c[2]-c[1]*c[3])
    Δs = (b[1]*c[1]-b[0]*c[2]) / (c[2]*c[2]-c[1]*c[3])
    r = r + Δr
    s = s + Δs
    εr = abs(Δr/r)
    εs = abs(Δs/s)
    while εr > ξ or εs > ξ:
        if k < N:
            k = k+1
            getB(r,s)
            getC(r,s)
            Δr = (b[0]*c[3]-b[1]*c[2]) / (c[2]*c[2]-c[1]*c[3])
            Δs = (b[1]*c[1]-b[0]*c[2]) / (c[2]*c[2]-c[1]*c[3])
            r = r + Δr
            s = s + Δs
            εr = abs(Δr/r)
            εs = abs(Δs/s)
        else:
            print("迭代失败！")
            return 
    Δ = r*r+4*s
    if Δ < 0:
        print("经过%d次迭代后，得到多项式的根:"%k)
        print("x%d = %d+%.3fi" % (j,round((r/2),3),round((np.power(abs(Δ),1/2)/2),3)))
        L.append(round(r/2,3)+1j*round(np.power(abs(Δ),1/2)/2,3))
        j = j+1
        print("x%d = %d-%.3fi" % (j,round((r/2),3),round((np.power(abs(Δ),1/2)/2),3)))
        L.append(round(r/2,3)-1j*round(np.power(abs(Δ),1/2)/2,3))
    else:
        print("经过%d次迭代后，得到多项式的根:"%k)
        print("x%d = %.1f" % (j,(r+np.power(Δ,1/2))/2))
        plt.plot((r+np.power(Δ,1/2))/2,0,'-or')
        L.append(round((r+np.power(Δ,1/2))/2,2))
        j = j+1
        print("x%d = %.1f" % (j,(r-np.power(Δ,1/2))/2))
        plt.plot((r-np.power(Δ,1/2))/2,0,'-or')
        L.append(round((r-np.power(Δ,1/2))/2,2))
    
    n = n-2
    #此时，商式存在三种可能：
    if n == 1:
        j = j+1
        print("x%d = %.1f" % (j,round(-r/s,0)))
        plt.plot(round(-r/s,0),0,'-or')
        L.append(round((-r/s),2))
    elif n == 2:
        print("x%d = %.1f" % (j,(r+np.power(Δ,1/2))/2))
        L.append((r+np.power(Δ,1/2))/2)
        j = j+1
        print("x%d = %.1f" % (j,(r-np.power(Δ,1/2))/2))
        L.append((r+np.power(Δ,1/2))/2)
    else:
        a[0] = b[2]
        a[1] = b[3]
        a[2] = b[4]
        a[3] = b[5]
        a[4] = 0
        a[5] = 0
        belsto_method(n,r,s,ξ,N,1,j+1,L)
 
print("贝尔斯托法求下面多项式的根：")        
print("f(x)=x^5-3.5*x^4+2.75*x^3+2.125*x^2-3.875*x+1.25")
print("使用初始估计为r=s=-1,并满足迭代条件ξ=1%")
L=[]
belsto_method(5,-1,-1,0.01,100,1,1,L)
print("综上，多项式的根为：")
print(L)

x = np.linspace(-1.5,3,100)
y =[f(i) for i in x]
plt.ylim(-25,45)
plt.plot(x,y)
plt.hlines(0,-1.5,3)
plt.title("real root")
plt.show()

figure = plt.figure()
ax = Axes3D(figure)
m,n = np.mgrid[-2:2:40j,-2:2:40j]
y = g(m,n)
ax.plot_surface(m,n,y) 
ax.set_xlabel('m label', color='r')
ax.set_ylabel('n label', color='g')
ax.set_zlabel('y label', color='b')
plt.show()