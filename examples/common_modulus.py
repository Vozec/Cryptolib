from Cryptolib.RSA.system import rsa_init

def gen(msg,bits=256):
	from Crypto.Util.number import bytes_to_long,getPrime
	e1,e2 = 3,5
	p,q = getPrime(bits),getPrime(bits)
	n = p*q
	m = bytes_to_long(msg)
	c1 = pow(m,e1,n)
	c2 = pow(m,e2,n)
	return c1,c2,e1,e2,n

def test(msg = b'Hello Vozec'):
	c1,c2,e1,e2,n = gen(msg)
	sys = rsa_init(
		e = e1,
		n = n
	)
	sys.add('e',e2)
	sys.add('c',c1)
	sys.add('c',c2)
	
	m = sys.common_modulus()
	return m == msg