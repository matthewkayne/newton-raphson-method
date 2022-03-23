# Newton Raphson Method

Solves a functions root using the Newton-Raphson method. It requires three parameters, the function, the x₀ value, and the number of iterations.

Run [real_time_graph.py](https://github.com/matthewkayne/newton-raphson-method/blob/master/real_time_graph.py) to see a graphical visualisation of the method

Start by importing the function and sympy:

```python
from sympy import *
from newton_raphson import nr
```

Then setup your `x` symbol:

```python
x = Symbol('x')
```

Finally call the Newton-Raphson function

```python
nr((x**3 + 2*x - 2)), 1, 3)
```

See [example.py](https://github.com/matthewkayne/newton-raphson-method/blob/master/example.py) for a functional example
