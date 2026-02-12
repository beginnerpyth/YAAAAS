import numpy as np
import pandas as pd
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20])
#i dont tthis work cause a is (2,3) and b is (1,2)
x=np.array([[[1,2,3],[4,5,6]]])
print(x.sum(axis=0))#i think (6,15)
print(x.sum(axis=1))#i think(5,7,9)
arr=np.array([])
print(arr**2)
arr=np.array([5,12,25,40,60])
g=arr[(arr>10)&(arr<50)]
print(g)
h=np.where(arr[arr>50],-1,22)
#q5 it fails because arange is within 12 and when reshape (5,3) it becomes 15
a=np.arrange(12)
b=a.reshape(3,4)
#q6
a=np.array([[1,2],[3,4]])
b=np.array([[5],[6]])
np.matmul(a,b)#it gives ius 2*1 and matmul it needs toi be same elements in column and riw 
a*b#(i dont know what it gives)
