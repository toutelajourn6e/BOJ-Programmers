import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = []
MAX = 100001

for _ in range(n):
    coins.append(int(input().rstrip()))

d = [MAX] * (k+1)
d[0] = 0
    
for i in range(n):
    for j in range(coins[i], k+1):
        d[j] = min(d[j], d[j - coins[i]] + 1)
        
if d[k] == MAX:
    print(-1)
else:
    print(d[k])

