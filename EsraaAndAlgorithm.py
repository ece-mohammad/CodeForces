#http://codeforces.com/group/P8UZg7UOT5/contest/223745/problem/A

def EsraaAndAlgorith():
	n , x = map(int, input().strip().split())
	arr = [int(i) for i in input().strip().split()]
	
	#for i in range(n):
		#for j in range(i+1, n):
			#if arr[i] + arr[j] == x:
				#return "YES"
	
	for i in range(n):
		if (x - arr[i]) in arr[:i]+arr[i+1:]:
			return "YES"
	
	return "No"

if __name__ == '__main__':
	a = EsraaAndAlgorith()
	print(a)
