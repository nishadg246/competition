import sys
import itertools
data = sys.stdin.readlines()
n=int(data[0])
a=[]
for i in xrange(n):
	a.append(int(data[i+1].split(' ')[1]))

goingup=None
for i in xrange(len(a)-1):
	if goingup


