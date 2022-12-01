from Crypto.Util.number import long_to_bytes,bytes_to_long,GCD
from Crypto.PublicKey import RSA

from Cryptolib.RSA.utils import primes
from Cryptolib.logger import *

class rsa_system():
	def __init__(self,e=None,q=None,p=None,n=None,d=None,phi=None):
		self.e = e
		self.p = p
		self.q = q
		self.n = n
		self.phi = phi
		self.d = d

	## UTILS #######################
	e 	= lambda self: self.e
	p 	= lambda self: self.p
	q 	= lambda self: self.q
	n 	= lambda self: self.n
	d 	= lambda self: self.d
	phi = lambda self: self.phi

	def full(self):
		return self.e and self.p and self.q and self.n and self.d and self.phi

	def check(self):
		if (self.n and self.p and self.q) and self.p*self.q != self.n :
			return False
		if (self.d and self.phi and self.e) and pow(self.e,-1,self.phi) != self.d:
			return False
		if (self.e and self.phi) and GCD(self.e,self.phi) != 1:
			return False
		if (self.e and self.p) and GCD(self.e,self.p-1) != 1:
			return False
		if (self.e and self.q) and GCD(self.e,self.q-1) != 1:
			return False
		return True

	def info(self):
		logger('--- Status ---','info',0,0,True)
		for name,value in self.list().items():
			logger('%3s: %s'%(name.upper(),'know' if value else 'unknow'),
				'flag' if value is not None else 'error',0,0,True)
		logger('--------------','info',0,0,True)

	def list(self):
		return {"e":self.e,"p":self.p,"q":self.q,"n":self.n,"d":self.d,"phi":self.phi}

	def pop(self,x):
		if x == 'e':self.e = None
		elif x == 'n':self.n = None
		elif x == 'p':self.p = None
		elif x == 'q':self.q = None
		elif x == 'd':self.d = None
		elif x == 'phi':self.phi = None

	def update(self,e=None,q=None,p=None,n=None,d=None,phi=None):
		if e :self.e = e
		elif n:self.n = n
		elif p:self.p = p
		elif q:self.q = q
		elif d:self.d = d
		elif phi:self.phi = phi
		self.compute()
		return self.check()

	def compute(self):
		if (self.p and self.n and not self.q):
			self.q = self.n // self.p
		if (self.q and self.n and not self.p):
			self.p = self.n // self.q
		if (self.q and self.q and not self.n):
			self.n = self.p * self.q
		if (self.p and self.n and not self.phi):
			self.phi = (self.p-1)*(self.q-1)
		if (self.e and self.phi and not self.d):
			self.d = pow(self.e,-1,self.phi)

	################################

	## OTHER #######################
	def public_key(self):
		assert self.n and self.e and self.d, '(n,e) incomplete'
		return RSA.construct((self.n,self.e)).publickey().export_key()

	def private_key(self):
		assert self.n and self.e and self.d, '(n,e,d) incomplete'
		return RSA.construct((self.n,self.e,self.d)).export_key()

	def encrypt(self,m):
		assert self.e and self.n ,'(e,n) incomplete'
		return pow(bytes_to_long(message),self.e,self.n)

	def decrypt(self,m):
		assert self.d and self.n ,'(d,n) incomplete'
		return long_to_bytes(pow(message,self.d,self.n))
	################################

	## OTHER #######################
	def factordb(self):
		assert self.n, 'N is unknow'
		from factordb.factordb import FactorDB
		f = FactorDB(self.n)
		f.connect()
		res = f.get_factor_list()
		if (len(res)) == 2:
			self.update(p=res[0],q=res[1])
		return self.p,self.q

	def fermat(self):
		assert self.n, 'N is unknow'
		from Cryptolib.RSA.attacks.fermat import fermat
		p,q = fermat(self.n)
		self.update(p=p,q=q)
		return p,q

	def wiener(self):
		assert self.n and self.e, '(n,e) incomplete'
		from Cryptolib.RSA.attacks.wiener import wiener
		p,q = wiener(self.e,self.n)
		if p is not None:
			self.update(p=p,q=q)
		return p,q

	def common_modulus(self,e2, c1, c2):
		assert self.n and self.e, '(n,e) incomplete'
		from Cryptolib.RSA.attacks.common_modulus import common_modulus
		m = common_modulus(self.e,e2, self.n, c1, c2)
		return long_to_bytes(m)

	def common_prime(self,n2,n1=None):
		assert self.n and self.e, '(n,e) incomplete'
		n1 = self.n if n1 is None else n1
		p = GCD(self.n,n2)
		self.update(p=p)
		return self.p,self.q

	def small_m(self,c):
		assert self.n and not e, '(n,e) incomplete'
		assert self.e != 3, 'E is not 3'
		from gmpy2 import iroot,get_context
		get_context().precision=1000000000000000000
		return int(iroot(c,3)[0])

	################################


def rsa_init(bits=1024,e=None,q=None,p=None,n=None,d=None,phi=None):
	def init():
		p,q = primes(bits)
		return rsa_system(
			e=0x10001,
			q=q,
			p=p,
			n=p*q,
			d=pow(0x10001,-1,(p-1)*(q-1)),
			phi=(p-1)*(q*1)
		)
	if e == q == p == n == d == phi == None:
		return init()
	return rsa_system(e=e,q=q,p=p,n=n,d=d,phi=phi)