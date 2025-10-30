import numpy as np
import sympy as sp

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

M = sp.Matrix(A)
try:
    P, D = M.diagonalize()
    print("Matrix is diagonalizable.")
    print("\nP (Eigenvectors):\n", P)
    print("\nD (Diagonal Matrix of Eigenvalues):\n", D)
except:
    print("Matrix is not diagonalizable.")

    p = M.charpoly()
    print("\nCharacteristic Polynomial:", p.as_expr())
    print("Verifying Cayley-Hamilton Theorem...")
    cayley_hamilton_result = p.eval(M)
    print("p(A) =\n", cayley_hamilton_result)
    if cayley_hamilton_result == sp.zeros(*M.shape):
        print("Cayley-Hamilton theorem verified successfully!")
    else:
        print("Cayley-Hamilton theorem not satisfied (possible rounding or symbolic issue).")