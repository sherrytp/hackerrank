# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def twoStrings(s1, s2):
        ss1 = set(s1)
        ss2 = set(s2)
        total = set(s1+s2)
        if (len(ss1)+len(ss2)==len(total)):
            return "NO"
        else:
            return "YES"









