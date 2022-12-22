from Crypto.Util.number import long_to_bytes,bytes_to_long,GCD,inverse
from Crypto.PublicKey import RSA

from Cryptolib.RSA.utils import primes
from Cryptolib.RSA.message import msg
from Cryptolib.logger import *

class rsa_system():
	def __init__(self,e=None,q=None,p=None,n=None,d=None,phi=None,c=None):
		self.phi = phi
		self.d = d
		self.p = p
		self.q = q
		self.e = [e] if e and type(e) != list else e
		self.n = [n] if n and type(n) != list else n
		self.c = [c] if c and type(c) != list else c

	## UTILS #######################
	e 	= lambda self: self.e
	p 	= lambda self: self.p
	q 	= lambda self: self.q
	n 	= lambda self: self.n
	d 	= lambda self: self.d
	phi = lambda self: self.phi

	def full(self):
		return self.e != None and self.n != None \
		and self.d!= None  and self.phi != None

	def check(self):
		if (self.n and self.p and self.q) and self.p*self.q != self.n[0] :
			return False
		if (self.d and self.phi and self.e[0]) and pow(self.e[0],-1,self.phi) != self.d:
			return False
		if (self.e and self.phi) and GCD(self.e[0],self.phi) != 1:
			return False
		if (self.e and self.p) and GCD(self.e[0],self.p-1) != 1:
			return False
		if (self.e and self.q) and GCD(self.e[0],self.q-1) != 1:
			return False
		return True

	def info(self):
		logger('--- Status ---','info',0,0,True)
		for name,value in self.list().items():
			logger('%3s: %s'%(name.upper(),'know' if value else 'unknow'),
				'flag' if value is not None else 'error',0,0,True)
		logger('--------------','info',0,0,True)

	def list(self):
		return {"e":self.e,"p":self.p,"q":self.q,"n":self.n,"d":self.d,"phi":self.phi,"c":self.c}

	def add(self,x,val):
		if   x == 'c':self.c = self.c+[val] if self.c else [val]
		elif x == 'e':self.e = self.e+[val] if self.e else [val]
		elif x == 'n':self.n = self.n+[val] if self.n else [val]

	def pop(self,x):
		if x == 'e':self.e = None
		elif x == 'n':self.n = None
		elif x == 'p':self.p = None
		elif x == 'q':self.q = None
		elif x == 'd':self.d = None
		elif x == 'phi':self.phi = None
		elif x == 'c':self.phi = None

	def update(self,e=None,q=None,p=None,n=None,d=None,phi=None,c=None):
		if e :self.e = [e] if type(e) != list else e
		if n:self.n = [n] if type(n) != list else n
		if c:self.c = [c] if type(c) != list else c
		if p:self.p = p
		if q:self.q = q
		if d:self.d = d
		if phi:self.phi = phi
		self.compute()
		return self.check()

	def compute(self):
		if (self.p and self.n and not self.q):
			self.q = self.n[0] // self.p
		if (self.q and self.n and not self.p):
			self.p = self.n[0] // self.q
		if (self.q and self.q and not self.n):
			self.n = [self.p * self.q]
		if (self.p and self.n and not self.phi):
			self.phi = (self.p-1)*(self.q-1)
		if (self.e and self.phi and not self.d):
			self.d = inverse(self.e[0],self.phi)
	################################

	## OTHER #######################
	def public_key(self):
		assert self.n and self.e and self.d, '(n,e) incomplete'
		return RSA.construct((self.n[0],self.e[0])).publickey().export_key()

	def private_key(self):
		assert self.n and self.e and self.d, '(n,e,d) incomplete'
		return RSA.construct((self.n[0],self.e[0],self.d)).export_key()

	def encrypt(self,m):
		assert self.e and self.n ,'(e,n) incomplete'
		return pow(bytes_to_long(m),self.e[0],self.n[0])

	def decrypt(self,m):
		assert self.d and self.n ,'(d,n) incomplete'
		return msg(pow(m,self.d,self.n[0]))
	################################

	## OTHER #######################
	def factordb(self):
		assert self.n, 'N is unknow'
		from factordb.factordb import FactorDB
		f = FactorDB(self.n[0])
		f.connect()
		res = f.get_factor_list()
		if (len(res)) == 2:
			self.update(p=res[0],q=res[1])
		return self.p,self.q

	def fermat(self):
		assert self.n, 'N is unknow'
		from Cryptolib.RSA.attacks.fermat import fermat
		p,q = fermat(self.n[0])
		self.update(p=int(p),q=int(q))
		return p,q

	def wiener(self):
		assert self.n and self.e, '(n,e) incomplete'
		from Cryptolib.RSA.attacks.wiener import wiener
		p,q = wiener(self.e[0],self.n[0])
		if p is not None:
			self.update(p=p,q=q)
		return p,q

	def common_modulus(self):
		assert self.n and self.e, '(n,e) incomplete'
		assert len(self.e) >= 2, '[e] has to have 2 elements'
		assert len(self.c) >= 2, '[c] has to have 2 elements'
		from Cryptolib.RSA.attacks.common_modulus import common_modulus
		m = common_modulus(self.e[0],self.e[1], self.n[0], self.c[0], self.c[1])
		return long_to_bytes(m)

	def small_m(self,c:int,e=None):
		e = e if e is not None else self.e[0]
		assert self.n[0] and self.e[0], '(n,e) incomplete'
		from gmpy2 import iroot,get_context
		get_context().precision=1000000000
		return int(iroot(c,e)[0])


	def common_prime(self):
		assert self.n and self.e, '(n,e) incomplete'
		assert len(self.n) >= 2, '[n] has to have 2 elements'
		p = GCD(self.n[0],self.n[1])
		self.update(p=p)
		return self.p,self.q

	def hastad(self):
		assert len(self.n) == len(self.c) and self.e[0] == len(self.n),\
			'You have to set %s couples of (n,c)'%self.e
		from Cryptolib.RSA.attacks.hastad import hastad_broadcast 
		m = hastad_broadcast(self.n,self.c,self.e[0])
		return m

	def franklin_reiter(self,a:int,b:int):
		assert self.e and self.n and self.c, '(n,e,c) incomplete'
		assert len(self.c),'[c] has to have 2 elements'
		assert self.e[0].bit_length() < 32, 'e is to much big'
		from Cryptolib.RSA.attacks.franklin_reiter import franklin_reiter 
		m = franklin_reiter(self.c[0],self.c[1],self.e[0],self.n[0],a,b)
		return m

	def multi_primes(self,primes=None):
		assert self.e and self.n, '(n,e) incomplete'
		from Cryptolib.RSA.attacks.multi_primes import multi_primes,check_primes
		if primes:
			assert check_primes(primes,self.n[0]),'Product of primes != N'
		phi,d = multi_primes(self.n[0],self.e[0],primes)
		self.update(phi=phi,d=d)
		return True

	def fault_signature(self,s:int,m:int):
		assert self.e and self.n, '(n,e) incomplete'
		p = GCD(s**self.e[0] - m,self.n[0])
		self.update(p=p)
		return self.p,self.q

	################################


def rsa_init(bits=1024,e=0x10001,q=None,p=None,n=None,d=None,phi=None,c=None):
	def init(e):
		p,q = primes(bits)
		return rsa_system(
			e=e,
			q=q,
			p=p,
			n=p*q,
			d=pow(e,-1,(p-1)*(q-1)),
			phi=(p-1)*(q*1),
			c=None)
	if q == p == n == d == phi == None:
		return init(e)
	return rsa_system(e=e,q=q,p=p,n=n,d=d,phi=phi,c=c)