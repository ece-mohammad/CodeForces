
# http://codeforces.com/group/wcUWIXdda1/contest/218033/problem/C5

def SubStrings(string):
    
    l = len(string)
    
    if l < 4:
        return "NO"
    
    fab = lambda s: (s.find("AB"), s.find("AB")+1)
    fba = lambda s: (s.find("BA"), s.find("BA")+1)
    valid = lambda x: (x[0] > -1) and (x[1] > -1)
    overlap = lambda x, y: (x[1] == y[0]) or (x[0] == y[1])
    
    ab = fab(string)
    ba = fba(string)
    
    if valid(ab) and valid(ba):
        
        if(ab < ba):
            ba = fba(string[ab[1]:])
            
            if not valid(ba):
                return "NO"
            else:
                return "YES"
            
        else:
            ab = fba(string[ba[1]:])
            
            if not valid(ab):
                return "NO"
            else:
                "YES"
        
    else:
        return "NO"
    
    return "YES"
    
if __name__ == "__main__":
    a = input().strip()
    a = SubStrings(a)
    print(a)
