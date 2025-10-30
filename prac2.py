import numpy as np
import sympy as sp
NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)


M=sp.Matrix(A)
rref_matrix, pivots = M.rref()

print("Row Echelon Form (RREF):\n", rref_matrix)
print("Rank of Matrix:", M.rank())
print("Pivot Columns:", pivots)
