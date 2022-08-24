import pandas as pd
import os
import sys


def adaptiveMidpointRectangular1D(func, a, b, n):
    pass

def midpointRectangular1D(func, a, b, n):
    n = int(n)
    
    integral_sum = 0
    for i in range(int(n)):
        integral_sum += func(a + (b-a)/n * i)
    return float(integral_sum/n)

def midpointRectangular2D(func, a, b, c, d, nx, ny):
    nx = int(nx)
    ny = int(ny)
    
    def q(x):
        return midpointRectangular1D(lambda y: func(x, y), c, d, ny)
    return midpointRectangular1D(q, a, b, nx)


def midpointRectangular3D(func, a, b, c, d, e, f, nx, ny, nz):
    nx = int(nx)
    ny = int(ny)
    nz = int(nz)

    def r(x):
        return midpointRectangular2D(lambda y, z: func(x, y, z), c, d, e, f, ny, nz)

    return midpointRectangular1D(r, a, b, nx)


def midpointRectangular4D(func, a, b, c, d, e, f, g, h, nx, ny, nz, nw):
    nx = int(nx)
    ny = int(ny)
    nz = int(nz)
    nw = int(nw)

    def r(x):
        return midpointRectangular3D(lambda y, z, w: func(x, y, z, w), c, d, e, f, g, h, ny, nz, nw)
    return midpointRectangular1D(r, a, b, nx)


def main():
    def func(x):
        return x**2
    print(midpointRectangular1D(func, 1,2, 1e5))

    def func(x, y):
        return x**2 + y**2
    print(midpointRectangular2D(func, 1, 2, 1, 2, 1e5, 1e5))

    def func(x, y, z):
        return x**2 + y**2 + z**3
    print(midpointRectangular3D(func, 1, 2, 1, 2, 1, 2, 150, 150, 150))

    def func(x, y, z, w):
        return x**2 + y**2 + z**3 + w**4
    print(midpointRectangular4D(func, 1, 2, 1, 2, 1, 2, 1, 2, 10, 10, 10, 10))

    return


if __name__ == "__main__":
    main()
