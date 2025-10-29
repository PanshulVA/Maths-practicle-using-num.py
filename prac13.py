import sympy as sp

x, y, z = sp.symbols('x y z')

P = input("Enter P(x,y,z) [default: y*z]: ").strip()
Q = input("Enter Q(x,y,z) [default: z*x]: ").strip()
R = input("Enter R(x,y,z) [default: x*y]: ").strip()

if P == "": P = "y*z"
if Q == "": Q = "z*x"
if R == "": R = "x*y"

P = sp.sympify(P)
Q = sp.sympify(Q)
R = sp.sympify(R)

curl_x = sp.diff(R, y) - sp.diff(Q, z)
curl_y = sp.diff(P, z) - sp.diff(R, x)
curl_z = sp.diff(Q, x) - sp.diff(P, y)

print("\nVector Field F =", (P, Q, R))
print("Curl ∇×F = [∂R/∂y - ∂Q/∂z, ∂P/∂z - ∂R/∂x, ∂Q/∂x - ∂P/∂y]")
print("∂R/∂y - ∂Q/∂z =", curl_x)
print("∂P/∂z - ∂R/∂x =", curl_y)
print("∂Q/∂x - ∂P/∂y =", curl_z)