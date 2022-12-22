from Cryptolib.RSA.system import rsa_init
from Crypto.Util.number import getPrime,bytes_to_long,inverse
from hashlib import sha256

def gen():
	e,p,q = (0x10001,getPrime(128),getPrime(128))
	n = p*q
	d = inverse(e,(p-1)*(q-1))
	return e,p,q,n,d

def sign(m,e,n,p,q,d):
	dp,dq = (d % (p-1),
			 d % (q-1))
	sp,sq = (pow(m,dp,p),
			 pow(m,dq,q))
	sq = sq+1
	h = ((sp-sq) * pow(q,-1,p)) % p
	return sq + q*h

def test(msg=b'Hello Vozec'):
	e,p,q,n,d = gen()
	hash  = bytes_to_long(sha256(msg).digest())
	sig   = sign(hash,e,n,p,q,d)
	sys   = rsa_init(n=n,e=e)
	sys.fault_signature(s=sig,m=hash)
	return sys.full()