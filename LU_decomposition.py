# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:30:23 2018

@author: 杨玉林
"""

import numpy as np
    
def LU_decomposition(A,B): 
    rows,columns = A.shape
    L = np.zeros((rows,columns))
    U = np.zeros((rows,columns))

    #U的第一行元素
    for j in range(columns):
        U[0][j] = A[0][j]
    
    #L的第一列元素
    for i in range(rows):
        L[i][0] = A[i][0]/A[0][0]
    
    for i in range(1,rows):
        #U的第i行元素
        for j in range(i,columns):
            sum = 0
            for k in range(0,i):
                sum = sum + L[i][k]*U[k][j]
            U[i][j] = A[i][j] - sum

        #L的第i列元素
        for j in range(i,columns):
            sum = 0
            for k in range(0,i):
                sum = sum + L[j][k]*U[k][i]
            L[j][i] = (A[j][i] - sum)/U[i][i]

    print("经LU分解得到:")
    print("L:")
    print(L)
    print("U:")
    print(U)
    
    print("\n")
    print("1607094105 杨玉林")
    print("\n")
    
    D = np.linalg.solve(L,B)
    print("根据L*D = B得到D:")
    print("D:",D)
    X = np.linalg.solve(U,D)
    print("根据U*X = D得到X:")
    print("X:",X)
    print("即x1 = %.1f , x2 = %.1f , x3 = %.1f" % (X[0],X[1],X[2]))
    return  X

A = np.array([[2,2,3],[4,7,7],[-2,4,5]])   
B = np.array([3,1,-7]) 
X = np.array(["x1","x2","x3"])    
print("求解方程组:")   
print(A,"*",X,"=",B) 
LU_decomposition(A,B)   
