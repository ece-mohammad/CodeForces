
# http://codeforces.com/group/P8UZg7UOT5/contest/225111/problem/0

def IsSuperLucky(n):
    
    n = str(n)
    
    if not (set(n) == {'4', '7'} ):
        return False
    
    else:
        if n.count('7') == n.count('4'):
            return True
        else:
            return False


def LuckyNumbers():
    
    n = int(input().strip())
    
    is_lucky = IsSuperLucky(n)
    
    while(is_lucky is False):
        n += 1
        is_lucky = IsSuperLucky(n)
    
    return n
    

if __name__ == '__main__':
    a = LuckyNumbers()
    print(a)

