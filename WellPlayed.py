##http://codeforces.com/contest/976/problem/E

class Pet(object):
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg

	def hp_sort(self):
		return (self.hp)

	def dmg_gain(self):
		return ((self.hp*2) - self.dmg)
	

def WellPlayed():
	n_pets, n_sp1, n_sp2 = map(int, input().strip().split())
	pets = list()
	ttl_dmg = 0
	
	for i in range(n_pets):
		hp, dmg = map(int, input().strip().split())
		pets.append(Pet(hp, dmg))
	
	if(n_sp1 > 0 and n_sp2 > 0):
		#sort pets by damage gain from sp1 and sp2
		gain_ranks = sorted(pets, key=Pet.dmg_gain, reverse=True)		
		
		while(n_sp1 > 0):
			gain_ranks[0].hp*=2
			n_sp1-=1
			gain_ranks = sorted(pets, key=Pet.dmg_gain, reverse=True)		
	
	#sort pets by hp
	hp_ranks = sorted(pets, key=Pet.hp_sort, reverse=True)
	
	for i in hp_ranks:
		if n_sp2 > 0:
			if i.hp > i.dmg:
				i.dmg = i.hp
				n_sp2 -= 1
	
	for i in pets:
		ttl_dmg += i.dmg
		
	return(ttl_dmg)

if __name__ == '__main__':
	a = WellPlayed()
	print(a)
