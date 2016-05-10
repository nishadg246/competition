import sys
import itertools
import bisect

data = sys.stdin.readlines()
m=int(data[0].split(' ')[1])
rooms=[int(a) for a in data[1].split(' ')]
q=[int(a) for a in data[3].split(' ')]
sums = [sum(rooms[:i]) for i in xrange(1,len(rooms)+1)]
def calc(s,a,m):
	tot=a*m
	i=bisect.bisect(s,tot)
	if i==len(s):
		return (i,(tot-s[-1])%m)
	elif i==0:
		return (0,tot)
	else:
		return (i,tot-s[i-1])
	


h={}
for a in q:
	(z,y) = calc(sums,a,m)
	sys.stdout.write(str(z)+' '+str(y)+'\n')
	h[a]=(z,y)
	