import sys
import itertools
data = sys.stdin.readlines()
pr=[int(a) for a in data[1].split(' ')]
k=[int(a) for a in data[2].split(' ')]
ps=[int(a) for a in data[3].split(' ')]
q=0
r=0
for x in xrange(len(k)):
	if abs(pr[x]-ps[x]) < abs(ps[x]-k[x]):
		q+=1
	elif abs(pr[x]-ps[x]) > abs(ps[x]-k[x]):
		r+=1
		
sys.stdout.write(str(q)+" "+str(r))