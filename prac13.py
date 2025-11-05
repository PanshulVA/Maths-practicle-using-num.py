import sympy as sp

x, y, z = sp.symbols('x y z')

P = input("Enter P(x,y,z): ").strip() or "y*z"
Q = input("Enter Q(x,y,z): ").strip() or "z*x"
R = input("Enter R(x,y,z): ").strip() or "x*y"

P = sp.sympify(P)
Q = sp.sympify(Q)
R = sp.sympify(R)

print("\nVector Field F = [P, Q, R] =", [P, Q, R])

curl_x = sp.diff(R, y) - sp.diff(Q, z)
curl_y = sp.diff(P, z) - sp.diff(R, x)
curl_z = sp.diff(Q, x) - sp.diff(P, y)

print("\nCurl ∇×F = [∂R/∂y - ∂Q/∂z, ∂P/∂z - ∂R/∂x, ∂Q/∂x - ∂P/∂y]")
print("\n∇×F =", [sp.simplify(curl_x), sp.simplify(curl_y), sp.simplify(curl_z)])
