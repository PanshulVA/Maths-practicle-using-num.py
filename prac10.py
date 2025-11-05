import numpy as np
import sympy as sp
n = int(input("Enter matrix size: "))
print(f"Enter {n*n} entries (separated by space):")
entries = list(map(int, input().split()))
A = np.array(entries).reshape(n, n)
M = sp.Matrix(A)
print("\nEncoding Matrix:")
print(M)
msg = input("\nEnter message: ").upper()
print("\nOriginal Message:", msg)
nums = []
for char in msg:
    if char.isalpha():
        nums.append(ord(char) - ord('A'))
    elif char == ' ':
        nums.append(26)
while len(nums) % n != 0:
    nums.append(26)
print("As numbers:", nums)
encoded = []
for i in range(0, len(nums), n):
    block = sp.Matrix(nums[i:i+n])
    encoded_block = M * block
    encoded.extend([int(x) for x in encoded_block])
print("\nEncoded:", encoded)
M_inv = M.inv()
decoded = []
for i in range(0, len(encoded), n):
    block = sp.Matrix(encoded[i:i+n])
    decoded_block = M_inv * block
    decoded.extend([int(round(x)) for x in decoded_block])
result = ""
for num in decoded:
    if 0 <= num <= 25:
        result += chr(num + ord('A'))
    elif num == 26:
        result += ' '
print("\nDecoded Message:", result)
