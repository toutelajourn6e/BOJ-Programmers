n = int(input())
d = [0 for _ in range(n+1)]
w = [0]
for _ in range(n):
    w.append(int(input()))

d[1] = w[1]

if n >= 2:
    d[2] = w[1] + w[2]

for n in range(3, n+1):
    d[n] = d[n-1]
    d[n] = max(d[n], d[n-2] + w[n])
    d[n] = max(d[n], d[n-3] + w[n-1] + w[n])
    
print(d[n])