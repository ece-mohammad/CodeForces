#http://codeforces.com/contest/791/problem/A

def BearAndBigBrother():
	a,b = map(int, input().strip().split())
	y = 0
	while (a <= b):
		a*=3
		b*=2
		y+=1
	
	return y


if __name__ == '__main__':
	a = BearAndBigBrother()
	print(a)
