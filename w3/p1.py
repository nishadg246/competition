import sys
data = sys.stdin.readlines()
num=int(data[0])
size=int(data[1])
flashes=[]
for i in data[2:]:
	flashes.append(int(i))
flashes.sort()
flashes.reverse()
count=0
while size>0:
	size-=flashes[0]
	flashes=flashes[1:]
	count+=1
sys.stdout.write(str(count))
