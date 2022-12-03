from Cryptolib.RSA.system import rsa_init

def test():
	sys = rsa_init(bits=10)
	sys.factordb()
	return sys.full()