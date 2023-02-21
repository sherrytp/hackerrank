# https://www.hackerrank.com/challenges/equality-in-a-array/problem?h_r=next-challenge&h_v=zen


def equalizeArray(arr):
    d = dict(Counter(arr))
    d = dict(sorted(d.items(), key= lambda x:x[1], reverse = True))
    res = 0
    for i, v in enumerate(d.items()):
        if i ==0:
            pass
        else:
            res +=v[1]
    return res

# optimal solution
# =====================================
# arr.count(i) count number of i in arr
# =====================================


def equalizeArray(arr):
    return len(arr) - max(arr.count(i) for i in arr)