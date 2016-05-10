import sys
import itertools
data = sys.stdin.readlines()
a=int(data[0])
b=int(data[1])
c=int(data[2])
l=[a,a,b,b,c,c]
op=False
for (q,r,s) in itertools.combinations(l, 3):
	if q+r==s or q+s==r or r+s==q:
		op=True
		break
if op:
	sys.stdout.write('YES')
else:
	sys.stdout.write('NO')
