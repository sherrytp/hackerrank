# https://www.hackerrank.com/challenges/non-divisible-subset/problem


# ================= video explanation ================
# https://www.youtube.com/watch?v=NvuzTl-jTRY&t=1904s


# ======================================================================================================
# If the reminder of two numbers's sum can be divisible by k then, the two number can not be in the list
# so find out the number which in each reminder's category
# if k = 4, find out the reminder of values = 0 (can be divisible), 1, 2, 3
# ======================================================================================================


def nonDivisibleSubset(k, s):
    # Write your code here
    f = [0]*k
    # find out freq of value after mod
    for i in range(len(s)):
        f[s[i]%k]+=1
    res = min(f[0], 1) # f[0] is the first value and it is the value which can be divisible by k
    for i in range(1, k//2+1):
        if i!=k-i:
            res += max(f[i], f[k-i])
        else:
            res+= min(f[i], 1)
    return res
    