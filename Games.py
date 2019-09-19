
#http://codeforces.com/contest/268/problem/A

def Games():
	n = int(input().strip())
	
	home_uni = []
	away_uni = []
	host_away_uni = 0
	
	for i in range(n):
		h,a = map(int, input().strip().split())
		home_uni.append(h)
		away_uni.append(a)
	
	for uni in home_uni:
		host_away_uni += away_uni.count(uni)
	
	return host_away_uni

if __name__ == '__main__':
	a = Games()
	print(a)
