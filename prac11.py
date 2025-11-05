import sympy as sp

x, y, z = sp.symbols('x y z')

expr_input = input("Enter scalar function f(x,y,z): ").strip()
if expr_input == "":
    expr_input = "x**2*y + sin(z)"
    
f = sp.sympify(expr_input)

print("\nFunction f(x,y,z) =", f)

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
df_dz = sp.diff(f, z)

print("\nGradient ∇f = [∂f/∂x, ∂f/∂y, ∂f/∂z]")
print("∂f/∂x =", df_dx)
print("∂f/∂y =", df_dy)
print("∂f/∂z =", df_dz)

print("\n∇f =", [df_dx, df_dy, df_dz])
