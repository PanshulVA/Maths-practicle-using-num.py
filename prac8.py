import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]], dtype=float)
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]])

M = sp.Matrix(A)
Q, R = M.QRdecomposition()
print("Orthonormal Basis (Q):\n", Q)