
#http://codeforces.com/contest/339/problem/A

def HelpfulMath():
	
	equation = input().strip().split('+')
	
	equation.sort()
	
	return '+'.join(equation)


if __name__ == '__main__':
	a = HelpfulMath()
	print(a)
