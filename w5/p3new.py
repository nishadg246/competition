import sys
import itertools
data = sys.stdin.readlines()
n=int(data[0].split(' ')[0])
m=int(data[0].split(' ')[1])
mat=[]
for i in xrange(n):
	mat.append(data[i].split)

def valid(i,j):
	if mat[i][j]!='#':
		if i-1<0 or mat[i-1][j]!='#':
			return True
		elif j-1<0 or mat[i][j-1]!='#':
			return True
	return False

for i in xrange(n):
	for j in xrange(m):
		if valid(i,j):
			mat[i][j]='!'
print mat

