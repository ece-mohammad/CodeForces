#http://codeforces.com/contest/231/problem/A

def Team():
	n = int(input())
	count = 0
	for problem in range(n):
		count += (input().strip().count('1') > 1)
	
	return count

if __name__ == '__main__':
	a = Team()
	print(a)
