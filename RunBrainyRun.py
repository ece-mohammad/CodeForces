
#http://codeforces.com/group/QUNKIkWhLC/contest/222116/problem/A

def HasPrimeDigits(num):
	num = str(num)
	
	for digi in ['0','1','4','6','8','9']:
		if digi in num:
			return False
	
	return True


def IsPrime(num):
	
	for div in range(2, int(num**0.5)+1):
		if num%div == 0:
			return False
	return True

def RunBrainyRun():
	
	num = int(input().strip())
	
	return HasPrimeDigits(num) and IsPrime(num)

if __name__ == '__main__':
	a = RunBrainyRun()
	if a:	
		print("Run Run Brainy !")
	else:
		print("Calm Down !")
		
