import sys
import itertools
import math
data = sys.stdin.readlines()
sq=[]
n=int(data[0])
for i in xrange(1,n+1):
	sq+=[int(z) for z in data[i].split(' ')]

def fill(z,n):
	s= (n*n+1)*n/2
	for i in xrange(n):
		z[i*n+i]= s - sum(z[n*i:n*i+n])

fill(sq,n)
sq=[str(q) for q in sq]

for i in xrange(n):
	sys.stdout.write(' '.join(sq[n*i:n*i+n]))
	sys.stdout.write('\n')

	
