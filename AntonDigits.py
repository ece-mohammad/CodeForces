
def Anton():
	
	nums = [*map(int, input().split())]
	
	n_256 =  min((nums[0], nums[2], nums[3]))
	
	ttl = n_256*256
	
	nums[0]-= n_256
	nums[2]-= n_256
	nums[3]-= n_256
	
	n_32 = min(nums[:2])
	
	ttl += n_32*32
	
	print(ttl)
	
	

if __name__ == '__main__':
	Anton()
