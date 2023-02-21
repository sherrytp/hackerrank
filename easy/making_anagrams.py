# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter

def makeAnagram(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    c = 0
    for k in d1:
        if k not in d2:
            print(k, d1[k])
            c+=d1[k]
        elif k in d2 and d1[k]!=d2[k]:
            print(k, d1[k], d2[k])
            c+=abs(d1[k]-d2[k])
            
    for k in d2:
        if k not in d1:
            print(k, d2[k])
            c+=d2[k]
            
    return c
# You can direct perform arithmic on dict
def makeAnagram(a, b):
    d1 = Counter(a)
    d2 = Counter(b)

    total = (d1-d2)+(d2-d1)
    return sum(total.values())


a = input()
b = input()
print(makeAnagram(a, b))

