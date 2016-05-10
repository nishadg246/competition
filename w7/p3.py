import sys

data = sys.stdin.readlines()
d=[]
for i in xrange(len(data)):
	r=int(data[i],2)
	d.append(r)

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

def bin2(x):
	return bin(x)[2:]

def isPrime(Number):
    return 2 in [Number,2**Number%Number]

def calc(i):
	j=i+1
	while True:
		q=bin2(j)
		if is_palindrome(q) and isPrime(j):
			break
		else:
			j+=1
	return j

for i in d:
	sys.stdout.write(bin(calc(i))[2:]+"\n")