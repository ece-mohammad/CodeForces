#http://codeforces.com/contest/281/problem/A

def WordCapitalization():
	word = input().strip()
	return word if word[0].isupper() else word[0].upper()+word[1:]
	
if __name__ == '__main__':
	a = WordCapitalization()
	print(a)
