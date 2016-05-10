import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
c=1
for i in xrange(n):
	n2=int((data[c]))
	r=[]
	for j in xrange(n2):
		r.append([int(q) for q in data[c+1+j].split(' ')])
	c+=1+n2
	d.append((r,n2))

def do((l,n)):
	b=True
	d=[]
	for i in xrange(n):
		a=[]
		for j in xrange(i+1):
			a.append(l[i-j][j])
		if b:
			d+=a
		else:
			a.reverse()
			d+=a
		b=not b
	for i in xrange(n-1):
		a=[]
		for j in xrange(n-1-i):
			a.append(l[n-1-j][i+1+j])
		if b:
			d+=a
		else:
			a.reverse()
			d+=a
		b=not b
	return d
def printer((n,l)):
	for i in xrange(n):
		for j in xrange(n):
			sys.stdout.write(str(l[n*i+j]))
			if j==n-1:
				sys.stdout.write('\n')
			else:
				sys.stdout.write(' ')


d2=[]
for (a,b) in d:
	d2.append((b,do((a,b))))

for i in d2:
	printer(i)
