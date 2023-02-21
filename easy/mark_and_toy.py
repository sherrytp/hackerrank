# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def maximumToys(prices, k):
    s = sorted(prices)
    new = []
    for i, v in enumerate(prices):
        while sum(new)<k:
            new.append(s[i])
            i+=1
    if sum(new)>k:
        return len(new[0:-1])
    else:
        return len(new)
    
prices = list(map(int, input().split()))
k = int(input())

print(maximumToys(prices, k))


