# import sympy as sp
# x,y = sp.symbols('x y')
# f = x**2 * y + sp.cos(x)+sp.sin(y)

# f_x = sp.diff(f,x)
# f_y = sp.diff(f,y)

# print("partial derivative w.r.t x\n",f_x)
# print("partial derivative w.r.t x\n",f_y)

# import sympy as sp
# x = sp.symbols('x')
# integral = sp.integrate(x**2, x)  
# derivative = sp.diff(x**3 + 2*x, x)  
# A = sp.Matrix([
#     [22, 77, 11],
#     [33, 23, 89],
#     [55, 100, 100]
# ])
# det_A = A.det()
# print()
# print("Integral:", integral)
# print()
# print("Derivative:", derivative)
# print()
# print("Matrix A:")
# sp.pprint(A) 
# print()
# print(A)
# print()
# print("Determinant of A:", det_A)

import sympy as sp
#to perform jacobian matrix formula
x, y = sp.symbols('x y')
f = x**2 + y**2
g = sp.sin(x) + sp.cos(y)

# Compute the Jacobian matrix
jacobian_matrix = sp.Matrix([[sp.diff(f, x), sp.diff(f, y)],
                            [sp.diff(g, x), sp.diff(g, y)]])
print("Jacobian matrix:")
sp.pprint(jacobian_matrix)  # Pretty print the Jacobian matrix
print()

print("Jacobian matrix:")
print(jacobian_matrix)  # Print the Jacobian matrix
print()
#to perform hessian matrix formula
x, y = sp.symbols('x y')
f = x**2 + y**2 + 2*x*y


