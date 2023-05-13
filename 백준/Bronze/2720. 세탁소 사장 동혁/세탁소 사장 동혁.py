t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    ans = []
    for coin in coins:
        ans.append(c // coin)
        c %= coin
        
    print(*ans)
    