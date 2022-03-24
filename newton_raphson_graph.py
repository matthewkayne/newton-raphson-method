import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from sympy import Symbol, diff
from newton_raphson import nr
from sympy.utilities.lambdify import lambdify


def graph(function, x_value, iterations):

    result = nr(function, x_value, iterations)

    x = np.linspace(-2, 2, 100)

    plt.subplots_adjust(bottom=0.2)

    y = x
    plt.plot(x, y, 'b', label='x')

    x = Symbol('x')

    lam_x = lambdify(x, (function), modules=['numpy'])

    x_vals = linspace(-2, 2, 100)
    y_vals = lam_x(x_vals)
    plt.plot(x_vals, y_vals, label=f"{function}")

    plt.legend()
    plt.grid(True, linestyle=':')
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])

    plt.title('Newton-Raphson Method')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    x = np.linspace(-2, 2, 100)

    result_list = list(result.values())

    print(result_list)
    x_symbol = Symbol('x')

    def slope(x_value):
        return diff(function, x_symbol).subs(x_symbol, x_value)

    for i in range(len(result_list)):
        x1 = result_list[i]
        y1 = function.subs(x_symbol, x1)
        y = slope(result_list[i]) * (x-x1) + y1

        plt.plot(x, y, 'C1--', linewidth=2)
        plt.pause(1.5)

    # Show plot
    plt.show()


x = Symbol('x')
graph((2*x**3+x**2-1), 0.5, 4)
