# https://www.hackerrank.com/challenges/largest-permutation/problem


def largestPermutation(k:int, arr:list):
    """
    """
    sorted_arr = sorted(arr, reverse = True)
    index_dict = {v:i for i, v in enumerate(arr)}
    counter = 0
    
    if k==0:
        print(arr)
    else:
        for i,v in enumerate(arr):
            largest_value = sorted_arr[i]
            lg_idx = index_dict[largest_value] # index for largest value in unsorted arr
            if (largest_value!=arr[i]) and (counter<k):
                arr[lg_idx], arr[i] = arr[i], arr[lg_idx]
                index_dict[v] = lg_idx 
                index_dict[largest_value] = i
                counter +=1
                
    return arr


n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(*largestPermutation(k, arr))
