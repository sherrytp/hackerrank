
# https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    counter=0
    for i in range(len(s)-2):
        if i%3==0:
            if s[i]!='S' or s[i+1]!='O' or s[i+2]!='S':
                counter+=3-sum([s[i]=='S',s[i+1]=='O',s[i+2]=='S'])
    return counter

def marsExploration(s):
    return sum([s[i]!='SOS'[i%3] for i in range(len(s))])