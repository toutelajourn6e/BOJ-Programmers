import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().split()
    temp = list()
    for i in s:
        i = i[::-1]
        temp.append(i)
    print(' '.join(temp))
        