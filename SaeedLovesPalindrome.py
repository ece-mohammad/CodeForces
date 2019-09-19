
# http://codeforces.com/group/HfHdGMEg3L/contest/225031/problem/D

def is_pal_string(s):
    return s == s[::-1]


def SaeedLovesPalindrome():
    
    word = list( input().strip() )
    
    L = len(word)
    
    for i in range(L//2+1):
        
        if word[i] == '?':
            word[i] = word[L-i-1]
            
        elif word[L-i-1] == '?':
            word[L-i-1] = word[i]
    
    word = ''.join(word)
    
    word = word.translate( word.maketrans({"?":"a"}) )
    
    if is_pal_string(word):
        print(word)
    else:
        print(-1)


if __name__ == '__main__':
    SaeedLovesPalindrome()
