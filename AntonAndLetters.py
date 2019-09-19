
#http://codeforces.com/contest/443/problem/A
def AntonAndLetters():
    
    string = input().strip()[1:-1]
    if string != '':
        return len( set( string.split(', ') ) )
    else:
        return 0
    


if __name__ == '__main__':
    a = AntonAndLetters()
    print(a)
