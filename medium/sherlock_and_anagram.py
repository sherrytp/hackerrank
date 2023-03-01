# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

from math import factorial

# with factorial function
def sherlockAndAnagrams(s):
    n = len(s)
    d = {}
    output = 0
    for i in range(1,n):
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if not subs in d:
                d[subs]=[1,0]
            else:
                d[subs][0]+=1
                d[subs][1]=factorial(d[subs][0])/(factorial(d[subs][0]-2)*factorial(2))
    for k in d:
        output +=d[k][1]
    
    return int(output)

 # without factorial function
def sherlockAndAnagrams(s):
    n = len(s)
    d = {}
    output = 0
    for i in range(1,n):
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if not subs in d:
                d[subs]=1
            else:
                d[subs]+=1
            output += d[subs]-1
  
    
    return output

s = input()
print(sherlockAndAnagrams(s))

    




