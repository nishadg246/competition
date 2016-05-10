import sys
import itertools
data = sys.stdin.readlines()
i=[int(a) for a in data[1].split(' ')]
n=[int(a) for a in data[2].split(' ')]
c=[int(a) for a in data[3].split(' ')]
a=[]
mon=0
for x in xrange(len(i)):
	a.append(-((-i[x])/n[x]))
amount=max(a)
for x in xrange(len(i)):
	mon+=c[x]*(amount*n[x]-i[x])
	
sys.stdout.write(str(mon)+"")