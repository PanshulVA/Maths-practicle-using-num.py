import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

print("Enter the entries in a single line (seperated by space) (Just 3 elements)")
NR2= int(input("Enter the number of rows:"))
NC2= int(input("Enter the number of columns:"))
entries2 = list (map(int, input().split()))
B=np.array(entries2).reshape(NR2,NC2)

M = sp.Matrix(A)
b= sp.Matrix(B)
print("Solution x:\n", M.LUsolve(b))