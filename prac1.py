import numpy as np

NR= int(input("Enter the number of rows:"))
NC= int(input("Enter the number of columns:"))
print("Enter the entries in a single line (seperated by space)")
entries = list (map(int, input().split()))
A=np.array(entries).reshape(NR,NC)

print("Original Matrix:\n", A)
print("\nTranspose:\n", A.T)
print("\nConjugate Transpose:\n", np.conjugate(A.T))