# https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=next-challenge&h_v=zen

def chocolateFeast(n, c, m):
    init_buy, left = n/c, n/c
    while left>=m:
        init_buy+=1
        left-=m-1
    return int(init_buy)