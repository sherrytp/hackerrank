
# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    if s ==t or (len(s)+len(t))<=k:
        return "Yes"
    elif set(s)==set(t) and abs(len(s)-len(t))<=k:
        return "Yes"
    else:
        i = 0
        while i<min(len(s),len(t)) and s[i]==t[i]:
            i+=1
        if k==(len(s)-i)+(len(t)-i):
            return "Yes"
        else:
            return "No"