import numpy as np
import sympy as sp

NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))
print("Enter the entries in a single line (separated by space):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(NR, NC)

M = sp.Matrix(A)

try:
    P, D = M.diagonalize()
    print("Matrix is diagonalizable.")
    print("\nP (Eigenvectors):\n", P)
    print("\nD (Eigenvalues):\n", D)
except:
    print("Matrix is not diagonalizable.")

print("\nCayley-Hamilton Theorem:")
p = M.charpoly()
print("Characteristic Polynomial:", p.as_expr())
result = p.as_expr().subs(sp.Symbol('lambda'), M)
if result == sp.zeros(*M.shape):
    print("p(A) = 0 ✓ Cayley-Hamilton theorem verified!")
else:
    print("Cayley-Hamilton theorem not satisfied.")
