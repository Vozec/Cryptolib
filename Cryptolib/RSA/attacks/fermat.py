from gmpy2 import get_context,ceil,sqrt,is_square,mpz

def fermat(n):
    get_context().precision=10000
    is_square = lambda n: sqrt(n).is_integer()
    a = mpz(ceil(sqrt(n)))
    b = mpz((a*a) - n)
    while not is_square(b):
        a = a + 1
        b = (a * a) - n
    p = a - sqrt(b)
    q = a + sqrt(b)
    return p,q