"""Newton-Raphson Graph"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, diff
from sympy.utilities.lambdify import lambdify
from newton_raphson import nr


def graph(function, x_value, iterations):
    """Graph"""

    result = nr(function, x_value, iterations)

    x_np = np.linspace(-2, 2, 100)

    y = x_np
    plt.plot(x_np, y, 'b', label='x')

    x_symbol = Symbol('x')

    lam_x = lambdify(x, (function), modules=['numpy'])

    y_vals = lam_x(x_np)
    plt.plot(x_np, y_vals, label=f"{function}")

    plt.legend()
    plt.grid(True, linestyle=':')
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])

    plt.title('Newton-Raphson Method')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    result_list = list(result.values())

    print(result_list)

    def slope(x_value):
        """Slope"""
        return diff(function, x_symbol).subs(x_symbol, x_value)

    for i, _ in enumerate(result_list):
        x1 = result_list[i]
        y1 = function.subs(x_symbol, x1)
        y = slope(result_list[i]) * (x_np-x1) + y1

        plt.plot(x_np, y, 'C1--', linewidth=2)
        plt.pause(1.5)

    # Show plot
    plt.show()


x = Symbol('x')
graph((2*x**3+x**2-1), 0.5, 4)
