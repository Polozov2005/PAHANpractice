import numpy as np

def alpha():
    e = np.e

    C = 150 * np.power(10.0, -12)
    T = 1.7 * np.power(10.0, -6)

    integrand = lambda t: np.power(e, -t/170*e-6)

    integral = integrate(integrand, 0, T)

    result = C/integral

    return result

def integrate(function, a, b):
    integral = 0
    x = a
    h = np.power(10.0, -8)

    while x < b:
        integral += function(x) * h
        x += h

    return integral