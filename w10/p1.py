import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
for i in xrange(n):
	j= [int(q) for q in data[1+i].split(' ')]
	d.append(j)

def beauty(l):
	s=sum(l[1:])
	x=l[0]%s
	if x < l[1]:
		return "GREEN"
	else:
		x-=l[1]
		if x < l[2]:
			return "YELLOW"
		else:
			return "RED"

d2=[]
for q in d:
	d2.append(beauty(q))
for i in d2:
	sys.stdout.write(str(i)+'\n')
