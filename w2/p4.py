import sys
data = sys.stdin.readlines()
i=int(data[0])
dat=[]
for z in xrange(i):
	dat.append([int(q) for q in data[z+1].split(' ')])
outs=[]

for z2 in xrange(i):
	outs.append(1.0/(dat[z2][0])-1.0/(dat[z2][1]+1))

outstring=""
for j in xrange(len(outs)):
	outstring+=("%.15f" % outs[j])+'\n'

sys.stdout.write(outstring)

