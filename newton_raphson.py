from sympy import *


def nr(function, x_value, iterations):
    x = Symbol('x')

    results = {"x0": x_value}

    for i in range(iterations):
        x_value = x_value - ((function.subs(x, x_value)) /
                             (diff(function, x).subs(x, x_value)))
        results["x"+str(i+1)] = x_value.evalf()

    return results
