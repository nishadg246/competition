import sys
import itertools
import math


def factorial(i,n,s):
	if i==n:
		return s
	else:
		return factorial(i+1,n,((i+1)*(s%1000000007))%1000000007)

def fact(i):
	if i==0:
		return 1
	else:
		return factorial(1,i,1)


def nCr(n,r):
    f = fact
    return (f(n)) / f(r) / f(n-r)



data = sys.stdin.readlines()
t=int(data[0])
d=[]
for i in xrange(t):
	r=data[i+1].split(' ')
	d.append((int(r[0]),int(r[1][:-1])))



for i in d:
	sys.stdout.write(str(nCr(i[0]+i[1],i[1]))+"\n")