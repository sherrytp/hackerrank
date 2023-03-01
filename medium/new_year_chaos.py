# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def minimumBribes(Q:list)->int:
    moves = 0
    for i in range(len(Q)-1,0,-1):
        if Q[i]!=i+1:
            if Q[i-1]==i+1:
                Q[i], Q[i-1] = Q[i-1], Q[i]
                moves+=1
            elif Q[i-2]==i+1:
                Q[i-2], Q[i-1] = Q[i-1], Q[i-2]
                Q[i], Q[i-1] = Q[i-1], Q[i]
                moves+=2
            else:
                print("Too chaotic")
                return
    print(moves)