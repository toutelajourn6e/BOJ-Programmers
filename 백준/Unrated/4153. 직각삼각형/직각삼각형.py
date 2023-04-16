import sys

while 1:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if (a, b, c) == (0, 0, 0):
        break
    if (a**2) + (b**2) == c**2:
        print('right')
    elif (b**2) + (c**2) == a**2:
        print('right')
    elif (c**2) + (a**2) == b**2:
        print('right')
    else:
        print('wrong')