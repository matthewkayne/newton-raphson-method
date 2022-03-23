from sympy import *
from newton_raphson import nr

# Where f(X) = equation

x = Symbol('x')

result = nr((ln(x)+E**x), 1, 3)

print(result)
