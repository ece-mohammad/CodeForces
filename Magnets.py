#http://codeforces.com/contest/344/problem/A

def Magnets():
	
	n = int(input().strip())
	
	last_pole = None
	groups = 0
	
	for mag in range(n):
		next_pole = input().strip()[-1]
		if (last_pole is None) or (next_pole != last_pole):
			groups += 1
			last_pole = next_pole
	
	return groups

if __name__ == '__main__':
	a = Magnets()
	print(a)
