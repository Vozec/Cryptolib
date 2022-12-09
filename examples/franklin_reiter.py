from Cryptolib.RSA.system import rsa_init
from Crypto.Util.number import getPrime,bytes_to_long

def gen(m,a=4,b=10,bits=256):	
	p,q = getPrime(bits),getPrime(bits)
	e 	= 3
	n   = p*q
	phi = (p-1)*(q-1)
	c1  = pow(m,e,n)
	c2  = pow(a*m+b,e,n)
	return c1,c2,e,n,a,b

def test(msg=b'Hello Vozec'):
	m1 = bytes_to_long(msg)
	c1,c2,e,n,a,b = gen(m1)
	sys = rsa_init(n=n,e=e)
	sys.add('c',c1)
	sys.add('c',c2)
	m2 = sys.franklin_reiter(a=a,b=b)
	return m1 == m2