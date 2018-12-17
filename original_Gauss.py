# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:06:54 2018

@author: 杨玉林
"""

import numpy as np

a = np.array([[0.50,1.1,3.1],[2.0,4.5,0.36],[5.0,0.96,6.5]])
b = np.array([6.0,0.020,0.96])
x=[0,0,0]
m,n=a.shape #m,n是矩阵的行数和列数
    
def original_gauss(a,b): 
    for k in range(1,n):    
        d = a[k-1][k-1]
        l = k
        i = k+1
       
        while abs(a[i-1][k-1]) > abs(d):
            d = a[i-1][k-1]
            l = i
            if i==n:
                break
            else:
                i = i+1
        if d!=0:
            if l!=k:
                for j in range(k,n+1):
                    t = a[l-1][j-1]
                    a[l-1][j-1] = a[k-1][j-1]
                    a[k-1][j-1] = t
                t = b[l-1]
                b[l-1] = b[k-1]
                b[k-1] = t
            else:
                pass
       
        for i in range(k+1,n+1):
            factor = a[i-1][k-1] / a[k-1][k-1]
            a[i-1][k-1] = a[i-1][k-1] - factor*a[k-1][k-1]
            for j in range(k+1,n+1):
                a[i-1][j-1] = round(a[i-1][j-1] - factor*a[k-1][j-1],2)
            b[i-1] = round(b[i-1] - factor*b[k-1] , 3)
            
      
    x[n-1] = float("%.2f" % (b[n-1] / a[n-1][n-1]))
    for i in range(n-1,0,-1):
        sum = b[i-1]
        for j in range(i+1,n+1):
            sum = sum - float(a[i-1][j-1]*x[j-1])
        x[i-1] = round(float("%.3f" % (sum / a[i-1][i-1])) , 2)
    
      
    print("经过部分交换主元并消元后，方程组的系数矩阵为：")
    print(a)  
    print("方程组等号右边的矩阵为：")
    print(b)   
    print("1607094105 杨玉林")
    print("原方程组的解为：")
    print(x)
    print("即x1 = %.1f , x2 = %.1f , x3 = %.1f" % (x[0],x[1],x[2]))

print("解方程组:")
print("        0.50x1 + 1.1x2  + 3.1x3  = 6.0")
print("        2.0x1  + 4.5x2  + 0.36x3 = 0.020")
print("        5.0x1  + 0.96x2 + 6.5x3  = 0.96")   
original_gauss(a,b)


