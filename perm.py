def fact(x):
	if x<2:
		return 1
	return x*fact(x-1)
def permToNum(x): #la posicion de x en ord. Lexi
	n = len(x)
	s = 0
	tacha = [False for i in range(n)]
	for i in range(n):
		xi = x[i]
		posT = 0
		for k in range(xi):
			if not tacha[k]:
				posT+=1
		tacha[xi-1]=True
		s=s+ (posT-1)*fact(n-i-1)
	return s

def numToPerm(n,m): #m-esima permutacion
	x = []
	tacha = [False for i in range(n)]
	for i in range(n):
		faci = fact(n-i-1)
		mm = m//faci
		posT = 0
		for k in range(n):
			if not tacha[k]:
				posT+=1
			if posT==mm+1:
				x.append(k+1)
				tacha[k]=True
				break
		m = m%faci
	return x
for i in range(24):
	permI = numToPerm(4,i)
	print(i,permI,permToNum(permI))