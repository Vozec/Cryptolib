from Crypto.Util.number import getPrime


def primes(bits=1024):
	return (getPrime(bits),getPrime(bits))

def isprime(n):
	def miller_rabin(n, k=40):
		import random
		if n == 2:
			return True
		if n & 1 == 0:
			return False
		r, s = 0, n - 1
		while s & 1 == 0:
			r += 1
			s >>= 1
		i = 0
		for i in range(0, k):
			a = random.randrange(2, n - 1)
			x = pow(a, s, n)
			if x == 1 or x == n - 1:
				continue
			j = 0
			while j <= r - 1:
				x = pow(x, 2, n)
				if x == n - 1:
					break
				j += 1
			else:
				return False
		return True

	fermat_criterion = lambda n,b=2: pow(b, n - 1, n) == 1
	if (
		fermat_criterion(n)
		and fermat_criterion(n, b=3)
		and fermat_criterion(n, b=5)
	):
		return miller_rabin(n)
	else:
		return False

