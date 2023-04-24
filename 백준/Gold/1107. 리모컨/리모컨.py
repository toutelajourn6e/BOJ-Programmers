n = int(input())
m = int(input())
br = [False] * 10

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
    
for x in a:
    br[x] = True

def possible(c):
    if c == 0:
        if br[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if br[c%10]:
            return 0
        l += 1
        c //= 10
    return l
    
    
ans = abs(n - 100)
for i in range(1000001):
    c = i
    k = possible(c) 
    if k > 0:
        press = abs(c - n)
        if ans > k + press:
            ans = k + press
            
print(ans)