import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]])

M = sp.Matrix(A)
print("Matrix:\n", M)
print("\nCofactor Matrix:\n", M.cofactor_matrix())
print("\nDeterminant:", M.det())
print("\nAdjoint (Adjugate):\n", M.adjugate())
if M.det() != 0:
    print("\nInverse:\n", M.inv())
else:
    print("\nMatrix is singular, inverse does not exist.")