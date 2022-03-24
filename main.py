from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

import numpy as np
from numpy import linspace
from sympy import Symbol, diff, parse_expr, sympify
from newton_raphson import nr
from sympy.utilities.lambdify import lambdify

x = Symbol('x')


def plot():

    global graph

    function = sympify(input_function.get(1.0, "end-1c"))
    x_value = int(input_x_value.get(1.0, "end-1c"))
    iterations = int(input_iterations.get(1.0, "end-1c"))
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    plot1 = fig.add_subplot(111)

    result = nr(function, x_value, iterations)

    x = np.linspace(-2, 2, 100)
    print(x)
    y = x
    plot1.plot(x, y, 'b', label='x')

    x = Symbol('x')

    lam_x = lambdify(x, (function), modules=['numpy'])

    x_vals = linspace(-2, 2, 100)
    y_vals = lam_x(x_vals)
    plot1.plot(x_vals, y_vals, label=f"{function}")

    plot1.legend()
    plot1.grid(True, linestyle=':')

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

        plot1.plot(x, y, 'C1--', linewidth=2)

    # creating the Tkinter canvas
    # containing the Matplotlib figure

    canvas = FigureCanvasTkAgg(fig,
                               master=window)

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()

# setting the title
window.title('Newton-Raphson Method')

# dimensions of the main window
window.geometry("500x500")

label_function = Label(window, text="f(x):")
label_function.pack()

input_function = Text(window,
                      height=2,
                      width=15)
input_function.pack()

label_x_value = Label(window, text="Starting x Value:")
label_x_value.pack()

input_x_value = Text(window,
                     height=2,
                     width=15)
input_x_value.pack()


label_iterations = Label(window, text="Iterations:")
label_iterations.pack()

input_iterations = Text(window,
                        height=2,
                        width=15)
input_iterations.pack()

# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()
