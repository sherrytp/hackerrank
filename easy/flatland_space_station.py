# https://www.hackerrank.com/challenges/flatland-space-stations/problem


def flatlandSpaceStations(n, c):
    m = len(c)
    res = []
    c.sort()
    mx = max(c[0]-0, n-1-c[-1])
    if n==m:
        return 0
    else:
        for i in range(1,len(c)):
            if mx< (c[i]-c[i-1])//2:
                mx = (c[i]-c[i-1])//2
        return mx
            