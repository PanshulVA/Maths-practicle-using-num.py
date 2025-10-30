import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(float, input().split()))
A=(np.array(entries).reshape(NR,NC))

M = sp.Matrix(A)
Q, R = M.QRdecomposition()
print("Orthonormal Basis (Q):\n", Q)