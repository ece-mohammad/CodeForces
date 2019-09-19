#http://codeforces.com/contest/263/problem/A

def BeautifulMatrix():
	
	for row in range(5):
		matrix_row = input().strip().split()
		
		if '1' in matrix_row:
			pos = (row, matrix_row.index('1'))
	
	return abs(2 - pos[0]) + abs(2-pos[1])
	
	return 0

if __name__ == '__main__':
	a = BeautifulMatrix()
	print(a)
