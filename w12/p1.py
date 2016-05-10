import sys
data = sys.stdin.readlines()
n=int((data[0]))
d=[]
for i in xrange(n):
	d.append([int(q) for q in data[1+i].split(' ')])

def do(l):
	if l[0]<l[3]:
		return "Player1"
	elif l[0]>l[3]:
		return "Player2"
	else:
		if l[1]<l[4]:
			return "Player1"
		elif l[1]>l[4]:
			return "Player2"
		else:
			if l[2]<l[5]:
				return "Player1"
			elif l[2]>l[5]:
				return "Player2"
			else:
				return "Tie"


for l in d:
	sys.stdout.write(do(l)+'\n')

