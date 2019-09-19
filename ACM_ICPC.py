
def ACM():
	scores = [ *map(int, input().split()) ]
	n = len(scores)
	scores_sum = sum(scores)
	sums = []
	
	for i in range(n-2):
		
		for j in range(i+1, n-1):
			
			for k in range(j+1, n):
				
				a = scores[i] + scores[j] + scores[k]
				
				if (scores_sum - a) == a:
				
					return 'YES'
	return 'NO'
	
	
if __name__ == '__main__':
	print(ACM())
	
