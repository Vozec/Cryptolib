from factordb.factordb import FactorDB
from Crypto.Util.number import inverse

def check_primes(primes,n):
	x = 1
	for p in primes:
		x *= p
	return x == n

def multi_primes(n,e,primes=None):
	if not primes:
		f = FactorDB(n)
		f.connect()
		primes = f.get_factor_list()
	phi = 1
	try:
		for p in primes:
			phi *= (p-1)
		d = inverse(e,phi)
		return phi,d
	except:
		return False