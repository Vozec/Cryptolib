from Crypto.Util.number import isPrime,getPrime,long_to_bytes,bytes_to_long
from random import randint

class SSS():
	def __init__(self,N,k,p):
		assert isPrime(p), "P has to be a Prime-Number"
		assert p > N, "P must be superior to N"
		self.N = N
		self.k = k
		self.p = p
		self.coeff  = [randint(1,self.p) for _ in range(self.k-1)]
		self.eval_polynomial = lambda coeff,x : sum([coeff[i] * x**(i+1) for i in range(len(coeff))])

	def encrypt(self,S):
		assert self.p > S, "Prime is to weak , P must be superior to S"
		self.shares = [
			(x,S + self.eval_polynomial(self.coeff,x))
			for x in range(1,self.N+1)
		]
		return self.shares

	def decrypt(self,shares):
		from sympy.polys.polyfuncs import interpolate
		from sympy import Poly
		from sympy.abc import a, b, x
		return Poly(interpolate(shares, x)).EC()
