# https://www.hackerrank.com/challenges/3d-surface-area/problem

# Complete the surfaceArea function below.
def surfaceArea(A):
    area = 2*H*W
    for i in range(H):
        for j in range(W):
            # handle row
            if i-1<0:
                area+=A[i][j]
            else:
                area+=abs(A[i][j]-A[i-1][j])
            # handle col
            if j-1<0:
                area+=A[i][j]
            else:
                area+=abs(A[i][j]-A[i][j-1])
            # check if it is last col
            if j==W-1:
                area+=A[i][j]
        # check if it is last row
        if i==H-1:
            area+=sum(A[i])
                
    return area