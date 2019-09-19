
# http://codeforces.com/group/P8UZg7UOT5/contest/225111/problem/G

def SuperMarkets():
    
    markets, kilos = map(int, input().strip().split())
    min_price = None
    
    while(markets > 0):
        
        weight, cost = map(int, input().strip().split())
        price = weight/cost
        
        if(min_price is None) or (price < min_price):
            min_price = price
        
        markets -= 1
    
    return min_price * kilos

if __name__ == '__main__':
    a = SuperMarkets()
    print(a)
