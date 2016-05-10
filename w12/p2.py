import sys
import math
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
for i in xrange(n):
	d.append([int(q) for q in data[1+i].split(' ')])

def get(l):
	cables=l[1]
	want=l[0]
	rounds=int(math.log(cables, 2))
	r2=int(math.log(want, 2))
	if r2<=rounds:
		return r2+1
	else:
		temp=want-((rounds)*2-1)
		return rounds+((temp+cables)/cables)


for l in d:
	print str(get(l))

