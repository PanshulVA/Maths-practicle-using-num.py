import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]])

M = sp.Matrix(A)

if M.rank() == M.shape[1]:
    print("The columns of A are linearly independent.")
else:
    print("The columns of A are linearly dependent.")