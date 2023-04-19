n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = p[1]

for i in range(2, n+1):
    ans = []
    for j in range(1, i+1):
        ans.append(d[i-j] + p[j])
    d[i] = min(ans)
        
        
print(d[n])