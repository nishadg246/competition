import sys
import itertools
data = sys.stdin.readlines()
t=int(data[0])
d=[]
data=data[1:]
for x in xrange(t):
	n=int(data[0])
	r=data[1:n+1]
	r=[j[:-1] for j in r]
	d.append(r)
	data=data[n+1:]

def calc(x):
	j=[int(q) for q in x.split(' ')]
	xs=[j[0],j[2],j[4],j[6]]
	ys=[j[1],j[3],j[5],j[7]]
	return ((min(xs),max(xs)),(min(ys),max(ys)))

def red (((x1,x2),(y1,y2)),((x3,x4),(y3,y4))): return ((min(x1,x3),max(x2,x4)),(min(y1,y3),max(y2,y4)))
def calc2(y):
	r=[]
	for i in y:
		r.append(calc(i))
	x=r[0]
	for i in r[1:]:
		x=red(x,i)
	return (x[0][1]-x[0][0])*(x[1][1]-x[1][0])

outtt = [calc2(i) for i in d]
for i in outtt:
	sys.stdout.write(str(i)+"\n")