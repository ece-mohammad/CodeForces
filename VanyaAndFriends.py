#http://codeforces.com/contest/677/problem/A

def VanyaAndfriends():
	
	n,h = map(int, input().strip().split())
	width = n #minimum road width if all heights are less than h!!
	
	heights = map(int, input().strip().split())
	
	for i in heights:
		if i > h:
			width+=1
	
	return width

if __name__ == '__main__':
	a = VanyaAndfriends()
	print(a)
