import numpy as np
x=np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]])
print("Matrix x is as afollows:",x)

y=np.matrix([[9,8,7],
             [6,5,4],
             [3,2,1]])
print("Matrix y is as afollows:",y)

print("Addition of matrices X & Y is as follows:")
result1= np.array(x) + np.array(y)
print(result1)

print("Difference of matrices X & Y is as follows:")
result2= np.array(x) - np.array(y)
print(result2)

print("Multiplication of matrices X & Y is as follows:")
result3= np.dot(x,y)
print(result3)

print("The transpose of matrix x is:")
print(np.transpose(x))
