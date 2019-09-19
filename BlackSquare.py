
#http://codeforces.com/contest/431/problem/A

def BlackSquare():
	calories = [*map( int, input().strip().split() )]
	moves = [*map( int, list(input().strip()) )]
	
	ttl = 0
	
	for i in moves:
		ttl += calories[i-1]
	
	return ttl

if __name__ == '__main__':
	a = BlackSquare()
	print(a)
