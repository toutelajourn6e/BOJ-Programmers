import sys
def get_gcd(a ,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gcd = get_gcd(a, b)
    print((a*b)//gcd)
    