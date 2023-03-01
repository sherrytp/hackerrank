# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import bisect

n, d  = map(int, input().split())
exp = list(map(int, input().split()))
arr = sorted(exp[:d])
m = d//2 # 5//2 = 2, 7//2 = 3, 8//2 = 0, 9//2 = 4
counter = 0

def med(arr, d, m):
    """calculate median for list arr, check if the list the odd or even
    """
    if d%2==0:
        return sum(arr[m-1:m+1])/2
    else: 
        return arr[m]

for i in range(d,n):
    # if current spending is greater or equal to 2* d months median
    if exp[i]>=2*med(arr, d, m):
        counter+=1
    # del the most left value in the arr
    del arr[bisect.bisect_left(arr, exp[i-d])] # i starts from d, as i increases i-d will start from 0, 1....
    bisect.insort(arr, exp[i])

print(counter)
    











