from collections import deque
import sys
sys.setrecursionlimit(10**6)

def back(n, k):
    if n != k:
        back(n, via[k])
    print(k, end=' ')

MAX = 100001
visited = [False] * MAX
gragh = [0] * MAX
via = [0] * MAX

n, k = map(int, input().split())
visited[n] = True
q = deque()
q.append(n)

while q:
    x = q.popleft()
    
    for i in (x+1, x-1, x*2):
        if 0 <= i < MAX and visited[i] == False:
            q.append(i)
            gragh[i] = gragh[x] + 1
            visited[i] = True
            via[i] = x
            
print(gragh[k])
back(n, k)