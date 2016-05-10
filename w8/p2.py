import sys
data = sys.stdin.readlines()

n=[int(i) for i in data[1].split(' ')]
l=data[2]
d=[]
s=0
for i in xrange(len(n)):
	if l[i]=='B':
		s+=n[i]
	if l[i]=='B':
		d.append(-n[i])
	else:
		d.append(n[i])

pref=[]
s1=0
s2=0
d1=[0]
d2=[0]
for x in xrange(len(d)):
	s1+=d[x]
	s2+=d[len(d)-1-x]
	d1.append(s1)
	d2.append(s2)



# temp=d[1:]
# temp2=(d[::-1])
# d2=[d[0]]
# d3=[temp2[0]]
# running=d[0]
# running2=temp2[0]
# temp2=temp2[1:]
# while temp!=[]:
# 	running+=temp[0]
# 	d2.append(running)
# 	temp=temp[1:]
# 	running2+=temp2[0]
# 	d3.append(running2)
# 	temp2=temp2[1:]
j=max(max(d2),max(d1),0)

sys.stdout.write(str(s+j))
