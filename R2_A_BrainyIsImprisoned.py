#http://codeforces.com/group/QUNKIkWhLC/contest/221998/problem/A

def BrainyIsImprisoned():
	
	k = 2
	
	msgA, msgB = [sorted(list(input().strip())) for _ in range(k)]
	#print(msgA, msgB, sep='\n')
	
	for i in msgA:
		if i in msgB:
			return 'Not Trap'
	
	return 'Trap'
	
if __name__ == '__main__':
	a = BrainyIsImprisoned()
	print(a)
