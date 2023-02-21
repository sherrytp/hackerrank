# https://www.hackerrank.com/challenges/gem-stones/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def gemstones(arr):
    res = []
    for i in range(len(arr)):
        res +=list(set(arr[i]))
    d = dict(Counter(res))
    counter = 0
    for k in d:
        if d[k]==len(arr):counter +=1
    return counter