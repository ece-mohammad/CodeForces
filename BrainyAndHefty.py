
#http://codeforces.com/group/QUNKIkWhLC/contest/222116/problem/C

def BrainyAndHefty():
	
	n = int(input())
	
	groups = [ *map( int, input().strip().split() ) ]
	groups = [ (1 if i else -1) for i in groups ]
	
	ttl = 0
	
	for i in range(n+1):
		for j in range(i+1, n+1):
			if not sum(groups[i:j]):
				ttl+=1
	return ttl

if __name__ == '__main__':
	a = BrainyAndHefty()
	print(a)
