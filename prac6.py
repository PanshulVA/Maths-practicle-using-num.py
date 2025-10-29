import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]])

M = sp.Matrix(A)
print("Column Space Basis:\n", M.columnspace())
print("\nRow Space Basis:\n", M.rowspace())
print("\nNull Space Basis:\n", M.nullspace())
print("\nLeft Null Space Basis:\n", M.T.nullspace())
