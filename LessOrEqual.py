
#http://codeforces.com/contest/977/problem/C

def LessOrEqual():
	
	n, k = map(int, input().strip().split())
	seq = [int(i) for i in input().strip().split()]
	
	seq.sort()
	
	if seq[k] > seq[k-1]:
		return seq[k-1]
	
	else:
		return -1

if __name__ == '__main__':
	a = LessOrEqual()
	print(a)
