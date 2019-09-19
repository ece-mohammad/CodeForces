
#http://codeforces.com/contest/71/problem/A

def LongWords():
	n = int(input())
	for i in range(n):
		word = input().strip()
		print("{}{}{}".format(word[0], len(word)-2, word[-1]) if len(word) > 10 else word)

if __name__ == '__main__':
	a = LongWords()
