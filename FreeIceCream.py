
#http://codeforces.com/contest/686/problem/A

def FreeIceCream():
	
	queue, stock = map(int, input().strip().split())
	unhappy = 0
	
	for i in range(queue):
		person, amount = input().strip().split()
		amount = int(amount)
		
		if person == '+':
			stock += amount
		
		elif person == '-':
			
			unhappy += (amount > stock)
			stock -= ((stock >= amount)*amount)
			
	return stock, unhappy

if __name__ == '__main__':
	a = FreeIceCream()
	print(*a)
