# https://www.hackerrank.com/challenges/maximize-it/problem

# =======================================================================
# product function in itertools print out combination of list of list
# =======================================================================


from itertools import product

k, m = map(int, input().split())

res = []
ls = []

for i in range(k):
    n = list(map(int, input().split()))[1:]
    ls.append(n)

combo = list(product(*ls))

for i in combo:
    s = []
    for j in i:  
        s.append(j**2)
        
    res.append(sum(s)%m)


print(max(res))