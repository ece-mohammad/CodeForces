
# http://codeforces.com/group/HfHdGMEg3L/contest/225031

import string

def is_pal_string(s):
    
    L = len(s)
    
    for i in range(L//2):
        if s[i] != s[L - i - 1]:
            return False
    return True


def MotherBear():
    
    n = int(input().strip())
    
    for i in range(n):
        
        line = input().strip().lower()
        
        line = ''.join( [ _ for _ in line if _ in string.ascii_lowercase] )
        
        if is_pal_string(line) == True:
            print("You won't be eaten!")
        else:
            print("Uh oh..")


if __name__ == '__main__':
    MotherBear()
