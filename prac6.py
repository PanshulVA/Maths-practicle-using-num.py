import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

M = sp.Matrix(A)
print("Column Space Basis:\n", M.columnspace())
print("\nRow Space Basis:\n", M.rowspace())
print("\nNull Space Basis:\n", M.nullspace())
print("\nLeft Null Space Basis:\n", M.T.nullspace())
