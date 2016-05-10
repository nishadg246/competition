import sys
import itertools
data = sys.stdin.readlines()
m=int(data[0].split(' ')[1])
rooms=[int(a) for a in data[1].split(' ')]
q=[int(a) for a in data[3].split(' ')]


def calc(rooms,ma,m):
	s=m
	month=0
	x=rooms
	while x!=[] and month<ma:
		if s>=x[0]:
			s-=x[0]
			x=x[1:]
		else:
			month+=1
			if(month!=ma):
				s+=m
	return (len(rooms)-len(x),s)


h={}
for a in q:
	if a in h:
		sys.stdout.write(str(h[a][0])+' '+str(h[a][1])+'\n')
	else:
		(z,y) = calc(rooms,a,m)
		sys.stdout.write(str(z)+' '+str(y)+'\n')
		h[a]=(z,y)
	