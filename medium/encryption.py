# https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
    n = len(s)
    r, c = math.floor(math.sqrt(n)), math.ceil(math.sqrt(n))
    if r*c<n:
        r+=1
    
    res =[]
    for i in range(c):
        temp = []
        j = 0
        while i+j<n:
            temp.append(s[i+j])
            j+=c
        res.append(''.join(temp))
        
    print(' '.join(res))



# =======================================================
# print out specific length of substring in a big string
# Example: print out substring length =4.
# output: feed, theg, og
# =======================================================

ct = 0
s = 'feedthedog'
for i in range(4):
    j =0
    sub = ''
    while j<c and ct<len(s):
        sub+=s[ct]
#         print(sub, s[ct], ct, j)
        j+=1
        ct+=1
        
        
        
    print(sub)