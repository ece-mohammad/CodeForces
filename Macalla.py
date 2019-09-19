#http://codeforces.com/contest/975/problem/B

def Mancalla():
    """ #http://codeforces.com/contest/975/problem/B """
    mancalla = [int(i) for i in input().strip().split()]
    scores = list()
    
    for i in range(14):
        if mancalla[i]:
            temp = mancalla[:]
            j, temp[i] = temp[i], 0
            
            j, r = j%14, j//14
            temp = [i+r for i in temp]
            
            for k in range(1, j+1):
                if i+k >= 14:
                    new_i = i + k - 14
                else:
                    new_i = i + k
                
                temp[new_i]+=1
                
            temp = [i for i in temp if (i&1 == 0)]
            scores.append(sum(temp))
    
    return max(scores)

if __name__ == '__main__':
    a = Mancalla()
    print(a)