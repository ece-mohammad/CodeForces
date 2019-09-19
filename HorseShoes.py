
#http://codeforces.com/contest/228/problem/A

def HorseShoes():
	
	shoes = input().strip().split()
	
	return 4 - len(set(shoes))

if __name__ == '__main__':
	a = HorseShoes()
	print(a)
