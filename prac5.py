import numpy as np
import sympy as sp

NR = int(input("Enter the number of equations: "))
NC = int(input("Enter the number of variables: "))
print("Enter the coefficients in a single line (separated by space):")
entries = list(map(int, input().split()))
A = np.array(entries).reshape(NR, NC)
M = sp.Matrix(A)

print("\nOriginal Coefficient Matrix A:")
print(M)

RREF, pivot_cols = M.rref()

print("\nReduced Row Echelon Form (RREF):")
print(RREF)

print("\nPivot columns:", pivot_cols)

print("\nSolution (Null Space Basis):")
null_space = M.nullspace()
if null_space:
    print("The system has infinitely many solutions:")
    for i, vec in enumerate(null_space, 1):
        print(f"\nBasis vector {i}:")
        print(vec)
else:
    print("{ 0 } (only trivial solution: all variables = 0)")
