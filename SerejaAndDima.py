#http://codeforces.com/contest/381/problem/A

def SerejaAndDima():
	
	n = int(input().strip())
	cards = [*map( int, input().strip().split() )]
	
	sereja = 0
	dima = 0
	
	while(n > 0):
		
		if cards[0] > cards[-1]:
			sereja += cards.pop(0)
		else:
			sereja += cards.pop(len(cards) - 1)
		
		if not cards:
			break
		
		if cards[0] > cards[-1]:
			dima += cards.pop(0)
		else:
			dima += cards.pop(len(cards) - 1)
			
		n-=2
	
	return sereja, dima

if __name__ == '__main__':
	a = SerejaAndDima()
	print(*a)
