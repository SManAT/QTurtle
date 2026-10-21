# Module Rechenoperation
#
#
#


def x_pow_y_mod_n(x, y, n):
    """berechnet x^y mod n mit Qudarieren Multiplizieren Algorithmus"""
    b = bin(y)[3:]
    erg = x
    for char in b:
        if char == "1":
            # quadrieren und multiplizieren
            erg = (erg % n) ** 2 * (x % n)
        else:
            erg = (erg % n) ** 2
    return erg % n


if __name__ == "__main__":
    print(x_pow_y_mod_n(150, 150, 14))
