
def AntonAndDanik():
	
	n = int(input())
	games = input().strip()
	
	anton = games.count('A')
	danik = n - anton
	
	if anton > danik:
		return 'Anton'
	elif danik > anton:
		return 'Danik'
	else:
		return 'Friendship'

if __name__ == '__main__':
	
	a = AntonAndDanik()
	print(a)
