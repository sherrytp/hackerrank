def counting_sort(arr):
    """# using counting sort when k(range of input) < n (# of integers to be sorted)
    """
    output = [0]*len(arr)
    ls = [0]*(max(arr)+1)

    # step 1: find out frequency of each value in arr save into ls list
    for i in arr:ls[i]+=1
    # step 2: create running sum for value in ls
    for i in range(len(ls)):
        if i>0:
            ls[i] = ls[i]+ls[i-1]
    # step 3: use value in arr as index position in output list
    for i in arr:
        output[ls[i]-1] = i
        ls[i]-=1
    print(output)

# enter list of numbers
ls = list(map(int, input().split()))
counting_sort(ls)
