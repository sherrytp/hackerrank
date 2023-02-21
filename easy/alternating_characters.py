def alternatingCharacters(s):
    s = list(s)
    n = len(s)
    c = 0
    for i in range(n-1,0,-1):
        if s[i]==s[i-1]:
            del s[i]
            i-=1
            c+=1
    return c

