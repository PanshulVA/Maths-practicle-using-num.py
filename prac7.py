import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

M = sp.Matrix(A)

if M.rank() == M.shape[1]:
    print("The columns of A are linearly independent.")
else:
    print("The columns of A are linearly dependent.")