# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    # your code goes here
    ls = ['A','E','I','O','U']
    k = 0
    s = 0
    n = len(string)
    for i in range(n):
        if string[i] in ls:
            k+=n-i
        else:
            s+=n-i
    if s>k:
        print(f'Stuart {s}')
    elif k==s:
        print("Draw")
    else:
        print(f'Kevin {k}')

s = input()
minion_game(s)