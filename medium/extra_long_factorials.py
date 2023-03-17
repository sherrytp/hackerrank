# https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n):
    res = 1
    for i in range(n,1,-1):
        res *= i
    print(res)
    