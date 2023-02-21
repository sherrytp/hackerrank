# https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    min_value = min(arr)
    max_value = max(arr)
    res = []
    
    if min_value==max_value:
        res.append(len(arr))
        return res
    else:
        
        while min_value<max_value:
            n = len(arr)
            res.append(n)
            min_value = min(arr)
            max_value = max(arr)
            i = 0
            while i<=n-1:
                arr[i] = arr[i] - min_value
                if arr[i]==0:
                    arr.pop(i)
                    i-=1
                n = len(arr)
                i+=1
                
        return res


# optimal solution
def cutTheSticks(arr):
    res = []
    while len(arr)!=0:
        res.append(len(arr))
        arr = [i for i in arr if i!=min(arr)]
    return res