a = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))
ans = []

for i, j in zip(a, n):
    ans.append(i-j)
        
print(*ans)