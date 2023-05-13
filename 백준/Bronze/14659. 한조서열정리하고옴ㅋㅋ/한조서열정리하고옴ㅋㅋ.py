n = int(input())
a = list(map(int, input().split()))
max_v = 0
max_num = 0

for i in range(len(a)-1):
    if max_num > a[i]:
        continue
    else:
        max_num = a[i]     
    v = 0
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            v += 1
        else:
            break
            
    if v > max_v:
        max_v = v
        
print(max_v)