import sys
data = sys.stdin.readlines()
n=int(data[0].split(' ')[0])
x=int(data[0].split(' ')[1])
s=[q for q in data[1][:-1]]
m=int(data[2])
i=[r for r in data[3][:-1]]
outp=s[x-1]
for a in xrange(m):
	if i[a]=='R':
		x+=1
	else:
		x-=1
	outp+=s[x-1]

sys.stdout.write(outp)





