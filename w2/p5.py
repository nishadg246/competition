import sys
data = sys.stdin.readlines()
i=int(data[0].split(' ')[0])
j=int(data[0].split(' ')[1])
if i>j:
	sys.stdout.write(str((i+1)*j))
else:
	sys.stdout.write(str((j+1)*i))


