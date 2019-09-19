def reduce_word(word):
    l = len(word)
    if l > 10:
        return "{}{}{}".format(word[0], (l-2), word[-1])
    else:
        return word

def LongWords():
    n = int(input())
    for w in map(reduce_word, [input().strip() for _ in range(n)]):
        print( reduce_word(w) )

if __name__ == '__main__':
    LongWords()
