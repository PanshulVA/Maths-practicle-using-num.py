import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(float, input().split()))
A=np.array(entries).reshape(NR,NC)
M = sp.Matrix(A)

print("Matrix:\n", M)
print("\nCofactor Matrix:\n", M.cofactor_matrix())
print("\nDeterminant:", M.det())
print("\nAdjoint (Adjugate):\n", M.adjugate())
if M.det() != 0:
    print("\nInverse:\n", M.inv())
else:
    print("\nMatrix is singular, inverse does not exist.")
