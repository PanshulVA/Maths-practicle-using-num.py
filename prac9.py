import numpy as np
import sympy as sp

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]], dtype=float)
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]])

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