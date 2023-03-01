# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

def isValid(s):
    d = dict(Counter(s))
    v = d[s[0]]
    c=0
    for k in d:
        if (d[k]!=v):
            c+=1
            if abs(v-d[k])>1 and (d[k]!=1) or c>1:
                return "NO"

    return "YES"

s = input()
print(isValid(s))