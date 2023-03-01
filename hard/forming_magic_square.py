# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

# https://www.youtube.com/watch?v=acGcfh4JJiI

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix) # row
    n = len(matrix[0]) # col

    k = min(m, n)//2 # number of layers
    ls = []
    
    for i in range(k):
        layer = []
        for j in range(i, n-i-1):
            layer.append(matrix[i][j])
        for j in range(i, m-1-i):
            layer.append(matrix[j][n-i-1])
        for j in range(n-1-i, i, -1):
            layer.append(matrix[m-i-1][j])
        for j in range(m-i-1, i, -1):
            layer.append(matrix[j][i])

        ls.append(layer)
    
    # find out rotated list of numbers
    new = []
    for i in range(k):
        row = ls[i]
        # find out rotation number
        rot = r%len(row)
        new.append(row[rot:]+row[:rot])
        
    # combine rotated list of numbers into one list
    new_new = []
    for i in new:
        for j in i:
            new_new.append(j)
    # replace number in new_new to matrix
    counter = 0
    for i in range(k):
        for j in range(i, n-i-1):
            matrix[i][j] = new_new[counter]
            counter+=1
        for j in range(i, m-1-i):
            matrix[j][n-i-1] = new_new[counter]
            counter+=1
        for j in range(n-1-i, i, -1):
            matrix[m-i-1][j] = new_new[counter]
            counter+=1
        for j in range(m-i-1, i, -1):
            matrix[j][i] = new_new[counter]
            counter+=1
            
    for i in matrix:
        print(*i)
