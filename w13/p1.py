import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
d=[int(q) for q in data[1].split(' ')]

def do(l):
	count=0
	t=[]
	for i in xrange(len(l)):
		if l[i]==i+1:
			t.append(i+1)
			count+=1
	if count%2==0:
		print count/2
	else:
		print (count+1)/2
	for i in xrange((len(t)/2)):
		print str(t[i])+" "+str(t[i+1])
	if len(t)%2==1:
		if t[-1]==1:
			print "1 2"
		else:
			print str(t[-1])+" "+str(t[-1]-1)


do(d)

