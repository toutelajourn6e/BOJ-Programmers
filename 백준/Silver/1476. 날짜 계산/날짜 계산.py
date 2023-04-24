e, s, m = map(int, input().split())
a, b, c = 0, 0, 0
ans = 0

while a != e or b != s or c != m:
        ans += 1
        if a == 15:
            a = 1
        else:
            a += 1
        
        if b == 28:
            b = 1
        else:
            b += 1
        
        if c == 19:
            c = 1
        else:
            c += 1
            
print(ans)
