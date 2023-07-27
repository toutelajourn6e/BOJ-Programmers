import sys

n = int(input())
schedules = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
schedules.sort(key=lambda x: (x[1], x[0]))

ans = 0
cur = 0
for st, ed in schedules:
    if st >= cur:
        ans += 1
        cur = ed
        
print(ans)
    
   