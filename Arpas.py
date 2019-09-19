#http://codeforces.com/problemset/problem/742/B

def Arpa():
	count = 0
	n, x = map(int, input().split())
	nums = [*map(int, input().split())]
	
	for i in nums:
		if i^x in nums:
			#print('%d xor %d is %d' %(i, x, i^x))
			count+=1
	
	print(int(count/2))

if __name__ == '__main__':
	Arpa()
