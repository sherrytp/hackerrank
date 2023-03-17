
# https://www.hackerrank.com/challenges/absolute-permutation/problem?h_r=next-challenge&h_v=zen

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    d = {i+1:v+1 for i,v in enumerate(range(n))}
    
    for i in range(1, n+1):
            val = i+k
            if abs(d[i]-i)!=k:
                if val>n:
                    return [-1]
                else:
                    d[i]=val
                    d[val]=i
        
    return list(d.values()) 