import sys
import itertools
data = sys.stdin.readlines()
m=int(data[0].split(' ')[1])
gens = [0]*m
for x in data[1].split(' '):
	gens[int(x)-1]+=1
total=0
for (a,b) in itertools.combinations(xrange(m), 2):
	total+=gens[a]*gens[b]
sys.stdout.write(str(total))

