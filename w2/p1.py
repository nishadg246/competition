import sys
data = sys.stdin.readlines()
a=None
b=None
end=[]
c=data[0].split(' ')
c[1]=c[1][:-1]
a=[int(z) for z in c[0]]
b=[int(y) for y in c[1]]

for x in xrange(len(a)):
	end.append(abs(a[x]-b[x]))

def conv(L):
	s=0
	for x in xrange(len(L)-1):
		s+=L[x]
		s*=10
	s+=L[len(L)-1]
	return s

sys.stdout.write(str(conv(end)))

