from sympy import *

def convergents(e):
    n,d = [e[0],e[1]*e[0] + 1],[1,e[1]]
    yield (n[0], n[0]);yield (n[1], n[1])
    for i in range(2,len(e)):
        ni,di = e[i]*n[i-1] + n[i-2],e[i]*d[i-1] + d[i-2]
        [x.append(y) for x,y in [(n,ni),(d,di)]]
        yield (ni, di)

continued_frac = lambda e,n: list(continued_fraction_iterator(Rational(e,n)))     
validity_check = lambda r,n: len(r) == 2 and n == r[0]*r[1]

def wiener(e,n):
    def solver(phi,n):
        p = Symbol('p', integer=True)
        return solve(p**2 + (phi - n - 1)*p + n, p)
    for pk, pd in convergents(continued_frac(e, n)):
        if pk == 0:
            continue;
        roots = solver((e*pd - 1)//pk,n)
        if validity_check(roots,n):
            return [int(_) for _ in roots]
    return (None,None)