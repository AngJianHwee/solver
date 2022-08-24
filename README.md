## `v2_integral.py`

#### `midpointRectangular1D(func, a, b, n)`

$$\int_{a}^{b} f(x) d x = h_{x} \sum_{i=0}^{n_{x}-1} f\left(a+\frac{h_{x}}{2}+i h_{x}\right)$$
Example:

```
def func(x):
    return x**2
midpointRectangular1D(func, 1,2, 1e5)
>
```

#### `midpointRectangular2dim(func, a, b, c, d, nx, ny)`

$$\int_{a}^{b} \int_{c}^{d} f(x, y) d x d y = h_{x} h_{y} \sum_{i=0}^{n_{x}-1} \sum_{j=0}^{n_{y}-1} f\left(a+\frac{h_{x}}{2}+i h_{x}, c+
\frac{h_{y}}{2}+j h_{y}\right)$$
Example:

```
def func(x, y):
        return x**2 + y**2

midpointRectangular2D(func, 1, 2, 1, 2, 1e5, 1e5)
> 4.663663997664667
```

#### `midpointRectangular3D(func, a, b, c, d, e, f, nx, ny, nz)`

$$\int_{a}^{b} \int_{c}^{d}\int_{e}^{f} f(x, y,z) d x d y dz = h_{x} h_{y} h_{z} \sum_{i=0}^{n_{x}-1} \sum_{j=0}^{n_{y}-1} \sum_{k=0}^{n_{z}-1} f\left(a+\frac{h_{x}}{2}+i h_{x}, c+\frac{h_{y}}{2}+j h_{y}, e+\frac{h_{z}}{2}+k h_{z}\right)$$
Example:

```
def func(x, y, z):
    return x**2 + y**2 + z**2
midpointRectangular3D(func, 1, 2, 1, 2, 1, 2, 1e5, 1e5, 1e5)
> 
```
