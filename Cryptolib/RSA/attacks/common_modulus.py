from gmpy2 import gcd,invert,iroot

def egcd(a, b):
    if (a == 0):return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def npow(a, b, n):
    assert b < 0
    assert gcd(a, n) == 1
    return pow(int(invert(a, n)), b*(-1), n)

def common_modulus(e1, e2, n, c1, c2):
    g, a, b = egcd(e1, e2)
    return int(
        iroot((
            (npow(c1, a, n) if a < 0 else pow(c1, a, n)) *
            (npow(c2, b, n) if b < 0 else pow(c2, b, n))
            )%n, g)[0]
        )