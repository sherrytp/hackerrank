# https://www.hackerrank.com/challenges/default-arguments/problem

# video explanation
# https://www.youtube.com/watch?v=_JGmemuINww



def print_from_stream(n, stream=None):
    if stream is None:
        stream=EvenStream()
    else:
        stream=OddStream()
    for _ in range(n):
        print(stream.get_next())
