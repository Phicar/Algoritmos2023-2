def insercion(x):
	n = len(x)
	L = [0 for i in range(n)]
	for i in range(1,n):
		p = x[i]
		j = i-1
		while j>-1 and p<x[j]:
			x[j+1]=x[j]
			j=j-1
			L[i]+=1
		x[j+1]=p
	return x,L
def st(x):
	n = len(x)
	perm = [1 for i in range(n)]
	for i in range(n):
		for j in range(n):
			if x[i]>x[j] or (x[i]==x[j] and j<i):
				perm[i]+=1
	return perm
A = [1,5,3,10,5,2,4]
stA = st(A)
print(insercion(A))
print(insercion(stA))
	