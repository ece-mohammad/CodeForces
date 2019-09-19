
#http://codeforces.com/group/P8UZg7UOT5/contest/223745/problem/C

def RestoringPasswod():
	encrypted = input().strip()
	keys = {input().strip():str(i) for i in range(10)}
	char_lenght = 10
	old_pass = ""
	
	for i in range(0, 80, 10):
		old_pass += keys[encrypted[i:i+10]]
	
	return old_pass

if __name__ == '__main__':
	a = RestoringPasswod()
	print(a)
	
