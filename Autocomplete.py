
# http://codeforces.com/group/P8UZg7UOT5/contest/225111/problem/D

def Autocomplete():
    
    s = input()
    n = int( input() )
    visited = [input().strip() for _ in range(n)]
    
    visited = filter(lambda x: x.startswith(s), visited)
    
    visited = [i for i in visited]
    
    if visited:
        visited.sort()
        return visited[0]
    else:
        return s


if __name__ == '__main__':
    a = Autocomplete()
    print(a)
