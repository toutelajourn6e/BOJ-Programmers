n = int(input())
d = [[0,0,0] for _ in range(n+2)]
d[0][0] = 1;d[0][1] = 1;d[0][2] = 1;
d[1][0] = 1;d[1][1] = 1;d[1][2] = 1;
mod = 9901

for n in range(2, n+1):
    d[n][0] = (d[n-1][0] + d[n-1][1] + d[n-1][2]) % mod 
    d[n][1] = (d[n-1][0] + d[n-1][2]) % mod
    d[n][2] = (d[n-1][0] + d[n-1][1]) % mod
    
print(sum(d[n]) % mod)