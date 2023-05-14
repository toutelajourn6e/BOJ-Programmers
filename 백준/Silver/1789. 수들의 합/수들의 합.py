n = int(input())
s = 0
ans = 0
i = 1

while True:
    if s + i == n:
        ans += 1
        break
    elif s + i > n:
        break
        
    s += i
    ans += 1
    
    i += 1
        
print(ans)
    