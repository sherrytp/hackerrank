# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def substrCount(n, s):
    i = 0
    res = 0
    while (i<n):
        char = 1
        while (i+1<n and s[i]==s[i+1]):
            i+=1
            char+=1
        res += int(char*(char+1)/2)  # number of combinations of letter in a string = n*(n+1)/2
        i+=1

    for i in range(1, n):
        char = 1
        while ((i+char<n) and # make sure pointer + char less than n
               (i-char>=0) and # make sure pointer + char more than or equal to 0
               (s[i]!=s[i+1]) and # make sure current value and next value is different
               (s[i-char]==s[i+char]) and # make sure the value to the left of pointer and right of the pointer are the same
               (s[i-1]==s[i-char])): # make sure the value to the left or right of the pointer is the same. meaning aabaa: first and second is also 'a'
            char+=1
        res += char-1 # we start with 1 as char, if just one value and we goes to the while loop, char will be 2, so we need to deduct by one
    return res

s = input()
n = int(input())
print(substrCount(n, s))


