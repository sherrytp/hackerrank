# https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    s = list(w)
    n = len(w)
    l = n-1

    while s[l]<=s[l-1] and l>0:
        l-=1
    if l ==0:
        return 'no answer'
    else:
        idx_pivot = l-1

    # switch pivot with smallest value in sufix
    for i in range(n-1, -1, -1):
        if s[i]>s[idx_pivot]:
            s[i],s[idx_pivot] = s[idx_pivot], s[i]
            break
    return ''.join(s[:idx_pivot+1] + sorted(s[idx_pivot+1:]))
    

    