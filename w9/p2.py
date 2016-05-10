import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
for i in xrange(n):
	j= [int(q) for q in data[2+2*i].split(' ')]
	d.append(j)


def do(l):
	if len(l)<=1:
		return 0
	elif l[0]==l[-1]:
		return do(l[1:-1])
	else:
		if len(l)==2:
			return 1
		elif l[0]<l[-1]:
			return 1 + do([l[0]+l[1]]+l[2:])
		else:
			return 1 + do(l[:-2]+[l[-1]+l[-2]])

d2=[]
for q in d:
	d2.append(do(q))
for i in d2:
	sys.stdout.write(str(i)+'\n')
