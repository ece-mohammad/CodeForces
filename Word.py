
#http://codeforces.com/contest/59/problem/A

def Word():
	
	word = list( input().strip() )
	
	up_cnt = sum( map( lambda x: x.isupper(), word ) )
	low_cnt = sum( map( lambda x: x.islower(), word ) )
	
	if(up_cnt > low_cnt):
		return ''.join(word).upper()
	else:
		return ''.join(word).lower()

if __name__ == '__main__':
	a = Word()
	print(a)
