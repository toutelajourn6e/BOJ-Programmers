import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(int(input()))

data.sort()

start, end = 0, 0
interval = 0
minv = int(1e10)

while start < n and end < n:
    interval = data[end] - data[start]
    if interval == m:
        print(interval)
        sys.exit(0)
    if interval < m:
        end += 1
        continue
    
    start += 1
    minv = min(minv, interval)
    
print(minv)
        