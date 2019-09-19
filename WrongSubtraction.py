
#http://codeforces.com/contest/977/problem/A

def WrongSubtraction():
	n, k = map(int, input().split())
	
	while(k):
		if n%10:
			n -= 1
		else:
			n /= 10
		k -= 1
	
	return int(n)

if __name__ == '__main__':
	a = WrongSubtraction()
	print(a)
