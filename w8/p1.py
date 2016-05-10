import sys

def count(d):
	d=d[1:]
	n=1
	while d!=[]:
		if d[0]==1:
			n*=2
		else:
			n*=2
			n+=1
		d=d[1:]
	return n

def find(d,p):
	x=count(d)
	prof=0
	while x!=0:
		prof+=p*(float(x)/2.0)
		x/=2
	return prof

data = sys.stdin.readlines()
n=int(data[0].split(' ')[0])
p=int(data[0].split(' ')[1])
d=[]
for i in xrange(n):
	r=data[i+1]
	if r=="half\n":
		d=[1]+d
	else:
		d=[2]+d

sys.stdout.write(str(int(find(d,p))))
