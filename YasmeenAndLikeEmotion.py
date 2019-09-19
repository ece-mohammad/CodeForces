
# http://codeforces.com/group/HfHdGMEg3L/contest/225031/problem/E

import re

def YasmeenAndLikeEmotion():
    
    n = int(input().strip())
    
    for i in range(n):
        
        line = input().strip()
        
        line = re.sub('\(Y\)', "", line)
        print(line)

if __name__ == '__main__':
    YasmeenAndLikeEmotion()
