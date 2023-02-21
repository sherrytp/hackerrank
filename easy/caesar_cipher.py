
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem?h_r=next-challenge&h_v=zen


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    d_lower = list('abcdefghijklmnopqrstuvwxyz')
    d_upper = [v.upper() for v in letters]
    res = []
    for i in range(len(list(s))):
        if s[i].isupper():
            idx = (d_upper.index(s[i])+(k%26))%26
            res.append(d_upper[idx])
        elif s[i].islower():
            idx = (d_lower.index(s[i])+(k%26))%26
            res.append(d_lower[idx])
        else:
            res.append(s[i])
    return ''.join(res)
            