

import sympy as sp

# Define the variable and function
x = sp.Symbol('x')
y = x**3 - 3*x**2 + 4

# First derivative
dy_dx = sp.diff(y, x)

# Solve for critical points                           
critical_points = sp.solve(dy_dx, x)

# Second derivative
d2y_dx2 = sp.diff(dy_dx, x)

# Determine local min and max
for point in critical_points:
    second_derivative_value = d2y_dx2.subs(x, point)
    function_value = y.subs(x, point)
    if second_derivative_value > 0:
        print(f'Local Minimum at x = {point}, y = {function_value}')
    elif second_derivative_value < 0:
        print(f'Local Maximum at x = {point}, y = {function_value}')
