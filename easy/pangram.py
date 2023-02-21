# https://www.hackerrank.com/challenges/pangrams/problem?h_r=next-challenge&h_v=zen

def pangrams(s):
    return (len(set(s.lower().replace(' ','')))==26 and 'pangram' or 'not pangram')