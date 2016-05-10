import sys
import itertools
data = sys.stdin.readlines()
[n,b,p]=[int(a) for a in data[0].split(' ')]

def calc(n):
	if n==1 or n==0:
		return 0
	else:
		i=0
		while 2**(i+1)<=n:
			i+=1
		return 2**(i-1)+calc(n-(2**(i-1)))



sys.stdout.write(str((2*b+1)*calc(n))+" "+str(n*p))