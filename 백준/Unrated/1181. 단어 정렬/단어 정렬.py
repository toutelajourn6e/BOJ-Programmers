t = int(input())
ans = [input() for i in range(t)]
ans = set(ans)
ans = list(ans)
ans.sort()
ans = sorted(ans, key=len)
for i in ans:
    print(i)