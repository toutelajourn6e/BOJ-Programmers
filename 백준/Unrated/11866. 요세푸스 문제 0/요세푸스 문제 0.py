from collections import deque

n, k = map(int, input().split())

dq = deque([i for i in range(1, n + 1)])
result = '<'

while not len(dq) == 0:
    for _ in range(k - 1):
        dq.append(dq.popleft())
    result += str(dq.popleft())+', '
    
    
    
result = result[:-2]
result += '>'
print(result)