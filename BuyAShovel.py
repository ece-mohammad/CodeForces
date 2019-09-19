
#http://codeforces.com/contest/732/problem/A

def BuyAShovel():
	
	price, r = map( int, input().strip().split() )
	shovels = 0
	
	for i in range(1, 10):
		
		if not (price*i)%10 or not (price*i - r)%10:
			return i

if __name__ == '__main__':
	a = BuyAShovel()
	print(a)
