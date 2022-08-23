import pandas as pd
import os
import sys


def midpointRectangular1dim(func, a, b, n):
    integral_sum = 0
    for i in range(int(n)):
        integral_sum += func(a + (b-a)/n * i)
    return float(integral_sum/n)

def adaptiveMidpointRectangular1dim(func, a, b, n):
    pass

def midpointRectangular2dim(func, a, b, c, d, nx, ny):
    def q(x):
        return midpointRectangular1dim(lambda y: func(x, y), c, d, ny)
    return midpointRectangular1dim(q, a, b, nx)


def midpointRectangular3dim(func, a, b, c, d, e, f, nx, ny, nz):
    def r(x):
        return midpointRectangular2dim(lambda y, z: func(x, y, z), c, d, e, f, ny, nz)

    return midpointRectangular1dim(r, a, b, nx)


def midpointRectangular4dim(func, a, b, c, d, e, f, g, h, nx, ny, nz, nw):
    def r(x):
        return midpointRectangular3dim(lambda y, z, w: func(x, y, z, w), c, d, e, f, g, h, ny, nz, nw)
    return midpointRectangular1dim(r, a, b, nx)


def main():
    def func(x):
        return x**x
    print(midpointRectangular1dim(func, 0, 4, 9e8))

    # def func(x, y):
    #     return x**2 + y**2
    # print(midpointRectangular2dim(func, 1, 2, 1, 2, 999, 999))

    # def func(x, y, z):
    #     return x**2 + y**2 + z**3
    # print(midpointRectangular3dim(func, 1, 2, 1, 2, 1, 2, 150, 150, 150))

    # def func(x, y, z, w):
    #     return x**2 + y**2 + z**3 + w**4
    # print(midpointRectangular4dim(func, 1, 2, 1, 2, 1, 2, 1, 2, 10, 10, 10, 10))

    return


if __name__ == "__main__":
    main()
