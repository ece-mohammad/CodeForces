
# http://codeforces.com/group/wcUWIXdda1/contest/218033/problem/E

def BerOdFS( string ):
	
	last_char = ""
	temp = ""
	
	for char in string:
		
		if char == "/" and last_char == "/":
			continue
		else:
			last_char = char
			temp += char
	
	if(len(temp) > 1) and temp.endswith("/"):
		temp = temp[:-1]
	
	return temp

if __name__ == '__main__':
	a = input().strip()
	a = BerOdFS(a)
	print(a)
