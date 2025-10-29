import numpy as np

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]], dtype=float)
B=np.array([[5,4,3],
            [8,2,6],
            [1,7,9]], dtype=float)

print("Original Matrix:\n", A)
print("\nTranspose:\n", A.T)
print("\nConjugate Transpose:\n", np.conjugate(A.T))