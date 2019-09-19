
# http://codeforces.com/group/wcUWIXdda1/contest/218033/problem/D

def Figures( n ):
	
	codes = dict()
	
	while( n > 0):
		line = input().strip()
		if line:
			n -= 1
			a, b, name = line.split()
			codes[(a, b)] = name
	
	return codes


def main():
	
	n = int(input().strip())
	
	codes = Figures(n)
	
	m = input().strip()
	
	while( not bool(m) ):
		m = input().strip()
	
	m = int(m)
	
	while(m > 0):
		line = input().strip()
		if line:
			m -= 1
			a, b = line.strip().split()
			print(codes[(a,b)])

if __name__ == "__main__":
	main()
