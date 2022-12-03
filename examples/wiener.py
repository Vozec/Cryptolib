from Cryptolib.RSA.system import rsa_init

def gen(bits=256):
	from Crypto.Util.number import getPrime
	from gmpy2 import isqrt, c_div
	import  random
	urandom = random.SystemRandom()
	p,q = getPrime(bits),getPrime(bits)
	n   = p*q
	phi = (p-1)*(q-1)
	max_d = c_div(isqrt(isqrt(n)), 3).bit_length() - 1
	while True:
		d = urandom.getrandbits(max_d)
		try:
			e = int(pow(d,-1,phi))
			if (e * d) % phi == 1:
				return p,q,n,e,d
		except:
			pass

def test():
	p,q,n,e,d = gen()
	sys = rsa_init(n=n,e=e)
	sys.wiener()
	return sys.full()