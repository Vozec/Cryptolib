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

sys = rsa_init()



n = [
  617139077659107484719642514515150599813,
  455501368683163575511029416282855516761,
  1220811363170363608054081272266092543733,
  744868697249383486872904964447584353871,
  1056623804661697063783855734111105962533
]

c = [
  267928735532011070728314243534627468467,
  90057125104859539155361452457872521237,
  703309972654724303918744740970618275473,
  712717592418034733819257980333485326670,
  719326504986102016457335197929146422287
]


