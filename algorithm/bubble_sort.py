def bubble_sort(arr):
    """
    This function return the number of swap needed to sort a arr
    starting from second element in a arr, comparing with previous value
    """
    counter = 0
    for i in range(len(arr)):
        while arr[i]<arr[i-1] and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            counter+=1
            i -=1
    return counter