# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def rotLeft(a:list,d:int)->list:
    output = []
    c =0
    for i in range(len(a)):
        try:
            output.append(a[i+d])
            c+=1
        except:
            output.append(a[i-c])
    print(output)

n, d = map(int, input().split())
a  = list(map(int, input().split()))
rotLeft(a, d)