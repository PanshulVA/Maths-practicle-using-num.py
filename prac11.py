import sympy as sp
x, y, z = sp.symbols('x y z')
expr_input = input("Enter scalar function f(x,y,z) [default: x**2*y + sin(z)]: ").strip()
if expr_input == "":
    expr_input = "x**2*y + sin(z)"
f = sp.sympify(expr_input)
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
df_dz = sp.diff(f, z)
print("\nFunction f(x,y,z) =", f)
print("Gradient ∇f = [∂f/∂x, ∂f/∂y, ∂f/∂z]")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)
print("∂f/∂z =", df_dz)