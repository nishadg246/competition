import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
for i in xrange(n):
	j= [int(q) for q in data[2+2*i].split(' ')]
	d.append(j)

def beauty(l):
	l=sorted(l)
	c =(len(l)+1)/2
	s=0
	for x in xrange(len(l)/2):
		s+=l[x+c]-l[x]
	return s

d2=[]
for q in d:
	d2.append(beauty(q))
for i in d2:

	sys.stdout.write(str(i)+'\n')
