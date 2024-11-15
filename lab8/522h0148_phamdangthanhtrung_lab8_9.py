# -*- coding: utf-8 -*-
"""522H0148_PhamDangThanhTrung_lab8_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vXrO0N6S6J-zcFyjSNlXRRFkPKO9JnMJ
"""

#cau vd
import numpy as np
A=np.array([[2,1],[1,2],[1,1]])
b=[2,0,-3]
print('A=',A)
print('b=',b)
x1=np.linalg.lstsq(A,b,rcond=None)
print('x1=',x1)
x=x1[0]
print('x[by lstsq function]=',x,x[0],x[1])
print('x[1]=',x[0])
print('x[2]=',round(x[1],5))

#cau1
import numpy as np
A=np.array([[2,2],[2,3]])
b=[4,6]
print('A=',A)
print('b=',b)
x1=np.linalg.lstsq(A,b,rcond=None)
print('x1=',x1)
x=x1[0]
print('x[by lstsq function]=',x,x[0],x[1])
print('x[1]=',round(x[0],5))
print('x[2]=',round(x[1],5))

#cau2
A=np.array([[0,0,1],[0,1,1],[1,2,1],[1,0,1],[4,1,1],[4,2,1]])
C=[0.5,1.6,2.8,0.8,5.1,5.9]
print('A=',A)
print('C=',C)
x1=np.linalg.lstsq(A,C,rcond=None)

x=x1[0]
print('c=',round(x[0],5))
print('d=',round(x[1],5))
print('e=',round(x[2],5))

from numpy.ma.extras import atleast_1d
import numpy as np
import matplotlib.pyplot as plt
#cau3
#a

A=np.array([[1,0],[1,1],[1,2],[1,3]])
print(A)
b = np.array([1,1,2,2])
print(b)
x1 = np.linalg.lstsq(A,b,rcond = None)
x = x1[0]
print("x [by lstsq funtion]=",round(x[0],5),round(x[1],5))
print("x[1]=",round(x[0],5))
print("x[2]",x[1])
a0 = round(x[0],5) 
a1 = round(x[1],5) 
y = lambda x: a0 + a1*x
x_arr = np.arange(-2,5,0.1) 
y_arr = list(map(y,x_arr))
plt.scatter([0,1,2,3],b,color="blue", label = "data points")
plt.plot(x_arr,y_arr,"r",label = "least squares line")
plt.title("cau a")
plt.legend() 
plt.show()
#b
A = np.array([[1,1],[1,2],[1,4],[1,5]])
print(A)
b = np.array([0,1,2,3])
print(b)
x1 = np.linalg.lstsq(A,b,rcond = None)
x = x1[0]
print("x [by lstsq funtion]=",round(x[0],5),round(x[1],5))
print("x[1]=",round(x[0],5))
print("x[2]",x[1])
a0 = round(x[0],5)
a1 = round(x[1],5)
y = lambda x: a0 + a1*x
x_arr = np.arange(-2,5,0.1) 
y_arr = list(map(y,x_arr))
plt.scatter([1,2,4,5],b,color="blue", label = "data points")
plt.plot(x_arr,y_arr,"r",label = "least squares line")
plt.title("cau b")
plt.legend() 
plt.show()

#cau4
import numpy as np
A4=np.array([[1,2000],[1,6000],[1,20000],[1,30000],[1,40000]])
B4=[20,18,10,6,2]

x4=np.linalg.lstsq(A4,B4,rcond=None)[0]
print("Ex4 x4 = ",x4)

a=x4[0]
b=x4[1]
y= lambda x : a +b*x

x_arr = np.arange(0,50000,1)
y_arr = list(map(y,x_arr))

plt.scatter([2000,6000,20000,30000,40000],B4,color="blue",label="data points")
plt.plot(x_arr , y_arr , "r" , label = "least squares line")

plt.title("cau 4")
plt.legend()
plt.show()

#cau5
b5=[7.9,5.4,-9]
A5=np.array([[np.cos(1),np.sin(1)],[np.cos(2),np.sin(2)],[np.cos(3),np.sin(3)]])
x5=np.linalg.lstsq(A4,B4,rcond=None)[0]
print("X5= = ",x5)

a=x5[0]
b=x5[1]
y= lambda x :a*np.cos(x)+b*np.sin(x)

x_arr = np.arange(-2,4,0.1)
y_arr = list(map(y,x_arr))

plt.scatter([1,2,3],b5,color="blue",label="data points")
plt.plot(x_arr , y_arr , "r" , label = "least squares line")

plt.title("cau 5")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#cau 6
A = np.array([
    [1, 1, 1, 1],
    [8, 4, 2, 1],
    [27, 9, 3, 1],
    [64, 16, 4, 1],
    [125, 25, 5, 1],
    [216, 36, 6, 1]
])
B = np.array([2.1, 3.5, 4.2, 3.1, 4.4, 6.8])

x = np.linalg.lstsq(A, B, rcond = None)[0]
print(x)
a = x[0]
b = x[1]
c = x[2]
d = x[3]
y = lambda x: a*x*x*x + b*x*x +c*x + d
x_arr = np.arange(0, 7, 0.1)
y_arr = list( map(y, x_arr))

plt.scatter([1, 2, 3, 4, 5, 6], B, color = "blue", label = "data point")
plt.plot(x_arr, y_arr, "r", label = "least squares line")

plt.title("cau 6:")
plt.legend()
plt.show()

#cau 7 
import numpy as np

def s_matrix(lamda, mu):
    return np.array([[lamda, 0], [0, mu]])

s1 = s_matrix(2, 2)
s2 = s_matrix(0.5, 0.5)
s3 = s_matrix(1, -1)
s4 = s_matrix(-1, 1)

print("the action of S2,2:")
print(np.array([1, 0]))
print(np.array([0, 1]))
print()

print("the action of S0.5,0.5:")
print(np.array([1, 0]))
print(np.array([0, 1]))
print()

print("the action of S1,-1")
print(np.array([1, 0]))
print(np.array([0, 1]))
print()

print("the action of S-1,1")
print(np.array([1, 0]))
print(np.array([0, 1]))
print()

#cau 8
import numpy as np

def R(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


R_pi = R(np.pi)
print("R_pi = ")
print(R_pi)

R_pi_div_3 = R(np.pi/3)
print("R_pi/3 = ")
print(R_pi_div_3)