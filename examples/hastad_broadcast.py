from Cryptolib.RSA.system import rsa_init

def gen(bits=64,msg=b'Hello Vozec'):
	from Crypto.Util.number import getPrime,bytes_to_long
	e = 5
	all_c = []
	all_n = []
	m = bytes_to_long(msg)
	for _ in range(e):
		p,q = getPrime(bits),getPrime(bits)
		n = p*q		
		c = pow(m,e,n)
		all_n.append(n)
		all_c.append(c)
	return m,all_c,all_n

def test():
	m1,c,n = gen()
	sys = rsa_init()
	sys.pop('n')
	sys.pop('e')
	sys.add('e',len(c))
	for _ in range(len(n)):
		sys.add('n',n[_])
		sys.add('c',c[_])
	m2 = sys.hastad()
	return m2 == m1

