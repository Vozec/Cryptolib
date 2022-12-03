from Cryptolib.RSA.system import rsa_init

def gen(bits=256):
	from Crypto.Util.number import getPrime
	from sympy import nextprime
	p = getPrime(bits)
	q = nextprime(p)
	n = p*q
	return p,q,n

def test():
	p,q,n = gen()
	sys = rsa_init(n = n)
	sys.fermat()
	return sys.full()