# -*- coding: utf-8 -*-
"""522H0148_PhamDangThanhTrung_lab8_9_B2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gX6HGq-I9aRcOukjZ0h74XPltYP-q0Py
"""

import numpy as np
import matplotlib.pyplot as plt
#cau9
# 1st row is x-values, and 2nd row is y-values
pts = np.array(
       [[0, 1, 3, 3, 4, 4, 5, 6, 5, 5, 3, 3, 2, 2, 1, 1, 0],
		    [2, 3, 3, 4, 4, 3, 3, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2]])

#This is just an example, you must draw the house in the Ex9

plt.plot(pts[0], pts[1],'r-')  #'b-' #Hình ban đầu
dx = 2 # set translation values
dy = 4

transV = [[dx], [dy]]
trans_pts = np.add(transV, pts) #Phép tịnh tiến :(0,2) -> (2,6); (1,3) -> (3,7) ...

plt.plot(trans_pts[0], trans_pts[1],'go-') #Hình sau khi tinh tien
plt.title("Translation")

plt.show()

#b
#dung pi/2 nó sẽ vuông góc
R=np.array([[np.cos(np.pi/3),-np.sin(np.pi/3)],
            [np.sin(np.pi/3),np.cos(np.pi/3)]])

mtrB=np.matmul(R,pts)

plt.plot(pts[0], pts[1],'r-') 
plt.plot(mtrB[0], mtrB[1],'go-') 

plt.title("Rotation")
plt.show()

#c
Sx=2
Sy=3
C=np.array([[Sx,0],[0,Sy]])

mtrC=np.matmul(C,pts)

plt.plot(pts[0],pts[1],'r-')
plt.plot(mtrC[0],mtrC[1],'go-')
plt.title("Scalling")
plt.show()
#d
Shearx=0.5
Sheary=-1.5
D=np.array([[1,Shearx],[Sheary,1]])

mtrD=np.matmul(D,pts)

plt.plot(pts[0],pts[1],'blue')
plt.plot(mtrD[0],mtrD[1],'p-')

plt.title("Shear")
plt.show()
#9d của thầy:
Sx = 0.5 # set Scaling values
Sy = -1.5
#transR = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
#print(transR)
Shearx = np.array([[1, 0],[Sx, 1]])
Sheary = np.array([[1, Sy],[0, 1]])
#trans_pts = np.matmul(Shearx, pts)
trans_pts = np.matmul(Sheary, pts)
print("trans_pts = ",trans_pts)
plt.plot(pts[0], pts[1],'r-')  #'b-'
plt.plot(trans_pts[0], trans_pts[1],'go-')
plt.title("Translation")
plt.show()

#test
Shearx=0.001
Sheary=-500
D=np.array([[1,Shearx],[Sheary,1]])

mtrD=np.matmul(D,pts)

plt.plot(pts[0],pts[1],'blue')
plt.plot(mtrD[0],mtrD[1],'p-')

plt.title("Shear")
plt.show()

import numpy as np
import matplotlib.pyplot as plt


pts=np.array([[1,3,1,1],
              [1,1,3,1]])
I=np.eye(2)
I_pts=np.matmul(-I,pts)
plt.plot(pts[0],pts[1],'r-')
plt.plot(I_pts[0],I_pts[1],'go-')
plt.title("Translation")
plt.show()

#cau11
import numpy as np
import matplotlib.pyplot as plt

# 1st row is x-values, and 2nd row is y-values
pts = np.array(
       [[2, 2, -3, -3, -2,   -2,    0, 0.0, -2.0, -2, 2],
		    [4, 5,  5, -5, -5, -0.5, -0.5, 0.5,  0.5,  4, 4]])
pts = np.vstack( (pts, np.ones(pts.shape[1]) ) )

print(pts)

T2 = [[-1,  0, 0],
      [ 0, -1, 0],
      [ 0,  0, 1]]
transform_pts = np.matmul( T2, pts )

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

plt.fill(pts[0], pts[1],'b')
plt.fill(transform_pts[0], transform_pts[1],'r')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(linestyle = '--')

plt.show()

