n, m = map(int, input().split())
a = []
b = []
ans = 0

for _ in range(m):
    temp1, temp2 = map(int, input().split())
    a.append(temp1)
    b.append(temp2)
    
min_6 = min(a)
min_1 = min(b)


if min_6 < (min_1 * 6):
    while True:
        if n - 6 < 0:
            break
        ans += min_6
        n -= 6
    if min_6 < (min_1 * n):
        ans += min_6
    else:
        ans += (min_1 * n)
else:
    ans = min_1 * n
        
print(ans)
    