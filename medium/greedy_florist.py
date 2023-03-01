# https://www.hackerrank.com/challenges/greedy-florist/problem?h_r=next-challenge&h_v=zen

def getMinimumCost(k, c):
    c_r = sorted(c, reverse= True)
    total= []
    
    d = {i:0 for i in range(k)}
    
    for i,v in enumerate(c_r):
        total.append((d[i%k]+1)*v)
        d[i%k]+=1
    
    return sum(total)







