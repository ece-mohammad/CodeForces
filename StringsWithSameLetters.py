
# http://codeforces.com/group/HfHdGMEg3L/contest/225031/problem/F

def StringsWithSameLetters():
    
    string_a, string_b = input().strip(), input().strip()
    case = 1
     
    while(string_a != "END"):
        
        if ''.join(sorted(string_a)) == ''.join(sorted(string_b)) :
            print("Case {}: same".format(case))
        else:
            print("Case {}: different".format(case))
        
        case += 1
        
        string_a, string_b = input().strip(), input().strip()

if __name__ == '__main__':
    
    StringsWithSameLetters()
