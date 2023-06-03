import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

prefix_sum = 0
prefix = [0]

for i in data:
    prefix_sum += i
    prefix.append(prefix_sum)
    
for _ in range(m):
    left, right = map(int, input().split())
    print(prefix[right] - prefix[left-1])