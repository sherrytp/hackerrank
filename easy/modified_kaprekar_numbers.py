# https://www.hackerrank.com/challenges/kaprekar-numbers/problem?h_r=next-challenge&h_v=zen

def kaprekarNumbers(p, q):
    res = []
    for i in range(p, q+1, 1):
        if i==1:
            res.append(str(i))
        elif i>8:
            sqr = str(i**2)
            d = len(str(i))
            l,r = int(sqr[:len(sqr)-d]), int(sqr[-d:])
            if l+r==i:
                res.append(str(i))
    if len(res)==0:
        print('INVALID RANGE')
    else:
        print(' '.join(res))