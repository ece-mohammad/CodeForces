#http://codeforces.com/contest/405/problem/A

def GravitySort():
	
	n = int(input())
	
	columns = [ *map( int, input().strip().split() ) ]
	
	return sorted(columns)

if __name__ == '__main__':
	
	a = GravitySort()
	print(*a)
