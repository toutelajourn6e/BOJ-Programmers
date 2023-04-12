from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
result = '<'

while not len(queue) == 0:
    for _ in range(k - 1):
        queue.rotate(-1)
    result += str(queue.popleft())+', '
    
    
    
result = result[:-2]
result += '>'
print(result)