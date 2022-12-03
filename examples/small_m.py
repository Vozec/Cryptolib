from Cryptolib.RSA.system import rsa_init

def gen(msg,bits=256):
	from Crypto.Util.number import bytes_to_long,long_to_bytes,getPrime
	e = 3
	p,q = getPrime(bits),getPrime(bits)
	n = p*q
	m = bytes_to_long(msg)
	c = pow(m,e,n)
	return c,e,m

def test(msg = b'Vozec'):
	c,e,m1 = gen(msg)
	sys = rsa_init(bits=64)
	m2 = sys.small_m(c,e)
	return m1 == m2