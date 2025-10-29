import numpy as np
import sympy as sp

A=np.array([[4,8,2],
            [7,9,6],
            [1,5,3]])
B=np.array([5,4,2])
M = sp.Matrix(A)
b= sp.Matrix(B)
print("Solution x:\n", M.LUsolve(b))