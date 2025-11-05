import numpy as np
import sympy as sp

NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))
print("Enter the entries in a single line (separated by space):")
entries = list(map(int, input().split()))
A = np.array(entries).reshape(NR, NC)
M = sp.Matrix(A)

print("\nMatrix A:")
print(M)

print("\n1. Linear Dependence:")
if M.rank() == M.shape[1]:
    print("Linearly independent")
else:
    print("Linearly dependent")

print(f"\n2. Enter {NC} coefficients (separated by space):")
coeffs = list(map(int, input().split()))
result = M * sp.Matrix(coeffs)
print("Linear combination result:")
print(result)

if input("\n3. Find transition matrix? (y/n): ").lower() == 'y':
    print(f"Enter new basis ({NR}x{NR}) entries (separated by space):")
    new_entries = list(map(int, input().split()))
    B = sp.Matrix(np.array(new_entries).reshape(NR, NR))
    print("\nTransition matrix:")
    print(B.inv())
