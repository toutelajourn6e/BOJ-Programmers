k, n = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))
    
start = 1
end = max(cables)
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for cable in cables:
        temp += cable // mid
        
    if temp < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)