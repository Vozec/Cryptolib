from Cryptolib.SSS import SSS
from Crypto.Util.number import getPrime,bytes_to_long

def test(msg=b'Hello Vozec'):
	m = bytes_to_long(msg)	
	engine = SSS(
		N = 5,
		k = 3,
		p = getPrime(256)
	)
	return m == engine.decrypt(engine.encrypt(m))