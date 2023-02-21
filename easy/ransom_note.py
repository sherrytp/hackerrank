# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()
    for w in note:
        if not w in magazine:
            print("No")
            return
        else:
            magazine.remove(w)
    print("Yes")

magazine = input().rstrip().split()
note = input().rstrip().split()

checkMagazine(magazine, note)