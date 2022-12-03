def hastad_broadcast(n,c,e=3):
	from gmpy import root	
	N = 1;
	for ni in n:
		N *= ni
	all_N = []
	all_x = []
	for i in range(len(n)):
		all_N.append(N//n[i])
		all_x.append(pow(all_N[-1],-1,n[i]))
	M = 0
	for _ in range(len(n)):
		M += (all_x[_]*all_N[_]*c[_])
	return root(M % N,e)[0]

