import sys
t = int(sys.stdin.readline().rstrip())
ans = [sys.stdin.readline().rstrip() for i in range(t)]
ans = set(ans)
ans = list(ans)
ans.sort()
ans = sorted(ans, key=len)
for i in ans:
    print(i)