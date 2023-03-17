# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


# ===============================================================
# The key to this question is to add while loop inside for loop
# ===============================================================

def climbingLeaderboard(ranked, player):
    # Write your code here
    u_rank = list(set(ranked))
    u_rank.sort()
    n = len(u_rank)
    res = []
    i = 0
    for p in player:
        while i<n and p>=u_rank[i]:
            i+=1
        res.append(n-i+1)
    return res