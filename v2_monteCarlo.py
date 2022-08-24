import numpy as np


def monteCarloRectangular1D(func, a, b, n):
    n = int(n)

    x = np.random.uniform(a, b, n)
    integral_sum = 0

    for i in range(len(x)):
        integral_sum += func(x[i])
    return float((b-a) * integral_sum/n)


def monteCarloRectangular2D(func, a, b, c, d, n):
    n = int(n)

    x = np.random.uniform(a, b, n)
    y = np.random.uniform(c, d, n)
    integral_sum = 0

    for i in range(len(x)):
        integral_sum += func(x[i], y[i])
    return float((b-a) * (d-c) * integral_sum/n)


def monteCarloRestrictFunc1D(func, restrict_func, a, b, n):
    n = int(n)

    x = np.random.uniform(a, b, n)
    integral_sum = 0
    restrict_count = 0

    for i in range(len(x)):
        if restrict_func(x[i]) > 0:
            restrict_count += 1
            integral_sum += func(x[i])
    return float((b-a) * integral_sum/restrict_count)


def monteCarloRestrictFunc2D(func, restrict_func, a, b, c, d, n):
    n = int(n)

    x = np.random.uniform(a, b, n)
    y = np.random.uniform(c, d, n)
    integral_sum = 0
    restrict_count = 0

    for i in range(len(x)):
        if restrict_func(x[i], y[i]) > 0:
            restrict_count += 1
            integral_sum += func(x[i], y[i])
    return float((b-a) * (d-c) * integral_sum/n)


def main():
    def func(x):
        return x**x
    print(monteCarloRectangular1D(func, 1, 2, 1e5))

    def func(x, y):
        return x**x+y**2
    print(monteCarloRectangular2D(func, 1, 2, 3, 4, 1e5))
    return


if __name__ == "__main__":
    main()
