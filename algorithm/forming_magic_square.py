#   https://www.hackerrank.com/challenges/magic-square-forming/problem

# key here is to understand what is magic square and all possible numbers for 3x3 magic square

def ls_calculation(l1, l2):
    n = len(l1)
    s = 0
    for i in range(n):
        s+=abs(l1[i]-l2[i])
    return s

# Complete the formingMagicSquare function below.
M = [[[8,3,4],[1,5,9],[6,7,2]],
     [[6,1,8],[7,5,3],[2,9,4]],
     [[2,7,6],[9,5,1],[4,3,8]],
     [[4,9,2],[3,5,7],[8,1,6]],
     [[4,3,8],[9,5,1],[2,7,6]],
     [[8,1,6],[3,5,7],[4,9,2]],
     [[6,7,2],[1,5,9],[8,3,4]],
     [[2,9,4],[7,5,3],[6,1,8]]
]

def formingMagicSquare(s, M):
    ss = []
    for i in M:
        total = 0
        for j in range(len(i)):
            total+=ls_calculation(i[j],s[j])
        ss.append(total)
            
    return min(ss)  