import sys

n = int(sys.stdin.readline().rstrip())
ans = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ans.append((x, y))

ans.sort()

for i in range(n):
    print(ans[i][0], ans[i][1])