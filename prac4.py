import numpy as np
import sympy as sp

NR = int(input("Enter number of equations (rows of A): "))
NC = int(input("Enter number of variables (columns of A): "))

if NR != NC:
    print("Error: For Gauss/LU solve, A must be a square matrix!")
    exit()

print("Enter the entries of matrix A (row-wise, space-separated):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(NR, NC)

print("Enter the entries of vector b (one value per row):")
entries2 = list(map(float, input().split()))

if len(entries2) != NR:
    print("Error: b must have the same number of rows as A!")
    exit()

b = np.array(entries2).reshape(NR, 1)

M = sp.Matrix(A)
b_vec = sp.Matrix(b)

print("\nMatrix A:")
print(M)
print("\nVector b:")
print(b_vec)

try:
    sol = M.LUsolve(b_vec)
    print("\nSolution x:")
    print(sol)
except Exception as e:
    print("\nMatrix A is singular or system not solvable using LU decomposition.")
    print("Error:", e)

