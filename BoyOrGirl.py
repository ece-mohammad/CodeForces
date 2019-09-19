#http://codeforces.com/contest/236/problem/A

def BoyOrgirl():
	
	name = set(input().strip())
	
	if len(name)%2 == 0:
		return "CHAT WITH HER!"
	else:
		return "IGNORE HIM!"
	

if __name__ == '__main__':
	
	a = BoyOrgirl()
	print(a)
