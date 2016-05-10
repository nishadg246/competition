import sys
import itertools
data = sys.stdin.readlines()
n =int(data[0])

if n<=4:
	sys.stdout.write(str(-1))
else:
	q=1
	m=n
	while True:
		i=m/2
		j=m-i
		if i*j>=1000000000:
			sys.stdout.write(str(q))
			break
		else:
			m=i*j
			q+=1