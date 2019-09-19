
# http://codeforces.com/group/P8UZg7UOT5/contest/225111/problem/E

def AmrAndMusic():
    
    n, k = map(int, input().strip().split())
    learned = []
    
    inst = [ *map(int, input().strip().split()) ]
    
    if min(inst) > k:
        
        return 0
        
    else:
    
        inst = [ (inst[i], i) for i in range(len(inst)) ]
    
        inst.sort(key = lambda x: x[0] )
        
        print(inst)
   
    
    return learned

if __name__ == '__main__':
    
    a = AmrAndMusic()
    print(a)
