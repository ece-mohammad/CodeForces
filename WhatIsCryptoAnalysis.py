
# http://codeforces.com/group/HfHdGMEg3L/contest/225031/problem/C

import string

def CryptoAnalysis():
    
    n = int(input().strip())
    
    histogram = dict()
    
    for i in range(n):
        
        line = input().strip().upper()
        
        line = ''.join( [_ for _ in line if _ in string.ascii_uppercase] )
        
        for char in line:
            histogram[char] = histogram.setdefault(char, 0) + 1
    
    for k,v in sorted( histogram.items(), key = lambda x: (x[1], x[0]), reverse = True ):
        print("{} {}".format(k, v))


if __name__ == '__main__':
    CryptoAnalysis()
