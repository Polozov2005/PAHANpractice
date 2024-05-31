import numpy as np

def U_0(alpha, U):
    alpha = float(alpha)
    U = float(U)

    result = alpha * U

    return result

def u(t, f, U_0):
    f = float(f)
    U_0 = float(U_0)
    p = np.pi

    result = U_0 * np.sin(2 * p * f * t) + 0.1 * U_0 * np.sin(6 * p * f * t)

    return result

def T(f):
    result = 1 / float(f)

    return result