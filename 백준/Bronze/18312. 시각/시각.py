n, k = map(int, input().split())
h = 0
m = 0
s = 0
cnt = 0

while h != n+1:
    if str(k) in str(s).zfill(2) or str(k) in str(m).zfill(2) or str(k) in str(h).zfill(2):
        cnt += 1
        
    s += 1
    
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
        
print(cnt)