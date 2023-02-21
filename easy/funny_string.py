

# https://www.hackerrank.com/challenges/funny-string/problem?h_r=next-challenge&h_v=zen

def funnyString(s):
    for i,j in zip(range(len(s)-1), range(len(s)-1,1,-1)):
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(s[j])-ord(s[j-1])):return 'Not Funny'
    return 'Funny'