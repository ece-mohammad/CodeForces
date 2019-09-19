#http://codeforces.com/group/P8UZg7UOT5/contest/223745/problem/B

def IsPrime(n):
	
	if n < 2:
		return False
		
	for div in range(2, int(n**0.5) + 1):
		if n%div == 0:
			return False
	return True

def MagdyAndFootball():
	n = int(input())
	s = input().strip()
	upper_count = 0
	
	for i in s:
		if i.isupper():
			upper_count += 1
			
	if IsPrime(upper_count):
		return "Magdy is a good boy"
	else:
		return "Magdy is a stupid boy"

if __name__ == '__main__':
	a = MagdyAndFootball()
	print(a)
