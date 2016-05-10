import sys
import itertools
data = sys.stdin.readlines()
n=int(data[0].split(' ')[0])
m=int(data[0].split(' ')[1])
matr=[]
for i in xrange(n):
	matr.append(list(data[i+1])[:-1])

def inrange(i,j,n,m):
	return i<n and j<m and i>-1 and j>-1

def valid2(i,j):
	if matr[i][j]!='#':
		if (i-1<0 or matr[i-1][j]=='#') and inrange(i+1,j,n,m) and inrange(i+2,j,n,m):
			if matr[i+1][j]!='#' and matr[i+2][j]!='#':
				return True
		if (j-1<0 or matr[i][j-1]=='#') and inrange(i,j+1,n,m) and inrange(i,j+2,n,m):
			if matr[i][j+1]!='#' and matr[i][j+2]!='#':
				return True
	return False

for i in xrange(n):
	for j in xrange(m):
		if valid2(i,j):
			matr[i][j]='!'

count=0
for i in xrange(n):
	for j in xrange(m):
		if matr[i][j]=='!':
			count+=1
sys.stdout.write(str(count)+'\n')
for i in xrange(n):
	for j in xrange(m):
		if matr[i][j]=='!':
			sys.stdout.write(str(i+1)+' '+str(j+1))
			sys.stdout.write('\n')


