import sympy as sp

x, y, z = sp.symbols('x y z')
P = input("Enter P(x,y,z) [default: x*y]: ").strip()
Q = input("Enter Q(x,y,z) [default: y*z]: ").strip()
R = input("Enter R(x,y,z) [default: z*x]: ").strip()

if P == "": P = "x*y"
if Q == "": Q = "y*z"
if R == "": R = "z*x"

P = sp.sympify(P)
Q = sp.sympify(Q)
R = sp.sympify(R)
div = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)
print("\nVector Field F =", (P, Q, R))
print("Divergence ∇·F =", sp.simplify(div))