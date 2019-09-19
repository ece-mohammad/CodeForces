#http://codeforces.com/group/QUNKIkWhLC/contest/221998/problem/C

def DefuseTheBomb():
	
	k = int(input())
	nums = [*map(int, input().strip().split())]
	start_index, end_index = map(int, input().strip().split())
	solution = [6, 4, 11, 7, 10, 20]
	#print(nums, start_index, end_index, sep='\n')
	
	temp = nums[start_index: end_index+1]
	other = [nums[i] for i in range(k) if not (i in range(start_index, end_index+1))]
	other.sort()
	
	#print(temp, other, sep='\n')
	#print(solution)
	return other[:start_index]+temp+other[start_index:]


if __name__ == '__main__':
	a = DefuseTheBomb()
	print(*a)
