from collections import deque

s = deque(input())
ans = list()
ans.append(''.join(s))

for _ in range(len(s)-1):
    s.popleft()
    ans.append(''.join(s))

for i in sorted(ans):
    print(i)
    