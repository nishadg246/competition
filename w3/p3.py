import sys
import itertools
data = sys.stdin.readlines()
m=[int(i) for i in data[1].split(' ')]
minlen=None
start=0
for x in xrange(len(m)):
	temp=m[(x+1):]
	s=m[x]
	count=1
	if s==0:
		if minlen==None:
			minlen=count
			start=x
		elif count<minlen:
			minlen=count
			start=x
	while temp!=[]:
		s+=temp[0]
		temp=temp[1:]
		count+=1
		if s==0:
			if minlen==None:
				minlen=count
				start=x
			elif count<minlen:
				minlen=count
				start=x
if minlen==None:
	sys.stdout.write(str(-1))
else:
	sys.stdout.write(str(start+1)+' '+str(minlen))


	

