import sys
import itertools
import math
data = sys.stdin.readlines()
n=int(data[0])
s=[int(z) for z in data[1].split(' ')]

def traings(s):
	if len(s)<3:
		return 0
	else:
		if s[0]+s[1]>s[2]:
			s.pop(lastInd(s,s[0]+s[1]))
			s=s[2:]
			return 1+traings(s)
		else:
			return traings(s[2:])

def lastInd(s,m):
	i=0
	while i<len(s)-1 and s[i+1]<m:
		i+=1
	return i
sys.stdout.write(str(traings(s)))