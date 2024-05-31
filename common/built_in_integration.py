import numpy as np
from scipy import integrate

def alpha():
    e = np.e

    C = 150 * np.power(10.0, -12)
    T = 1.7 * np.power(10.0, -6)

    integrand = lambda t: np.power(e, -t/170*e-6)

    integral = integrate.quad(integrand, 0, T)

    result = C/integral[0]

    return result