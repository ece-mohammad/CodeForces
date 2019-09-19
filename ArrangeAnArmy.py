
#http://codeforces.com/group/QUNKIkWhLC/contest/222116/problem/B

from operator import mul
from functools import reduce

def GenComb(iterable, length):
	
	
	

def ArrangeArmy():
	
	n = int(input())
	groups = [* map( int, input().strip().split() )]
	k = int(input())
	ttl = 0
	
	for i in range(n):
		for c in comb(groups, i):
			if c and reduce(mul, c) <= k:
				ttl+=1
	
	return ttl

if __name__ == '__main__':
	a = ArrangeArmy()
	print(a)
	
