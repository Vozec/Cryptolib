from Cryptolib.RSA.system import rsa_init

def gen(bits=64):
	from Crypto.Util.number import getPrime
	p,q,r = getPrime(bits),getPrime(bits),getPrime(bits)
	return p*q,p*r

def test():
	n1,n2 = gen()
	sys = rsa_init(n = n1)
	sys.add('n',n2)
	sys.common_prime()
	return sys.full()