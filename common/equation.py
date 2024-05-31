import numpy as np

def I_m(alpha, phi):
    alpha = float(alpha)
    phi = float(phi)

    result = alpha * phi

    return result

def i(t, I_m):
    e = np.e

    result = I_m * np.power(e, -t/170*e-6)

    return result