
def isEven(n):
	return not n%2


def Melon():
	
	weight = int(input())
	
	if(weight-2 and isEven(weight-2)):
		return "YES"
	else:
		return 'NO'
	

if __name__ == '__main__':
	print(Melon())
