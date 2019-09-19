#http://codeforces.com/contest/975/problem/A

class AramicWord(object):
    def __init__(self, word):
        self._word = word
        self._root = set(word)
    
    def get_root(self):
        return ''.join(sorted(set(self._root)))
    
    def get_word(self):
        return self._word


def AramicScript():
	
    n = int(input().strip())
    words = input().strip().split()
    
    for i in range(n):
        words[i] = (AramicWord(words[i]).get_root())
        
    return len(set(words))

if __name__ == '__main__':
    a = AramicScript()
    print(a)
