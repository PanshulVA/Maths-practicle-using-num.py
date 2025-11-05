import sympy as sp

x, y, z = sp.symbols('x y z')

P = input("Enter P(x,y,z): ").strip() or "x*y"
Q = input("Enter Q(x,y,z): ").strip() or "y*z"
R = input("Enter R(x,y,z): ").strip() or "z*x"

P = sp.sympify(P)
Q = sp.sympify(Q)
R = sp.sympify(R)

print("\nVector Field F = [P, Q, R] =", [P, Q, R])

div = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)

print("\nDivergence ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z")
print("∇·F =", sp.simplify(div))
