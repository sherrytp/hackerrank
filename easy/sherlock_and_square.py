# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def squares(a, b):
    counter = 1
    # find out first square integer in the range
    start =0
    for i in range(a, b+1):
        if int(math.sqrt(i))==math.sqrt(i):
            start = i
            first_sqr = int(math.sqrt(i))
            break
        
    if start == 0:
        return 0
    else:
        while (first_sqr+1)**2 <=b:
            first_sqr+=1
            counter+=1
        return counter