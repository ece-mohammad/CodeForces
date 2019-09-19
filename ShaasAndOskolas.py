
#http://codeforces.com/contest/294/problem/A

def ShaasAndOskolas():
	
	n_wires = int(input().strip())
	wire_birds = [ *map(int, input().strip().split() ) ]
	n_shots = int(input().strip())
	
	for i in range(n_shots):
		wire, bird = map(int, input().strip().split())
		
		wire -= 1
		
		if wire < n_wires - 1:
			wire_birds[wire+1] += (wire_birds[wire] - bird)
		
		if wire > 0:
			wire_birds[wire-1] += (bird - 1)
			
		wire_birds[wire] = 0
	
	return wire_birds
	

if __name__ == '__main__':
	a = ShaasAndOskolas()
	print(*a, sep='\n')
