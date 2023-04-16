import sys

def get_gcd(a, b):
    while b:
        r = a%b
        a = b
        b = r
    return a


n, s = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a = [abs(i - s) for i in a]

gcd = a[0]

for i in range(1, n):
    gcd = get_gcd(gcd, a[i])
print(gcd)