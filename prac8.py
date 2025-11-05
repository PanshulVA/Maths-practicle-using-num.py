import numpy as np
import sympy as sp

NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))
print("Enter the entries in a single line (separated by space):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(NR, NC)

M = sp.Matrix(A)

print("\nOriginal vectors (columns of A):")
print(M)

Q, R = M.QRdecomposition()

print("\nOrthonormal Basis (Q):")
print(Q)

print("\nR matrix (upper triangular):")
print(R)

print("\nVerification (Q * R should equal A):")
print(Q * R)
