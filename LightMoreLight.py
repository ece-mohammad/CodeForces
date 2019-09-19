
#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051

def LightMoreLight():
	
	n = int(input().strip())
	
	isSquare = lambda x: (x**0.5)%1 == 0
	
	while( n ):
		
		if isSquare(n):
			yield ('yes')
		else:
			yield ('no')
		
		n = int(input())


if __name__ == '__main__':
	a = LightMoreLight()
	print(*[i for i in a], sep = '\n')
