
#http://codeforces.com/contest/770/problem/A

def NewPassword():
	
	n, k = map(int, input().strip().split())
	alpha = "abcdefghijklmnopqrstuvwxyz"
	new_pass = ""
	
	for i in range(k):
		new_pass += alpha[i]
	
	i = 0
	j = k
	
	while((n - j) > 0):
		new_pass += alpha[i]
		i += 1
		j += 1
		
		if(i >= k):
			i = 0
	
	return new_pass
	

if __name__ == '__main__':
	a = NewPassword()
	print(a)
