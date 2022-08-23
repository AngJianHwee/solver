from math import *
from inspect import getsource
import numpy as np


def firstOrderODESolver(func, t0, y0, target_t, num_iter=20, method='forward_euler'):
    ts = [t0]
    ys = [y0]
    target_t = target_t
    num_iter = int(num_iter)
    h = (target_t - ts[-1])/num_iter

    # print("==========================================================================")
    print("-------------------------------------")
    print("\tSolving: y' =", end="")
    print("\n".join([x.strip().replace("return", "") for x in getsource(
        func).split("\n")[1:-1] if not x.strip().startswith("#")]))
    print(f"\tMethod : {method}")
    print(f"\t(t0, y0) = ({t0},{y0})")
    print(f"\tTarget_t = {target_t}")
    print(f"\tNumber of iteration = {num_iter}")
    print("-------------------------------------")
    print(f"Iter {str(0).rjust(len(str(num_iter)))}: t = {ts[-1]:.6f}, y = {ys[-1]:.6f}")

    for _ in range(num_iter):
        if method == 'forward_euler':
            ys.append(ys[-1]+h*func(ts[-1], ys[-1]))
        # elif method == 'backward_euler':
            # ys.append(ys[-1]+h*func(ts[-1], ys[-1]))
        ts.append(ts[-1]+h)
        print(f"Iter {str(len(ys)-1).rjust(len(str(num_iter)))}: t = {ts[-1]:.6f}, y = {ys[-1]:.6f}")
    # print("==========================================================================\n")
    print()
    return ts, ys


def oneDimUnivariateIntegrationSolver(func, a, b, num_iter=20, method='midpoint'):
    # print("==========================================================================")
    print("-------------------------------------")
    print("\tIntegrating: f(x) =", end="")
    print("\n".join([x.strip().replace("return", "") for x in getsource(
        func).split("\n")[1:-1] if not x.strip().startswith("#")]))
    print(f"\tMethod : {method}")
    print(f"\t(a, b) = ({a}, {b})")
    print(f"\tNumber of iteration = {num_iter}")
    print("-------------------------------------")
    if method == 'midpoint':
        xs = [a + ((b-a)/num_iter*i + (b-a)/num_iter*(i+1)) /
              2 for i in range(num_iter)]
        coefficients = [1 for i in range(num_iter)]
        denominator = 1
    elif method == 'trapezoidal':
        xs = [a + (b-a)/num_iter*i for i in range(num_iter+1)]
        coefficients = [1 if (i == 0) or (i == num_iter)
                        else 2 for i in range(num_iter+1)]
        denominator = 2
    elif method == 'simpson':
        xs = [a + (b-a)/num_iter*i for i in range(num_iter+1)]
        coefficients = [1 if (i == 0) or (i == num_iter) else (
            i % 2+1) * 2 for i in range(num_iter+1)]
        denominator = 3
    ys = []
    for i in range(len(xs)):
        ys.append(func(xs[i]))
        print(f"Summ {str(len(ys)-1).rjust(len(str(num_iter)))}: x = {xs[i]:.6f}, y = {ys[-1]:.6f}, coefficient = {coefficients[i]:1d}")
    ans = sum([y*coefficient for y, coefficient in zip(ys, coefficients)]
              ) * float((b-a)/denominator/num_iter)
    print(f"Final result: {ans:.6f}")
    # print("==========================================================================")
    print()
    return ys, ans


def main():
    def func(x):
        return sqrt(1+x**2)

    oneDimUnivariateIntegrationSolver(func, 1, 4,
                                      num_iter=6,
                                      method='simpson')

    def firstOrderODE(t, y):
        return t**2 - 4*y

    firstOrderODESolver(firstOrderODE, t0=0,
                        y0=1, target_t=0.1)


if __name__ == "__main__":
    main()
