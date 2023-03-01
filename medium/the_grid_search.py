# https://www.hackerrank.com/challenges/the-grid-search/problem


# ===================================
# find out the parttern in a whole
# ===================================
def gridSearch(G, P):
    
    for i in range(R):
        for j in range(C):
            
            if G[i][j]==P[0][0] and (C-j)>=c and (R-i)>=r:
                # print('---')
                counter = 0
                for k,u in zip(range(i,i+r),range(r)):
                    # print(G[k][j:j+c], P[u], i,i+r, r)
                    if G[k][j:j+c]==P[u]:
                        counter+=1
                if counter==r:
                    return 'YES'
                        
    return 'NO'
            