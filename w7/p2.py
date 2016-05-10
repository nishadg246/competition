import sys
import itertools
data = sys.stdin.readlines()
t=int(data[0])
d=[]
for i in xrange(t):
	r=data[i+1].split(' ')
	d.append((r[0],r[1][:-1]))

def allPerms(pref,(x,y)):
	if len(x)==0:
		return [pref+y]
	elif len(y)==0:
		return [pref+x]
	else:
		return allPerms(pref+x[0],(x[1:],y))+allPerms(pref+y[0],(x,y[1:]))

out = []
for i in d:
	p=allPerms("",i)
	p=sorted(list(set(p)))
	out.append(p)

for i in out:
	for j in i:
		sys.stdout.write(str(j)+"\n")
	sys.stdout.write("\n")