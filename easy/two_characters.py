# https://www.hackerrank.com/challenges/two-characters/problem


from itertools import combinations

def check_list(ls):
    for i in range(len(ls)-1):
        if ls[i]==ls[i+1]:return False
    return True
  
# Complete the alternate function below.
def alternate(s):
    list_s = list(s)
    two_letter = combinations(set(s),2)
    res = []
    for p in two_letter:
        temp = []
        for i in list_s:
            if i in list(p):
                temp.append(i)
        if check_list(temp):
            res.append(len(temp))
            
    if len(res)==0:
        return 0
    else:
        return max(res)