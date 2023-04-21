n = int(input())
d = [[0,0,0,0,0,0,0,0,0,0] for _ in range(1001)]
mod = 10007
for i in range(10):
    d[1][i] = 1

for n in range(2, n+1):
    for l in range(10):
        for k in range(l+1):
            d[n][l] += d[n-1][k]
            d[n][l] %= mod

print(sum(d[n]) % mod)
        