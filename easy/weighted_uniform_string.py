
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem


# ============================================================
# search value in dict is faster than searching value in list
# ============================================================


def weightedUniformStrings(s, queries):
    res = {}
    d = {v:i+1 for i,v in enumerate('abcdefghijklmnopqrstuvwxyz')}
    # temp = 0
    weight = 0
    for i in range(len(s)):
        if s[i]==s[i-1]:
            weight += d[s[i]]
            res[weight] = 1
        else:
            weight=0
            weight = d[s[i]]
            res[d[s[i]]]=1
            
    r = []
    for i in queries:
        if i in res:
            r.append('Yes')
        else:
            r.append('No')
    return r 
        