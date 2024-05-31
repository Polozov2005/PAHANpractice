import numpy as np

def alpha(f):
    f = float(f)
    p = np.pi

    integrand = lambda t: np.square(np.sin(2*p*f*t) + 0.1 * np.sin(6*p*f*t))

    integral = integrate(integrand, 0, 1/f)

    result = np.power(f*integral, -0.5)

    return result

def integrate(function, a, b):
    integral = 0
    x = a
    h = np.power(10.0, -5)

    while x < b:
        integral += function(x) * h
        x += h

    return integral