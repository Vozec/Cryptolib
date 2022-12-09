from Crypto.Util.number import long_to_bytes,bytes_to_long

class msg:
	def __init__(self,m):
		self.m = m

	def __str__(self):return self.text(self.m)
	def __int__(self):return int(self.m)
	def __long__(self):return int(self.m)
	def __bytes__(self):return bytes(self.m)


	def decode(self,m):
		m = self.m if not m else m
		if type(m) == bytes:
			return m.decode('utf-8')
		return m

	def text(self,m=None):
		m = self.m if not m else m
		t = type(m)
		if t == bytes:
			return self.decode(m)
		elif t == int:
			return self.decode(self.bytes(m))
		elif t in [tuple,list]:
			return [self.bytes(_) for _ in m]
		return self.m

	def long(self,m=None):
		m = self.m if not m else m
		return bytes_to_long(self.bytes(m))

	def int(self,m=None):
		m = self.m if not m else m
		return self.long(m)

	def bytes(self,m=None):
		m = self.m if not m else m
		t = type(m)
		if t == bytes:
			return m
		elif t == str:
			return bytes(m,'utf-8')
		elif type(m) == int:
			return long_to_bytes(m)
		elif t in [tuple,list]:
			return [self.bytes(_) for _ in m]
		return m