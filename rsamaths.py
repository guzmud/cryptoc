def modular_multiplicative_inverse(a, b):
    """
    Return the modular multiplicative inverse using the extended Euclide.
    Warning: this function assumes there is one to be found.
    """

    if a != 0:
        R, x0, x1, y0, y1 = 0, 1, 0, 0, 1
        U, V = a, b
        while R != 1:
            Q = U//V
            R = U-(Q*V)
            x0, x1 = x1, x0-(Q*x1)
            y0, y1 = y1, y0-(Q*y1)
            U, V = V, R
        return x1 % b

    else:
        return 0


def xmpl_values():
    """Return a dictionnary with sample values for n, pubkey and privkey"""

    p = 263
    q = 271
    n = p*q
    totient = (p-1)*(q-1)
    e = 281
    d = modular_multiplicative_inverse(e, totient)

    return {"n": n,
            "pubkey": e,
            "privkey": d}
