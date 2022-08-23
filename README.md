## V2

`midpointRectangular2dim(func, a, b, c, d, nx, ny)`

$$\int_{a}^{b} \int_{c}^{d} f(x, y) d x d y = h_{x} h_{y} \sum_{i=0}^{n_{x}-1} \sum_{j=0}^{n_{y}-1} f\left(a+\frac{h_{x}}{2}+i h_{x}, c+
\frac{h_{y}}{2}+j h_{y}\right)$$

`midpointRectangular3dim(func, a, b, c, d, e, f, nx, ny, nz)`

$$\int_{a}^{b} \int_{c}^{d}\int_{e}^{f} f(x, y,z) d x d y dz = h_{x} h_{y} h_{z} \sum_{i=0}^{n_{x}-1} \sum_{j=0}^{n_{y}-1} \sum_{k=0}^{n_{z}-1} f\left(a+\frac{h_{x}}{2}+i h_{x}, c+\frac{h_{y}}{2}+j h_{y}, e+\frac{h_{z}}{2}+k h_{z}\right)$$$