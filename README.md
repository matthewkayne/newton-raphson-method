# Newton Raphson

Solves a functions root using the Newton-Raphson method. It requires three parameters, the function, the x₀ value, and the number of iterations.

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
