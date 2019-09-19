
def PetyaAndStrings():
	"""Compares 2 strings (s1 and s2) and returns:
	1 	: if s1 > s2
	-1	: if s2 > s1
	0 	: if s1 == s2
	"""
	
	s1 = input().strip().lower()
	s2 = input().strip().lower()
	
	return (s1 >= s2) - (s1 == s2) - (s1 < s2)

if __name__ == '__main__':
	a = PetyaAndStrings()
	print(a)
	
