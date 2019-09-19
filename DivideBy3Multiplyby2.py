
#http://codeforces.com/contest/977/problem/D

def IsStartPoint(n, seq):
	has_head = (n/2 in seq) or (n*3 in seq)
	has_tail = (n*2 in seq) or (n/3 in seq)
	return (has_tail and (not has_head))
	

def DivideBy3MultiplyBy2():
	n = int(input())
	seq = [int(i) for i in input().strip().split()]
	start = 0
	tmp = list()
	
	for i in range(n):
		if IsStartPoint(seq[i], seq):
			tmp.append(seq[i])
			start = seq[i]
			break
	
	for i in range(n - 1):
		
		if int(start/3) in seq:
			tmp.append(int(start/3))
			start = int(start/3)
		else:
			tmp.append(start*2)
			start *= 2
	
	return tmp

if __name__ == '__main__':
	a = DivideBy3MultiplyBy2()
	print(*a)
