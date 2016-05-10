import sys
import itertools
data = sys.stdin.readlines()
n=data[0][:-1]
a=[(int(n[i:i+2]),i) for i in xrange(len(n)-1)]
def calc(x):
	if x[0]%4==0:
		return x[1]+1+(x[0]%10==0)
	return 0
a =map(calc,a)
c=(int(str(n)[:1])%4==0)
sys.stdout.write(str(sum(a)+t+c))