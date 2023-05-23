n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

d = [0] * (k+1)
d[0] = 1
    
for coin in coins:
    for i in range(coin, k+1):
        possible = d[i - coin]
        d[i] += possible
        
print(d[k])


