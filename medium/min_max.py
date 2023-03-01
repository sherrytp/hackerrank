# https://www.hackerrank.com/challenges/angry-children/problem

def maxMin(k, arr):
    k-=1
    arr.sort()
    
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))