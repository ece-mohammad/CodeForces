
#http://codeforces.com/group/P8UZg7UOT5/contest/223745/problem/E

def LectureSleep():
	n, k = map(int, input().strip().split())
	equ = [int(i) for i in input().strip().split()]		#number of equations
	awake = [int(i) for i in input().strip().split()]	#times awake/asleep
	not_awake = [i^1 for i in awake]					#times when asleep
	sleep_equ = [equ[i] if not awake[i] else 0 for i in range(n) ]	#equations during sleep time
	max_equ = None					#max number of equations
	apply_time = 0					#time to apply trick to stay awake
	ttl_equ = 0						#ttl number of equations (MAX THIS!)
	
	#add equations when awake
	for i in range(n):
		if awake[i]:
			ttl_equ += equ[i]
	
	#get apply time where the sum of equations in K time is maximum
	for i in range(n-k):
		sub_arr = sleep_equ[i:i+k]
		if max_equ is None or sum(sub_arr) > max_equ:
			max_equ = sum(sub_arr)
			apply_time = i
	
	#add equations starting from apply time
	for i in range(k):
		if awake[i+apply_time] == 0:
			ttl_equ += equ[i+apply_time]
			
	
	return ttl_equ

if __name__ == '__main__':
	a = LectureSleep()
	print(a)

