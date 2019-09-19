
#http://codeforces.com/group/P8UZg7UOT5/contest/223745/problem/D

def AGoodContest():
	n = int(input())
	good = 0
	
	for i in range(n):
		contestant = input().strip().split()
		before = int(contestant[1])
		after = int(contestant[2])
		if before >= 2400 and after > before:
			good += 1
	
	if good > 0:
		return "YES"
	else:		
		return "NO"

if __name__ == '__main__':
	a = AGoodContest()
	print(a)
