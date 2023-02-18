def anagrams(s):
    """function prints out every combinations of letters in a string
    """
    n =len(s)
    for i in range(1,n):
        for j in range(n-i+1):
            print(''.join(s[j:j+i]))
    
s = input()
anagrams(s)