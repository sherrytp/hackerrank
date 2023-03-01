# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def minimumSwaps(arr):
    """functions returns a smallest swap needed to sort an no duplicated arr
    """
    counter = 0
    ref_arr = sorted(arr)
    index_dict = {v:i for i, v in enumerate(arr)}

    for i, v in enumerate(arr):
        # if current value in unsorted arr less than sorted arr, switch current value with v in sorted arr
        smallest_value = ref_arr[i]
        if v != smallest_value:
            
            to_swap_ix = index_dict[smallest_value] # find out the index for smallest value in unsorted arr
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix] # swap
            index_dict[v] = to_swap_ix
            index_dict[smallest_value] = i
            counter+=1
    print(counter)

arr = list(map(int, input().split()))
minimumSwaps(arr)


