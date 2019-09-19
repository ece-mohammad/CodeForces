
#http://codeforces.com/contest/266/problem/A

def StonesOnTable():
	
	n = int(input())
	stones = input().strip()
	rep = 0
	
	for i in range(n - 1):
		if stones[i] == stones[i+1]:
			rep += 1
		
	return rep

if __name__ == '__main__':
	a = StonesOnTable()
	print(a)
