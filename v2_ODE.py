import math


def ODEForwardEuler(f, target_t, t0, N0, number_of_step):
    Ns = [N0]
    ts = [t0]
    step = float((target_t - t0)/int(number_of_step))
    for i in range(int(number_of_step)):
        Ns.append(Ns[-1] + step * f(Ns[-1], ts[-1]))
        ts.append(ts[-1] + step)
    return Ns, ts


def ODEplot(Ns, ts):
    import matplotlib.pyplot as plt

    plt.plot(ts, Ns, 'r--')
    # plt.plot(ts, Ns, 'bs')
    # plt.plot(ts, Ns, 'g^')
    plt.show()
    return None

def main():
    def func(y, t):
        return 2 - math.exp(-4*t) - 2*y
    print(ODEForwardEuler(func, 0.5, 0, 1, 10))
    
    Ns, ts = ODEForwardEuler((lambda y, t: 2 - math.exp(-4*t) - 2*y), 0.5, 0, 1, 100)
    ODEplot(Ns, ts)
    return


if __name__ == "__main__":
    main()