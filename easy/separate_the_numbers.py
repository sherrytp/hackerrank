# https://www.hackerrank.com/challenges/separate-the-numbers/problem



def separateNumbers(s):
    n = len(s)
    res = {}

    for i in range(1, n//2+1):
        k = 0
        total=''
        first = s[:i]
        while len(total)<n:
            current = str(int(s[:i])+k)
            total += current
            k+=1
        res[total] = i
    if s in res:
        print(f'YES {s[:res[s]]}')
    else:
        print('NO')