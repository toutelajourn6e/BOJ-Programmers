from collections import deque

MAX = 100001
gragh = [0] * MAX

n, k = map(int, input().split())
q = deque()
q.append(n)
result = 0

while q:
    x = q.popleft()
    if x == k:
        result += 1
        continue
        
    
    for i in (x+1, x-1, x*2):
        if 0 <= i < MAX and (gragh[i] == 0 or gragh[i] == gragh[x]+1):
            q.append(i)
            gragh[i] = gragh[x] + 1
            
print(gragh[k])
print(result)