import sys
data = sys.stdin.readlines()
a=None
b=None
end=[]
i=int(data[0])
emots=[x for x in data[1][:i]]
smile=0
frown=0
for i in xrange(len(emots)-1):
	if emots[i]==':':
		if emots[i+1]==')':
			smile+=1
		elif emots[i+1]=='(':
			frown+=1
	elif emots[i]=='(':
		if emots[i+1]==':':
			smile+=1
	elif emots[i]==')':
		if emots[i+1]==':':
			frown+=1

if smile==frown:
	sys.stdout.write('BORED')
elif smile<frown:
	sys.stdout.write('SAD')
else:
	sys.stdout.write('HAPPY')





