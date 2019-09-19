
# http://codeforces.com/group/wcUWIXdda1/contest/218033/problem/G

def Training():
	
	n, k = map(int, input().strip().split())
	
	ranks = [ *map(int, input().strip().split()) ]
	
	barracks = [ranks.count(i) for i in range(1, k+1) ]
	
	coins = 0
	
	while(barracks[-1] < n):
		
		for i in range(k - 1, 0, -1):
			
			if barracks[i - 1] > 0:
				barracks[i] += 1
				barracks[i - 1] -= 1
		
		coins += 1

	return coins

if __name__ == "__main__":
	a = Training()
	print(a)
