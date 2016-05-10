import sys
import math
data = sys.stdin.readlines()
[a,b,p]=[float(i) for i in data[0].split(' ')]

i=1
while i*(b*math.sqrt(i)+a)<p:
	i+=1
	#print 

if i*(b*math.sqrt(i)+a) - p < (i-1)*(b*math.sqrt(i-1)+a) - p:
	sys.stdout.write(str(i**3))
else:
	sys.stdout.write(str((i-1)**3))