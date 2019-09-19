
#http://codeforces.com/contest/977/problem/B

def TwoGrams():
	n = int(input())
	s = input().strip()
	
	two_grams = dict()
	
	for i in range(n - 1):
		two_grams[s[i:i+2]] = two_grams.setdefault(s[i:i+2], 0) + 1
	
	
	return sorted([(two_grams[k], k) for k in two_grams.keys()], reverse=True)[0][1]

if __name__ == '__main__':
	a = TwoGrams()
	print(a)
	
