import sys
import itertools
data = sys.stdin.readlines()
m=[int(i) for i in data[1].split(' ')]
m.sort()
m.reverse()

while m!=[]:
	if m[0]>len(m)-1:
		m = filter(lambda a: a != m[0], m)
	else:
		sys.stdout.write(str(len(m)))
		break
if m==[]:
	sys.stdout.write(str(0))
