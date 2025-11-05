import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

M = sp.Matrix(A)
print("Column Space Basis:\n", M.columnspace())
print("\nRow Space Basis:\n", M.rowspace())

print("\n3. Null Space Basis:")
null = M.nullspace()
print(null if null else "{ 0 } (only zero vector)")

print("\n4. Left Null Space Basis:")
left_null = M.T.nullspace()
print(left_null if left_null else "{ 0 } (only zero vector)")
