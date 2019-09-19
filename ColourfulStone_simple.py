
#http://codeforces.com/contest/265/problem/A

def ColourfulStones():
	
	stones = input().strip()
	cmd = input().strip()
	
	pos  = 0
	
	for i in range(len(cmd)):
		pos += (cmd[i] == stones[pos])
	
	return pos + 1

if __name__ == '__main__':
	a = ColourfulStones()
	print(a)
	
