
#http://codeforces.com/contest/427/problem/A

def PoliceRecruits():
	
	n = int(input().strip())
	events = [ *map( int, input().strip().split() ) ]
	
	police = 0; crime = 0
	
	for i in range(n):
		if events[i] == -1:
			crime += (police == 0)
			police -= (police > 0)
		else:
			police += events[i]
	
	return crime

if __name__ == '__main__':
	a = PoliceRecruits()
	print(a)
