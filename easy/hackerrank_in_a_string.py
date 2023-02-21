
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    return ((re.search('.*'.join("hackerrank"), s) and "YES") or "NO")