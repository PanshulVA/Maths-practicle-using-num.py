import numpy as np
NR=int(input("Enter no. of rows: "))
NC=int(input("Enter no. of columns: "))

print("Enter the entries in a single line (seperated by space): ")

entries = list(map(int, input().split ()))

matrix=np.array(entries).reshape(NR,NC)
print("Matrix is as follows:",'\n', matrix)
print("Transpose of matrix X is as follows:",'\n', np.transpose(matrix))    
