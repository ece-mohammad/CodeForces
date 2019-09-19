
#http://codeforces.com/contest/799/problem/A

def CarrotCakes():
	n, t, k, d = [ *map(int, input().strip().split()) ]
	
	if n <= k:
		return 'NO'
	
	elif d == t:
		return 'YES' if (n - k) > k else 'NO'
		
	elif d < t:
		return 'YES'
	
	else:
		return 'YES' if (n - (d//t)*k) > k else 'NO'

if __name__ == '__main__':
	a = CarrotCakes()
	print(a)
