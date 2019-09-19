
# http://codeforces.com/group/wcUWIXdda1/contest/218033/problem/J

def Flags():
	
	n, m = map(int, input().strip().split() )
	
	last_color = ""
	
	for line in range(n):
		
		l = input().strip()
		if len(set(l)) > 1 or l[0] == last_color:
			return "NO"
		else:
			last_color = l[0]
	
	return "YES"

if __name__ == "__main__":
	a = Flags()
	print(a)
