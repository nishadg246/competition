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
		for j in xrange(i):
			a.append(l[i-j][i+j])
		if b:
			d+=a
		else:
			d+=reversed(a)
		b= not b

d2=[]
for q in d:
	d2.append(do(q))
for i in d2:
	sys.stdout.write(str(i)+'\n')
