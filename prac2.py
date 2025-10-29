import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]], dtype=float)
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]], dtype=float)

M=sp.Matrix(A)
rref_matrix, pivots = M.rref()

print("Row Echelon Form (RREF):\n", rref_matrix)
print("Rank of Matrix:", M.rank())
print("Pivot Columns:", pivots)
