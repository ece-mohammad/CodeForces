
#http://codeforces.com/contest/9/problem/A

from fractions import Fraction

def DieRoll():
	
	rolls = [ *map(int, input().strip().split()) ]
	
	dom = 6 - max(rolls) + 1
	
	dot_chance =  Fraction(dom, 6)
	
	return dot_chance if dot_chance != 1 else '1/1'
	
	
if __name__ == '__main__':
	a = DieRoll()
	print(a)
