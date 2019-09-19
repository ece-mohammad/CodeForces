
#http://codeforces.com/contest/731/problem/A

def NightAtTheMuseum():
	
	label = input().strip()
	
	current = ord('a')
	moves = 0
	
	for i in label:
		i = ord(i)
		
		right_shift  = current - i
		left_shift = i - current
		
		if right_shift < 0:
			right_shift += 26
			
		if left_shift < 0:
			left_shift += 26
		
		moves += min(right_shift, left_shift)
		current = i
	
	return moves

if __name__ == '__main__':
	a = NightAtTheMuseum()
	print(a)
	
