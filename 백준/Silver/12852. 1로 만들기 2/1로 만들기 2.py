n = int(input())
d = [0] * (n+1)
via = [-1] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    via[i] = i-1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
        if d[i] == d[i//2] + 1:
            via[i] = i//2

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
        if d[i] == d[i//3] + 1:
            via[i] = i//3

        
def back(n, m):
    global result
    if n != m:
        back(n, via[m])
    result.append(m)
        
print(d[n])
result = []
back(1, n)

print(*result[::-1])

