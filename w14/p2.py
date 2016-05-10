import sys
import math
data = sys.stdin.readlines()
d=[int(q) for q in data[1].split(' ')]
d=sorted(d,reverse=True)

def do(d):
	x1=math.sqrt((d[0]-d[2])**2 + (d[1]-d[3])**2)
	x2=math.sqrt((d[2]-d[4])**2 + (d[3]-d[5])**2)
	t1=d[-2]
	t2=d[-1]
	ang1=math.arcsin(math.sin(t2)/math.sin(t1)*x1/x2)



print do(d)

