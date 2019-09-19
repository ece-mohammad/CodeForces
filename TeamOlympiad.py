#http://codeforces.com/contest/490/problem/A

def TeamOlympiad():
	
	n = int(input())
	
	children = {1:[], 2:[], 3:[]}
	
	talent_math = []
	talent_prog = []
	talent_pe =	[]
	
	temp = [ *map(int, input().strip().split()) ]
	
	for i in range(n):
		children[temp[i]].append((i+1))
	
	return min(len(children[1]), len(children[2]), len(children[3])), zip(children[1],children[2], children[3])

if __name__ == '__main__':
	a = TeamOlympiad()
	
	print(a[0])
	for team in a[1]:
		print(*team)
