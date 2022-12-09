from sympy import poly,gcdex
from sympy.abc import x

def franklin_reiter(c1,c2,e,n,a,b):
	g1 = poly((a*x + b)**e - c2)
	g2 = poly(x**e - c1)
	for res in gcdex(g1,g2):
		z = -res.coeffs()[-1]
		if z.is_integer and \
			len(res.coeffs()) == 2 :
			return z
	return None