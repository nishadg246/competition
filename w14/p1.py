import sys
data = sys.stdin.readlines()
d=[int(q) for q in data[1].split(' ')]
d=sorted(d,reverse=True)

def do(l):
	count=0
	while l!=[]:
		temp=list(set(l))
		for i in temp:
			if i in l:
				l.remove(i)
		count+=1
	return count



print do(d)

