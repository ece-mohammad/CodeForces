#http://codeforces.com/contest/976/problem/0

def MinimumBinaryNumber():
    n = int(input())
    num = input().strip()
    n_zeros = num.count('0')
    
    if num != '0':
        num = '1'+'0'*n_zeros
    
    return num


if __name__ == '__main__':
    a = MinimumBinaryNumber()
    print(a)