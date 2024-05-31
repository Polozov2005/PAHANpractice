import numpy as np
from scipy import integrate

def alpha(f):
    f = float(f)
    p = np.pi

    integrand = lambda t: np.square(np.sin(2*p*f*t) + 0.1 * np.sin(6*p*f*t))

    integral = integrate.quad(integrand, 0, 1/f)

    result = np.power(f*integral[0], -0.5)

    return result