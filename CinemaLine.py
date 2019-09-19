# http://codeforces.com/contest/349/problem/A

def CinemaLine():
    n = int(input())
    line = [int(i) for i in input().strip().split()]
    cashier  = {25:0, 50:0, 100:0}
    
    if line[0] != 25:
        return 'NO'

    for person in line:
        
        change = (person - 25)
        # if the change is more money than the clerck have
        if (cashier[25]*25 + cashier[50]*50) < change:
            return 'NO'
        else:
            # if change > 50s, and we have 50. give the person enough 50s
            # and deduct the given 50s from the clerck.
            # else: check for 25s
            if cashier[50] >= (change//50):
                cashier[50] -= change//50
                change -= (change//50)*50
            
            # if change/remaining change > 25 and we have 25s, give out enough 25s.
            # and deduct the given 25s from the clerck.
            if cashier[25] >= (change//25):
                cashier[25] -= change//25
                change -= (change//25)*25
            
            # if there is still some money for the person, the clerk doesn't have enough money
            # for him. so we return a 'NO'
            if change > 0:
                return 'NO'
            else:
                cashier[person] += 1

    return 'YES'


if __name__ == '__main__':
    a = CinemaLine()
    print(a)