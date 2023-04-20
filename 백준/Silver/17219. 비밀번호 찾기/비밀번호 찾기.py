import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
id_pw = dict()

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    id_pw[a] = b
    
for _ in range(m):
    c = input()
    if c in id_pw:
        print(id_pw[c])